### Report_8
### Alvaro Zapata Rojas
### 20173414

#### What is the research question of the article?

The authors main objective is to demonstrate: ¿How good are random forest to deal with data that presents problems of confounding and clustered errors? In this case, the data used (The National Study of Learning Mindsets) present confounding data since the treatment was more likely applied to children with a higher expectation of success. Therefore, the National Study appears not to be a randomize study and present selection effects. 

For this reason, the authors analyze the study as an observational study. In order to identify causal effects, they assume un-confoundedness.

Also, the students (10391 observations) in this study are not independently sampled; rather, they are all drawn from 76 randomly selected schools. Due to common school characteristics, children from the same school might be correlated and present clustered errors. 

Finally, the authors show how random forest address these issues related to clustered observations and selection bias. They show that random forest can be used for treatment effect estimation in observational studies.

#### What are the strengths and weaknesses of the paper's approach to answering that question?

To solve these questions the authors, propose an “R-learner” objective function for heterogeneous treatment effect estimation. Causal forests can be seen as a forest-based method motivated by the R-learner. For clustered observations the process is similar. 

The authors evaluate the causal average treatment effects from the causal forest to address heterogeneity. One strength of the paper is to show the limitation of the approach in problematic data. For instance, when testing they did not find strong evidence of treatment heterogeneity, this does not mean there is no heterogeneity present. The paper compares models to detect such heterogeneity. 

Another strength is that the pa3er provides the code used in the data treatment which may help readers and researches to replicate the results or treat another data set. 

Also, they compare the results when clustering for schools and not clustering.

#### How does this paper advance knowledge about the question, that is, what is the contribution? (If you can't find any contributions, ask yourself why the editor and referees decided to publish the article).

The authors show that Causal forests allow to deal with problems in treatment assignment and clustering. If we properly account for the clustering, we find hints of the presence of treatment heterogeneity. If the cluster analysis is ignoring the results are very different. 


#### What would be one or two specific and valuable next steps to move forward on this question?

A further step would be to analyze by luster since there is a different distribution per cluster. In a general sense, a next step would analyze non-parametric setting. 
