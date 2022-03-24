# Potential Outcomes and RCTs
## Multiconilearity

- Describe in a markdown cell what is Multicollinearity and present some examples. Use equations to explain your argument. 
- Create a 10x10 matrix following the next :
1.  9 vectors (columns) follow a normal distribution. 
2. The 10th vector is a linear combination of tree vectors.
3.  Feel free to choose any functional form for the **linear combination**. 
4. Try to find the inverse of this matrix and show what is the output you get in both R and Python.
5.  Explain why you get different results. 

## Analyzing RCT data with Precision Adjustment
Replicate the results of the script _analyzing_rct_reemployment_experiment_ both in Python and R. Follow the next instructions:
- Focus on the Treatment group 2 
- Plot two histograms for treatment and control group to see the distribution of the outcome variable _inuidur1_
- Run all specifications: 
1. classical 2-sample approach, no adjustment (CL)
2. classical linear regression adjustment (CRA)
3. interactive regression adjustment (IRA)
4. interactive regression adjustment (IRA) **using Lasso**. I already fixed the problems in the Python code so please **check again the Python script for the solution.** For this now I used another package called hdmpy, you can see how to install it in this [link](https://github.com/maxhuppertz/hdmpy). If you don´t want to use this package (which will give you the exact results as it is in R) just use the lasso from scikit-learn.

- Using the **3. interactive regression adjustment (IRA)** plot the coefficients of the next variables
1. T2*female 
2. T2*black
3. T2*agelt35
4. T2*factor(dep)1
Please comment this figure and try to give an explanation for the coefficients. 