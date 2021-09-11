1. In a markdown cell of the JN, briefly explain the idea of sample splitting to evaluate the performance
of prediction rules to a fellow student and show how to use it on the wage data. The explanation should be clear and concise (one paragraph suffices) so that a fellow student can understand. You don´t need to run any regression, just describe the steps and the intuition behind sample splitting. 
2. Replicate the PM1_Notebook1_Prediction_newdata (R and Python) JN but follow the next instructions:
- Focus on people who did not go to college (use the next variables **shs, hsg**)
- Basic model: 'lwage ~ sex + exp1 + shs + hsg+ scl + clg + mw + so + we + occ2+ ind2'
- Flexible model: 'lwage ~ (exp1+exp2+exp3+exp4+shs+hsg+scl+clg+occ2+ind2+mw+so+we)**2' 
3. In addition **Do a two examples of Partialling-Out using lasso**. Remember that we want to find the beta associated with sex. 
- Y = log(wage), D = sex
-  Example 1: Partialling-Out using lasso 1 : Matrix W = 'exp1 + shs + hsg+ scl + clg + mw + so + we + occ2+ ind2'
-  Example 2: Partialling-Out using lasso 2 : Matrix W =  (exp1+exp2+exp3+exp4+shs+hsg+scl+clg+occ2+ind2+mw+so+we)**2'
**Please, explain all the results you find!**

You have to upload both JN on Friday 17th at 18:00