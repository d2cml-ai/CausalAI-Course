## Subsection 1

    The idea of split the data to evaluate the predictive capacity of the model that uses that data is when you have a model with a high number of regressors, similar to or greater than the number of observations in the sample.

    As is known, the closer you are to the condition 'n = p' you can skew the R to the adjusted square, because as we saw in class, the difference in these values directly affects this value (insert figure 1) (* refers to estimation)

$$
R^2_a=\frac{1-n}{n-p}\frac{E_n\epsilon_i^*2\ } {E_ny^2}
$$



    This method consists of three steps. First, separate the sample into two parts, they do not necessarily have to be the same; the sample can be separated into seventy-five and twenty-five percent for example. 

    The first group, for the purposes of this explanation, will be called group 'A' or training group, and the second group will be called 'B' or test group. The idea is to estimate the basic model with the data of group 'A', because as it has been reduced, the condition 'n = p' is evaded (Figura 2).
    Group A training (r Group B testing (s)
$$

Y^r=X_1^r+\beta^*_1+\beta^*_2X^r_2
$$

    Then, rescue the estimated coefficients to introduce them with the observations of the variables in the group 'B' or test group to find the predicted dependent variable(figura 3). 
$$
Y^*= \beta_1 X_1^s+ \beta_2 X_2^s
$$

    Finally, compare the column of observations of the variable dependent on the original data with the column of predicted values previously calculated, for this, it would be expected, if the predictive capacity of the model is good, that the MSE was small, otherwise the predictive capacity of the model would not be reliable (figura 4).
$$
MSE=\frac{1}{n_s}\sum Y_i-Y^*_i
$$

