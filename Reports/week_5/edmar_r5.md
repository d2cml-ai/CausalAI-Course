# REPORT Nº 5
Edmar Quispe Duran

<div style="text-align: justify">

### Double Machine Learning and Automated Confounder Selection - A Cautionary Tale & Crash Course in Good and Bad Controls

##### 1. What is the research question of both articles?
Both articles discuss bad and good controls and what is the consequence of using them in regressions. Cinelli, Forney and Pearl (2022) emphasize the analysis of the problem known as "bad control" and how it has been approached in statistics and econometrics, since this addition to a regression equation produces a discrepancy between the regression coefficient and the effect that the coefficient is intended to represent, so they propose graphical tools to understand, visualize and solve the problem. On the other hand, Hünermund, Louw and Caspi (2022) show how sensitive the Double machine learning (DML) is to the inclusion of even a few "bad controls", and they claim to address the consequences of do the DML with bad control variables.

##### 2. What are the strengths and weaknesses of both papers' approaches to responding to that question?
The strengths of the first article by Cinelli et al. is that they use a graphical tool called DAG to plot the causal relationships and then condition on a set of variables that will give the causal effect, and I consider that the weakness of the article is in the conditioning on the variables and that this generally blocks the flow of association, but conditioning on a collider (common effect) will induce association between variables that are not causally related.

In the case of Hünermund et al. the strengths of the paper are that they highlight the problems involved in benchmarking correspondence learning against other methods, such as naive LASSO, and also provide an empirical application.

##### 3. How do the papers advance knowledge about the question, i.e., what is the contribution? (If you can't find any contributions, ask yourself why the editor and the referees decided to publish the articles)
The contributions of both papers mainly address the problem of "bad controls" and how these can affect the estimates and the interpretation of the coefficients. This is because researchers tend to misinterpret control variables, and perhaps a way out would be to better prepare researchers on these issues.

##### 4. What would be one or two specific and valuable next steps to move forward on this question?
I consider that the next steps, in the case of Cinelli et al. research, would be an empirical application with multiple controls. And for Hünermund et al. case, to investigate other solutions to be applied in the Double machine learning (DML) framework in the variable selection problem, since two main solutions to variable selection are proposed in the literature: a) partialling out, and b) double selection.