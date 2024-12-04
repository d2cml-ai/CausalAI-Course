#Part 1
#1.1. Load the data 

library(readr)

rm(list = ls())

ruta <- "C:/Users/Usuario/Desktop/Cursos PUCP/Ciclo 2024-2/Computacional/Assignment 5/data/experimental_control.csv"
datos <- read_csv(ruta)

# Means of re78 for treatment and control groups
mean_treatment <- mean(datos$re78[datos$treat == 1], na.rm = TRUE)
mean_control <- mean(datos$re78[datos$treat == 0], na.rm = TRUE)

#1.2. Find the ATE

# Calculate ATE (SDM)
ATE <- mean_treatment - mean_control

# Results
cat("Average Treatment Effect (ATE):", ATE, "\n")

#Interpretation: The ATE is positive so the program may have had a positive impact on participants' earnings in 1978.

#1.4. Heterogeneous effects with causal forests

Y <- datos$re78
W <- datos$treat
X <- datos[, c("age", "educ", "black", "hisp", "marr", "nodegree", "re74", "re75")]

library(grf)
tree <- causal_forest(X, Y, W, num.trees = 1,
                      mtry = ncol(X), min.node.size = 1800)

get_tree(tree, 1)

#1.5. Plot heterogeneous effects

datos$effects <- 7 * exp(-(datos$age - 35)^2 / 100) +
  3 * datos$educ - 2 * datos$black +
  datos$hisp - 2.5

# Asegurarte de que los efectos no sean negativos
datos$effects[datos$effects < 0] <- 0

# Crear los intervalos de tiempo redondeando al 0.5 más cercano (usando "age")
datos$time_bins <- floor(datos$age * 2) / 2

# Calcular los efectos promedio reales para cada intervalo de tiempo
effects_bins <- aggregate(effects ~ time_bins, data = datos, mean)

# Generar predicciones usando el modelo (suponiendo que "cf" está entrenado)
X <- datos[, c("age", "educ", "black", "hisp", "marr", "nodegree", "re74", "re75")] # Predictores
datos$predicted_effects <- predict(tree, X)$predictions

# Calcular los efectos promedio predichos para cada intervalo de tiempo
predicted_effects_bins <- aggregate(predicted_effects ~ time_bins, data = datos, mean)

# Graficar efectos reales vs. predichos
plot(effects_bins$time_bins, effects_bins$effects, type = "l", col = "blue",
     xlab = "Time Bins", ylab = "Effects", main = "Actual vs Predicted Effects Bins")
lines(predicted_effects_bins$time_bins, predicted_effects_bins$predicted_effects, col = "red")
legend("topright", legend = c("Actual Effects", "Predicted Effects"), col = c("blue", "red"), lty = 1)


#Part 2: Double/Debiased machine learning in observational data

ruta_2 <- "C:/Users/Usuario/Desktop/Cursos PUCP/Ciclo 2024-2/Computacional/Assignment 5/data/biased_control.csv"
datos_2 <- read_csv(ruta_2)

library(dplyr)

summary_stats <- datos_2 %>%
  group_by(treat) %>%
  summarise(
    mean_age = mean(age, na.rm = TRUE),
    sd_age = sd(age, na.rm = TRUE),
    min_age = min(age, na.rm = TRUE),
    max_age = max(age, na.rm = TRUE),
    mean_educ = mean(educ, na.rm = TRUE),
    sd_educ = sd(educ, na.rm = TRUE),
    min_educ = min(educ, na.rm = TRUE),
    max_educ = max(educ, na.rm = TRUE),
    mean_re74 = mean(re74, na.rm = TRUE),
    sd_re74 = sd(re74, na.rm = TRUE),
    min_re74 = min(re74, na.rm = TRUE),
    max_re74 = max(re74, na.rm = TRUE)
  )

print(summary_stats)

#En cuanto a la edad, el grupo de tratamiento es significativamente más joven, con una media de 25.8 años frente a los 33.2 años del grupo de control.
#Respecto al nivel educativo, el grupo de tratamiento también tiene menos años de educación (promedio de 10.3 años) en comparación con el grupo de control (12.0 años), lo que sugiere que los participantes del tratamiento tienen, en promedio, menor nivel educativo.
#En relación a los ingresos reales de 1974 (re74), el grupo de tratamiento presenta una media mucho más baja, con 2.10 mil dólares frente a los 14.0 mil dólares del grupo de control, lo que indica que, en promedio, el grupo de tratamiento tenía ingresos significativamente menores en ese año. 

# Calcular la diferencia de medias
mean_treat <- mean(datos_2$re74[datos_2$treat == 1], na.rm = TRUE)
mean_control <- mean(datos_2$re74[datos_2$treat == 0], na.rm = TRUE)
diff_means <- mean_treat - mean_control

# Calcular el pooled standard deviation
sd_treat <- sd(datos_2$re74[datos_2$treat == 1], na.rm = TRUE)
sd_control <- sd(datos_2$re74[datos_2$treat == 0], na.rm = TRUE)
n_treat <- sum(datos_2$treat == 1, na.rm = TRUE)
n_control <- sum(datos_2$treat == 0, na.rm = TRUE)

pooled_sd <- sqrt(((n_treat - 1) * sd_treat^2 + (n_control - 1) * sd_control^2) / (n_treat + n_control - 2))

# Calcular el SMD
smd <- diff_means / pooled_sd

library(xtable)
library(randomForest)
library(hdm)
library(glmnet)
library(sandwich)

y = as.matrix(datos_2[,8,9])         # outcome: growth rate
d = as.matrix(datos_2[,1])         # treatment: initial wealth
x = as.matrix(datos_2[,-c(2,3,4,5,6,7)]) # controls: country characteristics

# some summary statistics
cat(sprintf("\nThe length of y is %g \n", length(y) ))
cat(sprintf("\nThe number of features in x is %g \n", dim(x)[2] ))

lres=summary(lm(y~d +x))$coef[2,1:2]

DML2.for.PLM <- function(x, d, y, dreg, yreg, nfold=2) {
  nobs <- nrow(x) #number of observations
  foldid <- rep.int(1:nfold,times = ceiling(nobs/nfold))[sample.int(nobs)] #define folds indices
  I <- split(1:nobs, foldid)  #split observation indices into folds
  ytil <- dtil <- rep(NA, nobs)
  cat("fold: ")
  for(b in 1:length(I)){
    dfit <- dreg(x[-I[[b]],], d[-I[[b]]]) #take a fold out
    yfit <- yreg(x[-I[[b]],], y[-I[[b]]]) # take a foldt out
    dhat <- predict(dfit, x[I[[b]],], type="response") #predict the left-out fold
    yhat <- predict(yfit, x[I[[b]],], type="response") #predict the left-out fold
    dtil[I[[b]]] <- (d[I[[b]]] - dhat) #record residual for the left-out fold
    ytil[I[[b]]] <- (y[I[[b]]] - yhat) #record residial for the left-out fold
    cat(b," ")
  }
  rfit <- lm(ytil ~ dtil)    #estimate the main parameter by regressing one residual on the other
  coef.est <- coef(rfit)[2]  #extract coefficient
  se <- sqrt(vcovHC(rfit)[2,2]) #record robust standard error
  cat(sprintf("\ncoef (se) = %g (%g)\n", coef.est , se))  #printing output
  return( list(coef.est =coef.est , se=se, dtil=dtil, ytil=ytil) ) #save output and residuals
}

#DML with OLS
cat(sprintf("\nDML with OLS w/o feature selection \n"))
dreg <- function(x,d){ glmnet(x, d, lambda = 0) } #ML method= OLS using glmnet; using lm gives bugs
yreg <- function(x,y){ glmnet(x, y, lambda = 0) } #ML method = OLS
DML2.OLS = DML2.for.PLM(x, d, y, dreg, yreg, nfold=10)


#DML with Lasso:
cat(sprintf("\nDML with Lasso \n"))
dreg <- function(x,d){ rlasso(x,d, post=FALSE) } #ML method= lasso from hdm
yreg <- function(x,y){ rlasso(x,y, post=FALSE) } #ML method = lasso from hdm
DML2.lasso = DML2.for.PLM(x, d, y, dreg, yreg, nfold=10)


#DML with Random Forest:
cat(sprintf("\nDML with Random Forest \n"))
dreg <- function(x,d){ randomForest(x, d) } #ML method=Forest
yreg <- function(x,y){ randomForest(x, y) } #ML method=Forest
DML2.RF = DML2.for.PLM(x, d, y, dreg, yreg, nfold=10)

#DML MIX:
cat(sprintf("\nDML with Lasso for D and Random Forest for Y \n"))
dreg <- function(x,d){ rlasso(x,d, post=FALSE) } #ML method=Forest
yreg <- function(x,y){ randomForest(x, y) } #ML method=Forest
DML2.mix = DML2.for.PLM(x, d, y, dreg, yreg, nfold=10)

prRes.D<- c( mean((DML2.OLS$dtil)^2), mean((DML2.lasso$dtil)^2), mean((DML2.RF$dtil)^2), mean((DML2.mix$dtil)^2));
prRes.Y<- c(mean((DML2.OLS$ytil)^2), mean((DML2.lasso$ytil)^2),mean((DML2.RF$ytil)^2),mean((DML2.mix$ytil)^2));
prRes<- rbind(sqrt(prRes.D), sqrt(prRes.Y));
rownames(prRes)<- c("RMSE D", "RMSE Y");
colnames(prRes)<- c("OLS", "Lasso", "RF", "Mix")

table <- matrix(0,4,4)

# Point Estimate
table[1,1] <- as.numeric(DML2.OLS$coef.est)
table[2,1] <- as.numeric(DML2.lasso$coef.est)
table[3,1] <- as.numeric(DML2.RF$coef.est)
table[4,1]   <- as.numeric(DML2.mix$coef.est)

# SE
table[1,2] <- as.numeric(DML2.OLS$se)
table[2,2] <- as.numeric(DML2.lasso$se)
table[3,2] <- as.numeric(DML2.RF$se)
table[4,2]   <- as.numeric(DML2.mix$se)

# RMSE Y
table[1,3] <- as.numeric(prRes[2,1])
table[2,3] <- as.numeric(prRes[2,2])
table[3,3] <- as.numeric(prRes[2,3])
table[4,3]   <- as.numeric(prRes[2,4])

# RMSE D
table[1,4] <- as.numeric(prRes[1,1])
table[2,4] <- as.numeric(prRes[1,2])
table[3,4] <- as.numeric(prRes[1,3])
table[4,4]   <- as.numeric(prRes[1,4])

# print results
colnames(table) <- c("Estimate","Standard Error", "RMSE Y", "RMSE D")
rownames(table) <- c("OLS", "Lasso", "RF", "RF/Lasso Mix")

print(table, digit=3)




