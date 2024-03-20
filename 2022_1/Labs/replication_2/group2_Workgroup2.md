# Workgroup 2 - Group #2
- Luis
- Álvaro
- Diego

## 1. In a markdown cell of the Visual Code, explain the idea of sample splitting to evaluate the performance of prediction as presented in class. Use equations in your explanation.

When we try to ger the better prediction model, we can split the sample. By doing this, we will have two datasets randomly splitted: a training sample and a testing sample. Usually the 75% of the sample is used for training and the reimaing data is used for testing.

We take the original model as: 
$$ Y = \beta_1 X_1 + \beta_2 X_2 $$ 
An a functional model of the regression as:
$$f(X) = \beta_1 X_1 + \beta_2 X_2 $$
 
We split it as:
$$ Y = [ Y^{train} \   Y^{test}] $$ 
$$ X_1 = [X_1^{train} \   X_1^{test}] $$
$$ X_2 = [X_2^{train} \   X_2^{test}] $$ 

In order to estimate the prediction rule, we proceed to regress:  $ Y^{train} $ ~ $ X_1^{train},  X_2^{train}$ to obtain the estimated the parameters of prediction.
$$ \hat{f}(X^{train}) = \hat\beta_1 X_1^{train} + \hat\beta_2 X_2^{train} = \hat{Y}^{train}$$

Next, we will use the testing dataset to compare the predicted outcome, $\hat{Y}^{test}$ as follows:
$$ \hat{Y}^{test} = \hat\beta_1 X_1^{test} + \hat\beta_2 X_2^{test} $$

Finally, to check the power of our prediction model, we need to obtain the Mean Squared Error from testing. As lower the MSE is, the better.
$$MSE_{test} = \frac{1}{n} \sum [Y^{test} - \hat{Y}^{test}]^2 $$


## 2. Explain what cross-validation is. Use figures, Equations, code and your intuition to explain this concept and how we used it when choosing the optimal lambda from a lasso regression.

The cross-validation method is used to compare the outcomes from different candidates to a value of interest using different portions of the data. In this case, we use the method to obtain the optimal lambda ($\lambda$) that gets the better estimated parameters of an OLS regression.

First, we present a grid of potential $\lambda$ candidates choosen arbitrarily, we will use 5:
$$ \lambda \in [ 0.1; 0.2; 0.25; 0.5 ;0.9 ] $$

Then, we continue splitting the dataset in an arbitrary number of folds, each one has the same number of elements. We will split our dataset in 10 folds, containing 10 elements each fold.

$$ K = [ \begin{matrix} 
K_1&K_2&K_3&K_4&K_5&...&K_{10}]
\end{matrix} $$

The main porpouse of this method is to evaluate every lambda and choose the one that better fits our condition. We want the $\lambda$ that minimizes the MSE for our Lasso-OLS regression, this assure us the best predictive model aviable using the least number of parameters, obtaining a parsimonious model. First, we evaluate $\lambda_1= 0.1$, using every folds to fit the model except $K_j$. In this first step, $j=1$, so we will use $K_{2-10}$ (90 elements). 
$$ \min_{b \in R^p} (Y_i - b'X_i)^2 + \lambda_1 \sum_{w=1}^{p} b_w $$

Then, we obtain the estimated $b$ that will be tested using the $K_1$ fold.
$$\hat{b}_{K_{2-10}} X_{K_1} = \hat{Y}_{K_1}$$ 

Then, we repeat the same process for $K_2$ to $K_{10}$. Finally, collect all $\hat{Y}_{K_{1-10}}$ to calculate the MSE of the model using $\lambda_1 = 0.1$ (remember that n = number of total observations):

$$MSE_{\lambda =0.1} = \frac{1}{n} \sum [Y - \hat{Y}_{K_{1-10}}]^2$$

Repeat the same process for each $\lambda$, and then compare every $MSE$ value. The $\lambda$ that returns the lower Mean Square Error, is the optimal lambda that let us get the best predictive model for our dataset.