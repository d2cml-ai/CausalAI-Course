# Observational counterpart to `experimental_control.csv` data

## Description

Data from the Current Population Survey on participation in the National Supported Work Demonstration (NSW) job-training program experiment. This is used as an observational comparison to the NSW experimental data from the `experimental_control.csv` file.

## Format

A data frame with 15992 rows and 18 variables

| Name          | Description                                                       |
|---------------|-------------------------------------------------------------------|
| treat         | In the National Supported Work Demonstration Job Training Program |
| age           | Age in years                                                      |
| educ          | Years of education                                                |
| black         | Race: Black                                                       |
| hisp          | Ethnicity: Hispanic                                               |
| marr          | Married                                                           |
| nodegree      | Has no degree                                                     |
| re74          | Real earnings 1974 (in thousands of dollars)                      |
| re75          | Real earnings 1975 (in thousands of dollars)                      |
| re78          | Real earnings 1978 (in thousands of dollars)                      |
| agesq         | Square of age in years                                            |
| agecube       | Cube of age in years                                              |
| educsq        | Square of years of education                                      |
| u74           | Unemployed status in 1974                                         |
| u75           | Unemployed status in 1975                                         |
| interaction1  | Multiplication between `educ` and `re74`                          |
| re74sq        | Square of real earnings in 1974 (in thousands of dollars)         |
| re75sq        | Square of real earnings in 1975 (in thousands of dollars)         |


## Details

This data is used in the Matching and Subclassification chapter of Causal Inference: The Mixtape by Cunningham.

## Source

Dehejia, Rajeev H., and Sadek Wahba. 1999. "Causal Effects in Nonexperimental Studies: Reevaluating the Evaluation of Training Programs." Journal of the American Statistical Association 94 (448): 1053–62.".

## References

Cunningham. 2021. Causal Inference: The Mixtape. Yale Press. https://mixtape.scunning.com/05-matching_and_subclassification#example-the-nsw-job-training-program. 