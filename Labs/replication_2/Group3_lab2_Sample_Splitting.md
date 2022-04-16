## Measuring predictive ability by Sample Splitting
---
    Group 3:
        - Andrea Ulloa 20172597
        - Angela
        - Ana Cristina
---
The idea can be summarize in three steps:

1. We have to randomly partion the data into training and testing sample. Usually, the ratio is 75 (training) and 25 (testing). For example, the total data is N. Randomly 75%N values will be selected for the training group and 25%N will be the test group.   
2.  Then, the training data is what we will use to estimate the regressor coefficients. Once those estimates are obtained, they are used to evaluate their prediction quality on the test data (out of sample).

    Use training  $Y^{TR}$ ~ $X^{TR}_1$ , $X^{TR}_2$

    $\hat{Y}^{TR}$ =  $\hat{\beta}_1$ $X^{TR}_1$ + $\hat{\beta}_2$ $X^{TR}_2$

3. Finally, 
use the estimates of the training betas and recording out of sample mean square error and $R^2$

     $\hat{\beta}_1$ , $\hat{\beta}_2$ and $X^{Test}$, $Y^{Test}$

     We get the estimated Y from the test : $\hat{Y}^{Test}$

     $\hat{Y}^{Test}$ =  $\hat{\beta}_1$ $X^{Test}_1$ + $\hat{\beta}_2$ $X^{Test}_2$

     Finally, $MSE_{test}$ and $R^2_{test}$

     $MSE_{test}$ =  $\frac{\sum_{i \in Test} (Y^{Test} - \hat{Y}^{Test})}{25\%N}$  

     $R^2_{test}$ = $ 1 - \frac{MSE_{test}}{1/m *  \sum_{i \in Test} (Y_{Test}^2)}$