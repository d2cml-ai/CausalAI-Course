# Orthogonal Learning 
You have create your analysis based on the scripts **r-notebook-experiment-on-orthogonal-learnin**g and , **python_notebook_experiment_on_orthogonal_learning**.

1. Replicate Simulation Design 1 three times using different numbers of trials. So you have to use
- The equation of Y for the three cases now is: Y = 5*D + beta*X + rnorm(n)
-  B = 50 , B = 100, B = 1000. 
- Explain what do you see in the distribution of the histograms. Where the orthogonal and Naive should be centered? 
- Why does this happen? Give an econometric explanation of this. 
- Laber your axes and legends correctly your figures. 

# Double Lasso - Testing the Convergence Hypothesis
You have to create your analysis based on the scripts **pm2_notebook_jannis** both in Python and R.
1. Explain what is the Double Lasso Approach in a markdown cell. Use equations for a better explanation. 
2. Replicate the results using the next approaches:

- OLS
- Double LASSO using cross Validation ([GLMNET ](https://glmnet.stanford.edu/articles/glmnet.html)in R and [Sklearn ](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html)in Python )
- Double Lasso using theoretical Lambda (HDM package both in R and Python)
- Double Lasso using **method="partialling out"**, this is a direct way to get results from the HDM package, check the Python script for an example, and also you have to read the [documentation](https://arxiv.org/pdf/1603.01700.pdf)  for more details. 
- Plot the main coefficient and its confidence interval of the convergence hypothesis from these 4 cases in one figure. 

You have to summit both Rand Python codes on October 8th at 18:00. 
