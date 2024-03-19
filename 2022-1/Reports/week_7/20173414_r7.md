## Report_7

### 20173414
### Alvaro Zapata Rojas

### What is the research question of the article?

In an experiment the differences of treatment have different magnitude effects on subsets of the population. This is associated to the heterogeneity of causal effects. In general, subpopulations have different characteristics, therefore are affected different from the treatment causing heterogeny of causal effects. This paper proposes a method to deal with the question on: How to estimate this heterogeneity in causal effects and to conduct inference about the magnitude of the differences in treatment effects across subsets of the population?
Similar to previous methods, these approach fits for situations where there may be many regressor relative to the number of observations, and where the relationship between treatment effects and the attributes of units is not known. The goal is to get a set of treatment effects and confidence intervals for each subgroup.

### What are the strengths and weaknesses of the paper's approach to answering that question?

One strength of this paper is that it proposes a relatively simple method to a fairly complex question. This method consists in using different samples to select the model (partitions of the tree) and to estimate the model. The result is an “Honest” model. They evaluated these processes on Causal Trees.
Subpopulations are determined according to heterogeneity of treatment effect, based on standard regression trees. The authors argue that usual methods use the training data for model selection which leads to bias results that only mitigate with further larger samples. To avoid this, the authors don’t use the same data for selecting model structure and the estimation. They don’t use the same sample to determine the partitions and for the estimation. To achieve this, they propose splitting the training sample into two parts, one for constructing the tree (including the cross-validation step) and a second for estimating treatment effects within leaves of the tree. 
Another strength is that the authors compare the adaptive and “honest” version for four varieties of Causal Trees. They show valid confidence intervals without restrictions on the number of covariates or the complexity of the data-generating process. 
Although there is a benefit in terms of eliminating bias, these approach shows that there is a trade off in sample splitting and precision. 

### How does this paper advance knowledge about the question, that is, what is the contribution? (If you can't find any contributions, ask yourself why the editor and referees decided to publish the article)

This paper contributes in the field of supervised machine learning to estimate heterogeneity of treatment effects. Since it focusses on subgroups of the population, it can estimate groups with different effects magnitudes while producing confidence intervals for these estimates with nominal coverage, despite having searched over many possible subpopulations.

### What would be one or two specific and valuable next steps to move forward on this question?

The authors say that a potentially important application of their techniques is for “data mining” in randomized experiments.
Also, since this paper uses simulated data to prove its strength, this method can be used on previous research studies to compare the different results of the implemented and this new method. These can show if the subgroups are within the confidence interval of this new method. 
