Report 9: Double/debiased machine learning for treatment and structural parameters

The authors seek to answer whether double ML is a method that allows inference of a parameter in a complex environment. The main contribution of the paper is to provide a general and simple procedure to estimate and perform inference on a parameter of interest, which is formally valid when there are high-dimensional "nuisance" parameters or in highly complex environments; i.e., the entropy of the parameter space for the nuisance parameter increases with sample size. To estimate these parameters the authors use the dual Machine Learning method. 

The strength of the paper is the structure of the paper, namely the use of the 3 empirical examples: the effects of unemployment insurance in Pennsylvania, the effects of the 401(K) program on financial assets and the effect of institutions on economic growth (examples that helped to better understand the method) . They show that the impact of regularization bias and overfitting on the parameter of interest can be eliminated by (i) orthogonal Neyman scores, which have reduced sensitivity with respect to the nuisance parameters to estimate, and use (ii) cross-fitting which provides an efficient way to partition the data. The authors call the resulting set of methods dual ML (DML). Perhaps a next step is to conduct a focused study on the different ML methods and see in which situations each technique is more robust. 



