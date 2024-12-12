###############Part 1: Heterogeneous treatment effects using causal trees and forests##############################

url <- "https://raw.githubusercontent.com/d2cml-ai/CausalAI-Course/main/Labs/Assignment/Assignment_5/data/experimental/experimental_control.csv"
data <- read.csv(url)

head(data)


#calculate mean from each groupp
mean_treat <- mean(data$re78[data$treat == 1], na.rm = TRUE)
mean_control <- mean(data$re78[data$treat == 0], na.rm = TRUE)

#ATE
ATE <- mean_treat - mean_control
ATE

#ATE shows that treat in In the National Supported Work Demonstration Job Training Program is positve
#because, on average, individuals who participated in the program experienced an increase of 1794.342 units in real earnings, re78, compared to individuals who did not participate (control group).



install.packages("grf")
library(grf)

#seperate data
X <- data[, c("age", "educ", "black", "hisp", "marr", "nodegree", "re74", "re75")]
W <- data$treat
Y <- data$re78


##################### Heterogeneous effects with causal trees#####################

cf <- causal_forest(X = X, Y = Y, W = W, num.trees = 200)

tree <- get_tree(cf, 1)  # Extraer el primer árbol
print(tree)



#First split
#r74-> Split Value: 6337.49 where if re74 <= 6337.49 the data goes to the left node and if re74 > 6337.49, the data goes to the right node (Node 3)
#Second split (node 2)
#educ-> Split Value: 10 where if educ <= 10 the data goes to the left node (node 4) and if re74 > 10, the data goes to the right node (Node 5)
#Third split (node 4)
#age-> Split Value: 27 where if age <= 27 the data goes to the left node (node 6) and if age > 27, the data goes to the right node (Node 7)
#Fourth Split (Node 6)
#age-> Split Value: 19 where if age <= 19 the data goes to the left node (node 7) and if age > 27, the data goes to the right node (Node 8)

#These splits are key factors for separating the data. Individuals with lower earnings are analyzed based on age and education, and within education, age is further used to divide the data. Therefore, the nodes reflect specific subgroups of the population with similar characteristics.


##########################. Heterogeneous effects with causal forests ###################

# estimate Heterogeneous effect
treatment_effects <- predict(cf, X)$predictions

# calculte importance of prediction's variable
variable_importance <- variable_importance(cf)

#rename colnames
colnames_X <- colnames(X)
colnames_X <- as.character(colnames_X)

#bar graph of importance of variables
df <- data.frame(Variable = colnames_X, Importance = variable_importance)
barplot(df$Importance, 
        names.arg = df$Variable, 
        las = 2, 
        main = "Variable Importance from Causal Forest", 
        col = "steelblue")

#age an re74 are highly important, representing factors in the causal relationships.
#Moderate Importance: educ and re75
#Least Important: Variables like black, marr, nodegree, and especially hisp.




##################Plot heterogeneous effects################################


# select a variable (for example, "age")
selected_variable <- X$age

# scatter plot
plot(selected_variable, treatment_effects,
     xlab = "Edad",
     ylab = "Predicted Treatment Effect",
     main = "Treatment Effect by Age",
     col = "blue",
     pch = 16)

# trend line
lines(lowess(selected_variable, treatment_effects), col = "red", lwd = 2)




###########################Part 2: Double/Debiased machine learning in observational data####################33


url2 <- "https://raw.githubusercontent.com/d2cml-ai/CausalAI-Course/main/Labs/Assignment/Assignment_5/data/observational/biased_control.csv"

data_observational <- read.csv(url2)


#separate groups
treatment_group <- data_observational[data_observational$treat == 1, ]
control_group <- data_observational[data_observational$treat == 0, ]

# calculate statistics
summary_treat <- summary(treatment_group[, c("age", "educ", "re74")])
summary_control <- summary(control_group[, c("age", "educ", "re74")])

# show results
cat("Estadísticas resumidas - Treatment Group\n")
print(summary_treat)

cat("\nEstadísticas resumidas - Control Group\n")
print(summary_control)


#treatment group
  #age where mean is 25.82, range is since 17 until 29 and most values are between 20 and 29.
  #educ where mean is 10.35,tange is since 4 until 16 and most values are between 9 and 12.
  #re74 (real earnings): where mean is 2.096, also we can see that lot of people didn't have earnings that year

#control group
  #age where mean is 33.23, range is since 16 until 25 and most values are between 24 and 42.
  #educ where mean is 12.03, range is since 0 until 8 and most values are between 11 and 13.
  #re74 where mean is 14.017 with a range since 0 until 25.862

#age: The control group is older on average (33.23 years vs. 25.82 years).
#educ: The control group has, on average, more years of study (12.03 versus 10.35 years).
#re74: The control group has significantly higher average incomes in 1974 ($14,017 vs. $2,096). Furthermore, the median for the treatment group is $0, suggesting that many had no income that year.



#############ATE###########################

mean_treat_2 <- mean(data_observational$re78[data_observational$treat == 1], na.rm = TRUE)
mean_control_2 <- mean(data_observational$re78[data_observational$treat == 0], na.rm = TRUE)

#ATE
ATE_2 <- mean_treat_2 - mean_control_2
ATE_2
  
#ATE in this case (observational data) is -8.497516
#we see ATE in experimental data is 1794.342
 
#In the experimental data, participants were randomly assigned to the treatment or control group, therefore the ATE (experimental) more accurately reflects the causal effect of the treatment on income in 1978.
#In the observational data, the treatment and control groups were not randomly assigned, so both groups are not matched with similar characteristics. Then the observational ATE reflects the treatment effect and the initial differences between the groups.





################## Using DML


install.packages("xtable")
install.packages("hdm")
install.packages("glmnet")
install.packages("randomForest")
install.packages("sandwich")
install.packages("DoubleML")
install.packages("mlr3tuning")

library(xtable)
library(sandwich)
library(mlr3tuning)
library(DoubleML)


y <- data_observational$re78  # Resultado: ingresos en 1978
d <- data_observational$treat # Tratamiento
x <- data_observational[, c("age", "educ", "black", "hisp", "marr", "nodegree", "re74", "re75")]  # Covariables



#OLS
library(glmnet)
cat(sprintf("\nDML con OLS sin selección de variables\n"))
dreg <- function(x, d) glmnet(x, d, lambda = 0)  # Modelo de regresión para D
yreg <- function(x, y) glmnet(x, y, lambda = 0)  # Modelo de regresión para Y

DML2_OLS <- DML2.for.PLM(x, d, y, dreg, yreg, nfold = 10)  # Implementación DML
print(DML2_OLS)



#LASSO
library(hdm)
cat(sprintf("\nDML con Lasso\n"))
dreg <- function(x, d) rlasso(x, d, post = FALSE)  # Modelo Lasso para D
yreg <- function(x, y) rlasso(x, y, post = FALSE)  # Modelo Lasso para Y

DML2_Lasso <- DML2.for.PLM(x, d, y, dreg, yreg, nfold = 10)
print(DML2_Lasso)


#RANDOM FOREST
library(randomForest)
cat(sprintf("\nDML con Random Forest\n"))
dreg <- function(x, d) randomForest(x, d)  # Modelo Random Forest para D
yreg <- function(x, y) randomForest(x, y)  # Modelo Random Forest para Y

DML2_RF <- DML2.for.PLM(x, d, y, dreg, yreg, nfold = 10)
print(DML2_RF)


#DML MIX
cat(sprintf("\nDML Mixto (Lasso para D y Random Forest para Y)\n"))
dreg <- function(x, d) rlasso(x, d, post = FALSE)  # Lasso para D
yreg <- function(x, y) randomForest(x, y)          # Random Forest para Y

DML2_Mix <- DML2.for.PLM(x, d, y, dreg, yreg, nfold = 10)
print(DML2_Mix)