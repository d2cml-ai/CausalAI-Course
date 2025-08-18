# Add required packages (only needs to be run once)
#import Pkg
#Pkg.add("CSV")
#Pkg.add("Distributions")
#Pkg.add("DataFrames")
#Pkg.add("Dates")
#Pkg.add("Plots")
#Pkg.add("Random")
#Pkg.add("LinearAlgebra")
#Pkg.add("LaTeXStrings")
#Pkg.add("Lasso")
#Pkg.add("Statistics")
#Pkg.add("GLMNet")
#Pkg.add("MLJ")
#Pkg.add("StatsBase")
#Pkg.add("StatsModels")
#Pkg.add("GLM")
#Pkg.add("Random")
#Pkg.add("CategoricalArrays")

# Load packages
using CSV
using Distributions
using DataFrames
using Dates
using Plots
using Random
using LinearAlgebra
using LaTeXStrings
using Lasso
using Statistics
using GLMNet
using MLJ
using StatsBase
using StatsModels
using GLM
using CategoricalArrays
using Random
using GLM

# Read the dataset
data = CSV.read("../data/data2.csv", DataFrame)

# Reemplazar valores "NA" en la columna "Salary" con `missing`
data.Salary .= replace(data.Salary, "NA" => missing)

# Convertir columnas categóricas a dummies
for col in [:League, :Division, :NewLeague]
    # Convertir a categórico
    data[!, col] = categorical(data[!, col])
    
    # Crear matriz dummy para los niveles de la columna categórica
    dummy_matrix = hcat([data[!, col] .== level for level in levels(data[!, col])]...)
    
    # Crear nombres únicos para las columnas dummy
    dummy_names = [string(col, "_", level) for level in levels(data[!, col])]
    
    # Crear un DataFrame con las columnas dummy
    dummy_df = DataFrame(dummy_matrix, Symbol.(dummy_names))
    
    # Añadir las columnas dummy al DataFrame original
    data = hcat(data, dummy_df)
end

# Eliminar las columnas originales categóricas
select!(data, Not([:League, :Division, :NewLeague]))

# Establecer una semilla para reproducibilidad
Random.seed!(123)

# Calcular el tamaño de cada conjunto
n_total = nrow(data)
n_train = round(Int, 0.9 * n_total)  # 90% para entrenamiento
n_test = n_total - n_train          # 10% para prueba

# Crear índices aleatorios para entrenamiento
train_indices = randperm(n_total)[1:n_train]

# Dividir los datos
train_set = data[train_indices, :]
test_set = data[setdiff(1:n_total, train_indices), :]

# Crear una lista de las variables independientes (todas las variables excepto "Salary")
independent_vars = setdiff(names(data), [:Salary])

# Crear la fórmula de la regresión
formula = @formula(Salary ~ 1 + $(join(independent_vars, " + ")))

# Ajustar el modelo OLS con los datos de entrenamiento
ols_model = lm(formula, train_set)

# Obtener las estimaciones puntuales (coeficientes)
beta_hat = coef(ols_model)
println("Estimaciones puntuales de β^: ", beta_hat)

# Número de muestras bootstrap
n_bootstrap = 10000

# Inicializar un array para almacenar las estimaciones bootstrap
beta_boots = zeros(n_bootstrap, length(beta_hat))

# Realizar el bootstrap
for i in 1:n_bootstrap
    # Generar una muestra bootstrap (muestra con reemplazo)
    bootstrap_sample_indices = rand(1:nrow(train_set), nrow(train_set))
    bootstrap_sample = train_set[bootstrap_sample_indices, :]

    # Ajustar el modelo OLS a la muestra bootstrap
    ols_bootstrap_model = lm(formula, bootstrap_sample)

    # Almacenar los coeficientes obtenidos del modelo bootstrap
    beta_boots[i, :] = coef(ols_bootstrap_model)
end

# Calcular los percentiles 2.5% y 97.5% de las distribuciones bootstrap
lower_percentile = 2.5
upper_percentile = 97.5

# Calcular los límites inferiores y superiores de los intervalos de confianza
beta_boots_lower = quantile(beta_boots, lower_percentile / 100)
beta_boots_upper = quantile(beta_boots, upper_percentile / 100)

println("Intervalos de confianza 95% para β^:")
println("Límite inferior: ", beta_boots_lower)
println("Límite superior: ", beta_boots_upper)

# Predecir en el conjunto de prueba
y_pred = predict(ols_model, test_set)

# Obtener los valores verdaderos de salario en el conjunto de prueba
y_true = test_set.Salary

# Calcular el MSE (Mean Squared Error)
mse = mean((y_pred .- y_true).^2)





