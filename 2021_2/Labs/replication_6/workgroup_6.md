Welcome to the last workgroup of the semester. As I already mentioned the grade from this workgroup will be duplicated on your workgroup_7 so please do your best!. You can use Jupyter Notebook or Rmarkdown. 

# 1. Causal Forest 
You have to replicate the results found in the paper of [Athey and Wager (2018) ](https://github.com/alexanderquispe/ECO224/blob/main/Report/week_7/causal_forest_Athey_Wagner_2019.pdf). I want to help you so I already found the steps you should follow to replicate this, check this [repo](https://github.com/grf-labs/grf/tree/master/experiments/acic18) and use the [code ](https://github.com/grf-labs/grf/tree/master/experiments/acic18) in there.
Please describe in detail the results you found in the next sections of the code:
1.  How the tree was built? 
2.  Estimate ATE
3.  Run best linear predictor analysis
4.  Look at school-wise heterogeneity
5.  Analysis ignoring clusters. How do the results change? 
6.  Analysis without fitting the propensity score 
7.  The code plot six plots in the **Make some plots** section, so explain what you find there. 
8. Visualize school-level covariates by treatment heterogeneity
9. CATE by school

# 2. Debiased Machine Learning
In this section, you will use the DML algorithm we have learned. You can use the [R](https://github.com/alexanderquispe/ECO224/blob/main/Labs/R_Notebooks/pm3-notebook-inference-clustering.ipynb) and [Python ](https://github.com/alexanderquispe/ECO224/blob/main/Labs/Python_Notebooks/pm3_notebook_inference_clustering.ipynb)scripts from the labs as guides.  
For this task you will use the data from [The Testing Convergence Hypothesis Lab](https://github.com/alexanderquispe/ECO224/blob/main/Labs/R_Notebooks/pm2-notebook-jannis.ipynb) (Barro-Lee growth data).

Use the next variables for the main analysis: 

**y = outcome: growth rate
d = treatment: initial wealth
x = controls: country characteristics**

You have to run the next regressions:
1. OLS without including the country characteristics.
2. OLS including the country characteristics.
3. DML using Lasso to predict y an d.
4. DML using Post-Lasso to predict y an d.
5. DML using Random Forest to predict y an d.
6. Run the best method i.e. the best combination of methods to predict y and d. 
7.  Show your results in a table as we did in the lab. 

Please, comment on all your results and explain how did you choose the best method. 

Hint:
1.  We do not need to cluster our regressions in this analysis, so you need to modify a bit the DML algorithm for not including the cluster argument in the function.
2. In the Python script focus on what you found in your Python script (not as we did in the lab using the best method from R) as the best method, no matter if it is different than the R best method. 
3. If the Random Forest Analysis takes a lot of time, just use two folds when you run the code. 
4. If you have any questions, please use this issue so everyone from the class can check the answers. 

You have to upload your results on Saturday 27th November at 18:00.



