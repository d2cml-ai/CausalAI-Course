# Assignment 4: Decision Trees and Causal Forest Analysis

This directory contains the complete implementation of Assignment 4 for the CausalAI Course, focusing on predicting heart disease using classification trees and analyzing treatment effects with causal forests.

## Directory Structure

```
Decision_Trees/
├── Python/
│   ├── input/
│   │   └── processed.cleveland.data
│   ├── output/
│   └── scripts/
│       ├── assignment_4.ipynb
│       └── COMMENTS.md
└── R/
    ├── input/
    │   └── processed.cleveland.data
    ├── output/
    └── scripts/
        ├── assignment_4.ipynb
        └── COMMENTS.md
```

### Folder Organization

- **input/**: Contains raw datasets used by the scripts
  - `processed.cleveland.data`: Cleveland heart disease dataset with 297 observations
  
- **output/**: Contains generated figures, tables, and results
  - Classification trees (initial and optimal)
  - Confusion matrices
  - Inaccuracy vs alpha plots
  - Individual treatment effect distributions
  - Feature importance charts
  - Treatment effect tercile heatmaps
  
- **scripts/**: Contains analysis code and documentation
  - `assignment_4.ipynb`: Main Jupyter notebook with all analyses
  - `COMMENTS.md`: Detailed answers to assignment questions

## Assignment Overview

### Part 1: Predicting Heart Disease Using Classification Trees (10 points)

1. **Data Cleaning (2 points)**
   - Rename variables to standard names
   - Remove missing values
   - Convert categorical variables to dummy variables
   - Create binary heart disease indicator

2. **Data Analysis (8 points)**
   - Split data into training and test sets
   - Build and visualize initial classification tree
   - Generate confusion matrix with interpretation
   - Apply cross-validation to prevent overfitting (50 alpha values, 4-fold CV)
   - Plot inaccuracy rate vs alpha
   - Build optimal tree and interpret results

### Part 2: Causal Forest Analysis (10 points)

1. **Simulate Treatment Assignment (0.5 points)**
   - Create random binary treatment variable

2. **Generate Outcome Variable (1 point)**
   - Create outcome based on: Y = (1 + 0.05×age + 0.3×sex + 0.2×restbp) × T + 0.5×oldpeak + ε

3. **OLS Estimation (1 point)**
   - Calculate average treatment effect using ordinary least squares

4. **Random Forest for Causal Effects (2 points)**
   - Estimate heterogeneous treatment effects
   - Compute individual treatment effects (ITEs)

5. **Representative Tree (2 points)**
   - Visualize treatment heterogeneity with max_depth=2 tree
   - Interpret decision rules

6. **Feature Importance (1.5 points)**
   - Compute and visualize feature importances
   - Identify key predictors of treatment response

7. **Tercile Analysis (2 points)**
   - Standardize all covariates
   - Divide patients into treatment effect terciles
   - Create heatmap showing covariate patterns by tercile

## Dataset: Cleveland Heart Disease

**Source**: UCI Machine Learning Repository (processed.cleveland.data)

**Variables**:
- `age`: Age in years
- `sex`: Sex (1 = male, 0 = female)
- `cp`: Chest pain type (1-4)
- `restbp`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol (mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- `restecg`: Resting ECG results (0-2)
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise-induced angina (1 = yes, 0 = no)
- `oldpeak`: ST depression induced by exercise
- `slope`: Slope of peak exercise ST segment (1-3)
- `ca`: Number of major vessels colored by fluoroscopy (0-3)
- `thal`: Thallium stress test result (3, 6, or 7)
- `hd`: Heart disease diagnosis (0 = no disease, 1-4 = disease severity)

## How to Run

### Python

1. Ensure you have the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

2. Open and run the Jupyter notebook:
```bash
cd Decision_Trees/Python/scripts
jupyter notebook assignment_4.ipynb
```

3. Results will be saved to `../output/`

### R

1. Ensure you have the required libraries:
```r
install.packages(c("rpart", "rpart.plot", "caret", "ggplot2", "dplyr", "tidyr", "randomForest", "pheatmap"))
```

2. Open and run the Jupyter notebook (with R kernel):
```bash
cd Decision_Trees/R/scripts
jupyter notebook assignment_4.ipynb
```

3. Results will be saved to `../output/`

## Key Results

### Classification Tree
- **Optimal Alpha**: Selected via 4-fold cross-validation to balance bias-variance
- **Pruning Benefit**: Simpler tree with better generalization
- **Test Accuracy**: Reported in confusion matrix
- **Clinical Interpretation**: Decision rules for heart disease diagnosis

### Causal Forest
- **Average Treatment Effect (ATE)**: Overall impact of medical check-up program
- **Heterogeneity**: Treatment effects vary significantly across patients
- **Key Moderators**: Age, sex, and blood pressure influence treatment response
- **Targeting Recommendations**: Identifies high-benefit patient subgroups

## Comments and Interpretation

See `COMMENTS.md` in each scripts folder for:
- Detailed answers to all assignment questions
- Interpretation of statistical results
- Clinical implications
- Discussion of methodological choices

## Due Date

**October 31, 2024 at 23:59**

Submit a link to your GitHub repository via email, indicating your group.

## Notes

- All random operations use `random_state = 123` (Python) or `set.seed(123)` (R) for reproducibility
- Figures are saved as high-resolution PNG files
- Code is documented with markdown cells explaining each step
- Both Python and R implementations produce equivalent results

## Contact

For questions about this assignment, please contact the teaching assistants:
- Alberto Trelles
- Valeria Hoyos
