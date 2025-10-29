# Assignment 4 - Comments and Answers

## Part 1: Classification Trees for Heart Disease Prediction

### Question 1.1: Data Cleaning
**Task**: Rename variables, remove missing values, create dummy variables, and create binary outcome variable.

**Answer**: 
- We successfully renamed all 14 variables according to the specified order
- Missing values (marked as '?') were removed, reducing the dataset from 303 to 297 observations
- All categorical variables (sex, cp, fbs, restecg, exang, slope, ca, thal) were converted to dummy variables using one-hot encoding
- The binary outcome variable `y` was created where 1 indicates presence of heart disease (original hd > 0) and 0 indicates no disease

### Question 1.2.1: Classification Tree
**Task**: Split data and plot initial classification tree.

**Answer**: 
- Data was split 70-30 into training and test sets using random_state=123
- The initial unpruned tree shows high complexity with many splits and leaves
- This suggests potential overfitting on the training data
- The tree uses various features including chest pain type, thalassemia results, and cardiac measurements

### Question 1.2.2: Confusion Matrix Interpretation
**Task**: Plot confusion matrix and interpret results.

**Answer**:
The initial confusion matrix reveals:
- **True Negatives (TN)**: Patients correctly identified as not having heart disease
- **False Positives (FP)**: Healthy patients misclassified as having disease (Type I error)
- **False Negatives (FN)**: Sick patients misclassified as healthy (Type II error - more serious)
- **True Positives (TP)**: Patients correctly identified as having heart disease

**Clinical Implications**:
- False negatives are particularly concerning in medical diagnosis as they mean missing actual cases
- The model's sensitivity (ability to detect disease) and specificity (ability to identify healthy) must be balanced
- High accuracy alone may not be sufficient if sensitivity is too low

### Question 1.2.3: Cross-Validation for Overfitting
**Task**: Use 4-fold cross-validation with 50 alpha values to find optimal complexity.

**Answer**:
- Generated 50 alpha (complexity) values on logarithmic scale from e^-10 to 0.05
- Used 4-fold cross-validation with random_state=123
- Optimal alpha balances model complexity with prediction accuracy
- This regularization approach prevents overfitting by penalizing tree complexity

### Question 1.2.4: Inaccuracy Rate Plot
**Task**: Plot inaccuracy rate (1 - accuracy) vs alpha.

**Answer**:
The plot shows:
- At very small alpha values: Low inaccuracy (high accuracy) but risk of overfitting
- At large alpha values: Higher inaccuracy due to underfitting
- U-shaped curve with optimal alpha at the minimum point
- This demonstrates the bias-variance tradeoff in model complexity

### Question 1.2.5: Optimal Tree Discussion
**Task**: Plot optimal tree and confusion matrix, interpret results.

**Answer**:
The pruned tree with optimal alpha shows:
- **Reduced Complexity**: Fewer splits and leaves compared to unpruned tree
- **Better Generalization**: May have slightly lower training accuracy but better test performance
- **Interpretability**: Simpler tree is easier for clinicians to understand and apply
- **Key Features**: The most important features for prediction are revealed at top splits

**Performance Metrics**:
- Sensitivity: Proportion of actual positives correctly identified
- Specificity: Proportion of actual negatives correctly identified
- The optimal model provides a good balance between these metrics

## Part 2: Causal Forest Analysis

### Question 2.1: Treatment Variable
**Task**: Create binary treatment variable T with random assignment.

**Answer**:
- Created binary variable T with binomial(1, 0.5) distribution
- This simulates random assignment to treatment (medical check-up program)
- Approximately 50% of individuals assigned to each group
- Random assignment ensures treatment is independent of patient characteristics

### Question 2.2: Outcome Variable
**Task**: Create outcome Y based on specified formula.

**Answer**:
The outcome variable Y represents cardiovascular health improvement:
- Formula: Y = (1 + 0.05×age + 0.3×sex + 0.2×restbp) × T + 0.5×oldpeak + ε
- Treatment effect varies by age, sex, and resting blood pressure
- Baseline health (oldpeak) affects outcome regardless of treatment
- Random error ε ~ N(0,1) captures unmeasured factors

**Interpretation**:
- Older patients have larger treatment effects (0.05 per year)
- Males have larger treatment effects than females (+0.3)
- Higher blood pressure associated with larger treatment effects (0.2 per mm Hg)

### Question 2.3: OLS Treatment Effect
**Task**: Calculate treatment effect using ordinary least squares.

**Answer**:
OLS regression Y ~ T provides:
- **Average Treatment Effect (ATE)**: The coefficient on T
- This is a naive estimate that doesn't account for heterogeneity
- Assumes constant treatment effect across all individuals
- Provides baseline for comparison with Random Forest estimates

### Question 2.4: Random Forest Causal Effects
**Task**: Use Random Forest to estimate heterogeneous treatment effects.

**Answer**:
The Random Forest approach:
- Created interaction terms between treatment and all covariates
- Estimated separate potential outcomes under treatment and control
- Individual Treatment Effects (ITE) = Y(treated) - Y(control)
- **Average Treatment Effect**: Mean of all ITEs
- **Heterogeneity**: Variation in ITEs across individuals shows treatment effects differ by patient characteristics

**Key Findings**:
- Treatment effects are heterogeneous across the population
- Some patients benefit much more than others
- This information can guide targeted interventions

### Question 2.5: Representative Tree
**Task**: Plot tree with max_depth=2 and interpret.

**Answer**:
The shallow tree reveals:
- **Most Important Splits**: Shows which characteristics most differentiate treatment response
- **Subgroup Effects**: Different predicted outcomes for different patient groups
- **Clinical Decision Making**: Provides interpretable rules for targeting treatment
- **Interaction Effects**: Captured through T × covariate terms

**Practical Use**:
Clinicians can use this tree to identify which patients would benefit most from the program.

### Question 2.6: Feature Importance
**Task**: Compute and visualize feature importances.

**Answer**:
The feature importance bar chart shows:
- **Top Features**: Variables most predictive of treatment response
- **Interaction Terms**: T × covariate interactions often highly important
- **Clinical Relevance**: Helps identify which patient characteristics matter most
- **Model Interpretation**: Complements tree visualization with quantitative importance

### Question 2.7: Tercile Heatmap
**Task**: Plot covariate distribution by treatment effect terciles.

**Answer**:
The heatmap reveals patient characteristics by treatment effect level:

- **Low Tercile**: Patients with smallest treatment effects
  - Tend to have certain covariate patterns (shown in blue/below average)
  
- **Medium Tercile**: Patients with moderate treatment effects
  - Middle ground in covariate distributions
  
- **High Tercile**: Patients with largest treatment effects
  - Tend to have other covariate patterns (shown in red/above average)

**Standardization**: All covariates are standardized (mean=0, sd=1) for comparability

**Clinical Implications**:
- Identifies patient profiles that respond best to treatment
- Enables targeted resource allocation
- Supports personalized medicine approaches
- Red cells indicate above-average values associated with that tercile
- Blue cells indicate below-average values

## Summary

This assignment demonstrated:
1. **Classification Trees**: Effective for interpretable prediction with proper regularization
2. **Cross-Validation**: Essential for preventing overfitting and selecting optimal model complexity
3. **Causal Inference**: Random Forest can reveal heterogeneous treatment effects
4. **Clinical Decision Making**: Machine learning insights can guide targeted interventions
5. **Visualization**: Multiple visualization techniques help communicate results to stakeholders

The combination of prediction (Part 1) and causal inference (Part 2) provides a comprehensive approach to using machine learning for medical decision-making.
