# **Frisch-Waugh-Lovell (FWL) Theorem Proof**

Given a linear regression model, we aim to demonstrate the FWL theorem using the following elements:

- **$y$**: dependent variable vector ($n \times 1$)
- **$D$**: matrix of independent variables of interest ($n \times k_1$)
- **$\beta_1$**: coefficient vector for $D$ ($k_1 \times 1$)
- **$W$**: matrix of control variables ($n \times k_2$)
- **$\beta_2$**: coefficient vector for $W$ ($k_2 \times 1$)
- **$u$**: error term vector ($n \times 1$)

The model is represented as:

$$ y = D\beta_1 + W\beta_2 + u$$

---

## **Objective**

To prove that $\Psi = \beta_1$ can be accurately estimated through the regression $e_y = e_D \Psi + \varepsilon$, employing the FWL theorem.

---

## **Proof**

### **Step 1: Control for Variables in $W$**

First, we calculate the residuals after controlling for $W$:

- **Regress $D$ on $W$:** Aim to determine the component of $D$ that is orthogonal to $W$. This is achieved by calculating the residuals $e_D$, using the projection matrix:
  
  $$M_W = I - W(W'W)^{-1}W'$$
  
  Thus, the residuals for $D$ are:
  
  $$e_D = M_W D$$ 

- **Regress $y$ on $W$:** Similarly, find the component of $y$ not explained by $W$:
  
  $$e_y = M_W y$$

### **Step 2: Estimate $\Psi$**

With the residuals obtained, we proceed to estimate $\Psi$:

- **Regress $e_y$ on $e_D$ by OLS:** 

  $$ e_y = e_D \Psi + z $$
  
  Solving for $\Psi$, we get:
  
  $$ \hat{\Psi} = (e_D'e_D)^{-1}e_D'e_y $$
  
  Substituting the expressions for residuals into $\hat{\Psi}$ yields:
  
  $$ \hat{\Psi} = (D'M_W'M_W'D)^{-1}D'M_W'M_Wy $$
  
  Which simplifies to:
  
  $$ \hat{\Psi} = (D'M_WD)^{-1}D'M_Wy $$

And this proof that $\Psi = \beta_1$.

