In this workgroup we will use bootstraping tools and causal trees. For both analysis you have to use the Pennsylvania re-employment bonus experiment (penn_jae.dat in the data folder). You have to subset your data for tg== 4 | tg==0, so we are going to compare treatment group 4 and the control group. For this exercise follow the first part of the next [notebook](https://github.com/alexanderquispe/ECO224/blob/main/Labs/R_Notebooks/analyzing-rct-reemployment-experiment.ipynb).


 # Bootstraping - Scripts in R and Python
For the bootstrap section you have to use the next equation:
log(inuidur1)~T4+ (female+black+othrace+factor(dep)+q2+q3+q4+q5+q6+agelt35+agegt54+durable+lusd+husd)
**No quadratic tem is required!!!**
Next, you have to compute the standard errors of 1,000 bootstrap estimates for the **T4, female** and **black**  variables.
Describe in detail each step you follow, and what lines of code you changed. 
Finally, present your results in a table. 

# Causal Tree - Only script in R 
Now you have to replicate de Causal tree estimation of this [script](https://github.com/alexanderquispe/ECO224/blob/main/Labs/R_Notebooks/hte_causal_tree.ipynb) but using the  Pennsylvania re-employment bonus experiment. You have to read this [intro](https://github.com/susanathey/causalTree/blob/master/briefintro.pdf) in order to answer the next questions. 
1. First run an OLS regression to find the HTE of female*T4, remember that log(inuidur1) is the endogenous variable.  Also use the HC2 correction. 

2. Replicate the causal tree estimation: 
*  Use the next specification or formula
log(inuidur1)~T4+ (female+black+othrace+factor(dep)+q2+q3+q4+q5+q6+agelt35+agegt54+durable+lusd+husd)
 
* Explain why we need to partitionate the data in three sets. 
* Why do we need to use the honest.causalTree function? 
* Explain in detail the creation of the tree and how do you choose the optimal pruned tree
* Plot the pruned tree and explain the HTE you found. 
