url <- "https://raw.githubusercontent.com/d2cml-ai/CausalAI-Course/main/data/wage2015_subsample_inference.csv"
data <- read.csv(url)
view(data)
colnames(data)

###1
#Generate the dataset with all the two-way interactions between variables.

data$sex <- as.factor(data$sex)
data$clg <- as.factor(data$clg)
data$mw <- as.factor(data$mw)
data$so <- as.factor(data$so)
data$we <- as.factor(data$we)
data$ne <- as.factor(data$ne)

formula <- lwage ~ (clg + sex + mw + so + we + ne)^2

data_interacciones <- model.matrix(formula, data = data)

data_interacciones <- as.data.frame(data_interacciones)
data_interacciones$lwage <- data$lwage
view(data_interacciones)

#Use the double lasso technique to find the effect of the treatment and it’s relevant interactions on the wage. To tune the penalization parameter in the lasso step, cross-validate it.

library(hdm)
library(glmnet)

X <- as.matrix(data_interacciones %>% select(-lwage)) 
y <- data_interacciones$lwage

#aplha=1 because it's lasso regression
cv_fit <- cv.glmnet(X, y, alpha = 1)  

#we estimated model with optimal lambda
final_model <- glmnet(X, y, alpha = 1, lambda = cv_fit$lambda.min)

coef(final_model)

#Data was prepared by transforming categorical variables into factors to enable interaction modeling
#A new data frame was constructed by modelling an interaction
#Then we found an optimal lambda to use in our regression


#Being universitary graduated has a possitve efecte in wage, becausa it increases around 0.2116 lwage 
#Being woman suggests that its group has less salary than men on -0.040989872
#mw1 has an effect of -0.036870228 and we1's effect is of 0.056576659, however, so1 and we1 don't have a significatly effect
#there are also interactions between variables 

#mainly we found where clg has most impact in wage. Interaction betwwen clg an mw (midwest) has a coeficent of 0.1044, that means that for college graduates in the Midwes, impact on wages is even greater than in other regions, giving this group an additional increase.




#2

##a
library(dagitty)


dag <- dagitty('
  dag {
    Age -> Individual_smoking_behavior 
    Sex -> Individual_smoking_behavior 
    Age -> Forced_respiratory_volume 
    Height -> Forced_respiratory_volume 
    Sex -> Forced_respiratory_volume
    Individual_smoking_behavior   -> Forced_respiratory_volume
  }
')


plot(dag)


#Firstable, we connected age and sex as a causes of individual smoking behavior, for example, a male teenager who's 18 years old could be exposed an enviorement that all his friends smokes.
#Individual_smoking_behavior has a direct effect on lung function
#age: orced vital capacity can change with age
#height is also related to lung capacity
#sex: Men generally have a greater forced vital capacity compared to women

#confounders: age and sex
#colliders: Individual_smoking_behavior and Forced_respiratory_volume
# proper controls: age and sex




##b

dag2 <- dagitty('
  dag {
    Marital_status -> Breast_fed
    Family_income -> Breast_fed
    Education -> Breast_fed
    Number_of_children -> Breast_fed
    Childcare_outside_home -> Breast_fed
    Marital_status -> Number_of_infections
    Family_income -> Number_of_infections
    Education -> Number_of_infections
    Number_of_children -> Number_of_infections
    Childcare_outside_home -> Number_of_infections
    Breast_fed -> Number_of_infections
  }
')

plot(dag2)


#Confounders: Marital status, Family income, Education, Number of children in the house and Childcare
#Colliders: Breast fed and  Number of infections of the baby
#Controls: Marital status, Family income, Education, Number of children in the house, Childcare outside the home.







########################PART 2#########################################################

library(ISLR)
library(dplyr)
library(caret)

data(Hitters)
head(Hitters)

sum(is.na(Hitters))

#delete NA

Hitters <- na.omit(Hitters)
sum(is.na(Hitters))
str(Hitters)

#create dummys
Hitters_dummy <- cbind(Hitters, model.matrix(~ League + Division + NewLeague - 1, data = Hitters))
Hitters_dummy <- subset(Hitters_dummy, select = -LeagueN)
Hitters_dummy$lsalary <- log(Hitters_dummy$Salary)  #created column called lsalary
view(Hitters_dummy)


#Divide the sample in two sets: training (90%) and testing (10%) sets


set.seed(123)

#number of obs of training model
train_size <- floor(0.9 * nrow(Hitters_dummy))

train_indices <- sample(seq_len(nrow(Hitters_dummy)), size = train_size)

#Create the training and test sets
train_set <- Hitters_dummy[train_indices, ]
test_set <- Hitters_dummy[-train_indices, ]

view(train_set)


modelo_mco_train <- lm(Salary ~ AtBat + Hits + HmRun + Runs + RBI + Walks + Years + I(Years^2) + CAtBat + CHits + CHmRun + CRuns + CRBI + CWalks +  
  DivisionW + LeagueA + NewLeagueN + PutOuts + Assists + Errors, data = train_set)

coeficientes_train <- coef(modelo_mco_train)
print(coeficientes_train)



##Use a loop to generate 10 000 bootstrap estimates.

n_bootstrap <- 10000
bootstrap_coefs <- matrix(NA, nrow = n_bootstrap, ncol = length(coef(modelo_mco_train)))

set.seed(123)  
for (i in 1:n_bootstrap) {
 
  bootstrap_sample <- train_set[sample(1:nrow(train_set), replace = TRUE), ]
  
  
  modelo_mco_bootstrap <- lm(Salary ~ AtBat + Hits + HmRun + Runs + RBI + Walks + Years + I(Years^2) + CAtBat + CHits + CHmRun + CRuns + CRBI + CWalks +  
  DivisionW + LeagueA + NewLeagueN + PutOuts + Assists + Errors, data = bootstrap_sample)
  
  
  bootstrap_coefs[i, ] <- coef(modelo_mco_bootstrap)
}

dim(bootstrap_coefs)


view(bootstrap_coefs)

##Calculate the 95% confidence intervals 


bootstrap_lower <- apply(bootstrap_coefs, 2, function(x) quantile(x, 0.025))
bootstrap_upper <- apply(bootstrap_coefs, 2, function(x) quantile(x, 0.975))


coeficientes_estimados <- coef(modelo_mco_train)


bootstrap_conf_int_lower <- coeficientes_estimados - bootstrap_upper
bootstrap_conf_int_upper <- coeficientes_estimados - bootstrap_lower


data.frame(
  Coefficient = names(coeficientes_estimados),
  Estimate = coeficientes_estimados,
  LowerCI = bootstrap_conf_int_lower,
  UpperCI = bootstrap_conf_int_upper
)


##Calculate the out of sample mean squared error of the model

predicciones_test <- predict(modelo_mco_train, newdata = test_set)

sqrt(mean((as.numeric(predicciones_test) - test_set$Salary) ^ 2))





##Fit a regression tree to predict the salary using all the features of your dataset. Follow these steps:


library(tree)
library(caret)

set.seed(42)
tree_model <- tree(Salary ~ AtBat + Hits + HmRun + Runs + RBI + Walks + Years + + I(Years^2) + CAtBat + CHits + CHmRun + CRuns + CRBI + CWalks +  
  DivisionW + LeagueA + NewLeagueN + PutOuts + Assists + Errors, 
                   data = train_set, 
                   mindev = 0, 
                   mincut = 0, 
                   minsize = 0)

plot(tree_model)
text(tree_model, pretty = 0)

#we could evaluate some predictions as we saw in class
predictions <- predict(tree_model, test_set)
sqrt(mean((as.numeric(predictions) - test_set$Salary) ^ 2))
     
tree_model_prune <- prune.tree(tree_model, k = 500000)
plot(tree_model_prune)
text(tree_model_prune, pretty = 0)
predictions_prune <- predict(tree_model_prune, test_set)
sqrt(mean((as.numeric(predictions_prune) - test_set$Salary) ^ 2))

#we made our pruned tree
cv_tree <- cv.tree(tree_model, K = 3)
cv_tree

optimal_size <- cv_tree$size[which.min(cv_tree$dev)]
optimal_size

pruned_tree <- prune.tree(tree_model, best = 11)

predicciones_pruned_tree <- predict(pruned_tree, newdata = test_set)

# MSE
sqrt(mean((as.numeric(predicciones_pruned_tree) - test_set$Salary) ^ 2))





#cross validate
cv_results <- cv.tree(tree_model, FUN = prune.tree, K = 10)

# find optimal size
optimal_size <- cv_results$size[which.min(cv_results$dev)]

# Podar el árbol utilizando el tamaño óptimo
pruned_tree <- prune.tree(tree_model, best = optimal_size)


#predictions
predicciones_pruned_tree <- predict(pruned_tree, newdata = test_set)

# MSE
sqrt(mean((as.numeric(predicciones_pruned_tree) - test_set$Salary) ^ 2))



#########Which model performs better in terms of predictive accuracy?
#we know mse of each one: ols->373.7057       and pruned tree ->395.5078
#A lower MSE value indicates that the model has a good fit to the test data, 
#suggesting that the OLS model is relatively accurate in its salary predictions.
#OLS model is better than regression tree