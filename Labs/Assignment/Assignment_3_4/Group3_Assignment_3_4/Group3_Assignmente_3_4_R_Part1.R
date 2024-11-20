install.packages("hdm")
install.packages("xtable")
install.packages("igraph")
install.packages("ggraph")
## Part 1: Double Lasso and DAGs (20 points)

##Consider the US census data from the year 2015 to analyse the effect of college graduate (clg) status
##and it’s interaction effects with gender (sex), location (mw, so,we, ne) and both on wage jointly. All
##other variables denote some other socio-economic characteristics, e.g. marital status, occupation, and
##experience.

# Cargar los datos desde el enlace proporcionado
file <- "https://raw.githubusercontent.com/CausalAIBook/MetricsMLNotebooks/main/data/wage2015_subsample_inference.csv"
data <- read.csv(file)

# Explorar la estructura de los datos
str(data)
head(data)

y <- data$lwage
Z <- subset(data, select = -c(wage, lwage))
y_log <- log(data$wage)

## A. Generate the dataset with all the two-way interactions between variables. 
## Make sure that the categorical variables are transformed to dummies properly. 
## Also, note that the resulting dataset contains the treatment and it’s interactions 
## with the other variables of interest, so you don’t need to generate them separately. (2 pts)

# Generar las interacciones de dos vías
center_colmeans <- function(x) {
  xcenter <- colMeans(x)
  x - rep(xcenter, rep.int(nrow(x), ncol(x)))
}

controls_formula <- "~ 0 + (sex + mw + so + we + C(occ2) + C(ind2) + exp1 + exp2 + exp3 + exp4)**2"
Zcontrols <- model.matrix(as.formula(controls_formula), data = Z)
Zcontrols <- center_colmeans(Zcontrols)

linear_het_formula <- "~ 0 + (sex + mw + so + we)"
Zhet <- model.matrix(as.formula(linear_het_formula), data = Z)
Zhet <- center_colmeans(Zhet)

Zhet <- as.data.frame(cbind(Zhet, "clg" = Z$clg))
nonlin_het_formula <- "~ 0 + clg + clg * (sex + mw + so + we)"
Zinteractions <- model.matrix(as.formula(nonlin_het_formula), data = Zhet)
interaction_cols <- Zinteractions[, grepl("clg", colnames(Zinteractions))]

X <- cbind(Zinteractions, Zcontrols)

## B. Use the double lasso technique to find the effect of the treatment and 
## it’s relevant interactions on the wage. To tune the penalization parameter 
## in the lasso step, cross-validate it. (4 pts)
index_clg <- grep("clg", colnames(Zinteractions))
effects_clg <- hdm::rlassoEffects(x = X, y = y, index = index_clg, post = FALSE)
result <- summary(effects_clg)
print(xtable(result$coef[, c(1, 2, 4)], type = "latex"), digits = 3)

## C. Report a summary of the estimation of the parameters of interest. (2 pts)
pointwise_ci <- confint(effects_clg, level = 0.95)
print(xtable(pointwise_ci), type = "latex")

joint_ci <- confint(effects_clg, level = 0.95, joint = TRUE)
print(xtable(joint_ci), type = "latex")

## D. A college degree has a positive impact on income, but the interactions 
## with factors such as gender and geographic location show no significant 
## differences. This indicates that the economic benefits of obtaining a degree 
## are consistent and do not vary noticeably across the groups analyzed.

## B.You are trying to study the effect of breast feeding in the number of 
## infections a baby is likely to have. Your dataset contains the following 
## variables : (5 pts)
edges <- matrix(c(
  "Individual smoking behavior", "Forced respiratory volume",
  "Age", "Forced respiratory volume",
  "Age", "Individual smoking behavior",
  "Sex", "Individual smoking behavior",
  "Sex", "Forced respiratory volume",
  "Height", "Forced respiratory volume"
), byrow = TRUE, ncol = 2)

graph <- graph_from_edgelist(edges, directed = TRUE)

ggraph(graph, layout = "fr") +
  geom_edge_link(aes(edge_alpha = 0.7), show.legend = FALSE) +
  geom_node_point(color = "skyblue", size = 10) +
  geom_node_text(aes(label = name), color = "black", fontface = "bold", size = 5) +
  theme_void() +
  ggtitle("Directed Acyclic Graph (DAG)") +
  theme(plot.title = element_text(size = 16, face = "bold"))
## B.You are trying to study the effect of breast feeding in the number of 
## infections a baby is likely to have. Your dataset contains the following 
## variables : (5 pts)

edges <- matrix(c(
  "Breast fed", "Number of infections",
  "Marital status", "Family income",
  "Family income", "Breast fed",
  "Family income", "Childcare outside home",
  "Education", "Family income",
  "Number of children", "Breast fed",
  "Childcare outside home", "Number of infections"
), byrow = TRUE, ncol = 2)

graph <- graph_from_edgelist(edges, directed = TRUE)

ggraph(graph, layout = "fr") +
  geom_edge_link(aes(edge_alpha = 0.7), show.legend = FALSE) +
  geom_node_point(color = "skyblue", size = 10) +
  geom_node_text(aes(label = name), color = "black", fontface = "bold", size = 5) +
  theme_void() +
  ggtitle("Directed Acyclic Graph (DAG)") +
  theme(plot.title = element_text(size = 16, face = "bold"))



