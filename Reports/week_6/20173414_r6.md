## Report_6

Alvaro Zapata Rojas
20173414

### What is the research question of the article?

When estimating the standard error in a study in economics there might be the question of how to calculate the standard error. On one hand, the researcher can report the heteroskedasticity-robust standard errors. On the other hand, the researcher can report the cluster standard error which is most common applied within geographic units such as states or counties. However, this two metrics have large differences and can lead to unprecise results especially when the researcher is interested in causal inference. The main question is which is it correct to adjust standard errors for clustering and when to adjust for robust? 

The authors argue however that this question is insufficient. For instance, the authors argue that the researcher should consider cluster adjustments, or at least not only, from clustered sampling, but also from the potential within cluster correlation in the causal variable whose effect is the primary focus of the analysis. 

In a causal effect analysis these correlations are important for the researcher. Given this necessity, the authors propose a method which takes into consideration this within correlations since it affects the variance. Thus, the authors consider clustering for the sampling and the design process and not whether to adjust the standard error for cluster or robust. 

### What are the strengths and weaknesses of the paper's approach to answering that question?

This paper has its strength in organizing the demonstration process. First, it presents the problem and its implication in the economics field. Then it resumes well the process it would take to solve the issue. Later it offers the mathematical demonstration. This is supported by simulations and empirical data analysis. In both cases they present the results well.

However, the mathematical demonstration in the middle pages of the paper could be overwhelming and lacks in comparing the results to real data o the simulation. 

### How does this paper advance knowledge about the question, that is, what is the contribution? (If you can't find any contributions, ask yourself why the editor and referees decided to publish the article)

This paper accomplishes three main contributions. First, it offers a new framework that separates the roles of clustering in the sampling and assignment (design) process. they find that the data are not informative about the need to adjust for clustering in the sampling, but they are informative about the need to adjust for clustering in the assignment process.

Second it shows that there are large differences in the standard errors when changing the sampling and assignment in comparison with the robust and cluster variances. The results show that the robust standard errors are generally too small, and the cluster standard errors are unnecessarily conservative. These differences show that the method of the researcher affects inference in the estimation of average treatment effects. 

Third, the propose the Causal Cluster Variance (CCV). This framework considers the within-cluster sums do not have expectation zero, and squaring them over-estimates the variance. Also, they propose a bootstrap version of the variance estimator (TSCB) Two-Stage-Cluster-Bootstrap. It consists in resampling in two stages to determine the number of treated and untreated units and then sampling those numbers for each cluster. 

### What would be one or two specific and valuable next steps to move forward on this question?

The authors point on two main issues that should be addressed in future works:

This paper only addresses the case where the assignment process has one layer. On other cases this assignment process may have multiple layers, thus requiring multi-level clustering adjustments. 

This paper only studies the estimators in least squares and fixed effect estimators. However inverse-variance weighted combinations of the between and appropriately weighted within estimators may have better properties.  

