
linear model formulation

$$
Y = \alpha D + \beta' W + \epsilon
$$

Where:

- $\alpha$ is the coefficient of interest linked to the treatment variable $D$.
- $\beta$ is a vector of coefficients associated with the control variables $W$.
- $\epsilon$ is the error term.

The residuals from Lasso regressions:

- For the outcome $Y$ on controls $W$, let the estimate be $\gamma_{YW}'$.
- For the treatment $D$ on controls $W$, let the estimate be $\gamma_{DW}'$.

The residuals are defined as:

$$
\tilde{Y} = Y - \gamma_{YW}'W
$$

$$
\tilde{D} = D - \gamma_{DW}'W
$$

We define the true parameter vector:

$$
\eta^0 = (\gamma_{DW}', \gamma_{YW}')'
$$

Since $\alpha$ is a function of $\eta$, where $\eta = (\eta_1', \eta_2')'$, we aim to show that $\alpha$ is insensitive to local perturbations around $\eta^0$:

$$
D = \frac{\partial \alpha(\eta^0)}{\partial \eta} = 0
$$

### Proposed Model

We assume the model:

$$
\tilde{Y} = a \tilde{D} + \mu
$$

$\alpha$ is the true value as it minimizes the expected square residuals.

Where $\alpha = \arg\min_{a \in \mathbb{R}} E[(\tilde{Y} - a \tilde{D})^2]$.

The moment condition for the model is:

$$
M(a, \eta) = E[(\tilde{Y}(\eta_1) - a \tilde{D}(\eta_2)) \tilde{D}(\eta_2)]
$$

Where:

$$
\tilde{Y}(\eta_1) = Y - \eta_1'W
$$

$$
\tilde{D}(\eta_2) = D - \eta_2'W
$$

At true values $\eta = \eta^0$:

$$
\tilde{Y} = Y - \gamma_{YW}'W
$$

$$
\tilde{D} = D - \gamma_{DW}'W
$$

### Application of the Implicit Function Theorem

To derive $a$ with respect to $\eta$:

$$
\frac{\partial a}{\partial \eta} = -\partial_a M(\alpha, \eta^0)^{-1} \partial_\eta M(\alpha, \eta^0)
$$

To demonstrate $\frac{\partial \alpha(\eta^0)}{\partial \eta} = 0$, we need $\partial_\eta M(\alpha, \eta^0)$ to be zero since $\partial_a M(\alpha, \eta^0)$ cannot be zero.

### Derivatives Calculation

For the first component:

$$
\frac{\partial M(\alpha, \eta^0)}{\partial \eta_1} = E\left[\frac{\partial \tilde{Y}(\eta_1)}{\partial \eta_1} \tilde{D}\right]
$$

Given that $\tilde{Y} = Y - \eta_1'W$:

$$
\frac{\partial \tilde{Y}}{\partial \eta_1} = -W
$$

Thus:

$$
\frac{\partial M(\alpha, \eta^0)}{\partial \eta_1} = E[-W \tilde{D}] = 0
$$

For the second component:

$$
\frac{\partial M(\alpha, \eta^0)}{\partial \eta_2} = E\left[(-a \frac{\partial \tilde{D}(\eta_2)}{\partial \eta_2})\tilde{D} + \frac{\partial \tilde{D}(\eta_2)}{\partial \eta_2}(\tilde{Y} - a\tilde{D})\right]
$$

Since $\tilde{D} = D - \eta_2'W$:

$$
\frac{\partial \tilde{D}}{\partial \eta_2} = -W
$$

Resulting in:

$$
\frac{\partial M(\alpha, \eta^0)}{\partial \eta_2} = -E[W\tilde{Y}] + 2E(\alpha W\tilde{D}) = 0
$$

This confirms that $\frac{\partial M}{\partial \eta_1} = 0$ and $\frac{\partial M}{\partial \eta_2} = 0$. Therefore, $\frac{\partial \alpha(\eta^0)}{\partial \eta} = 0$ is proven.
