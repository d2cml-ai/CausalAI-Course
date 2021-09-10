# Grupo 8
## - Gianfranco Soria Alosilla (20163509)

# An inferential problem: The Gender Wage Gap

In the previous lab, we already analyzed data from the March Supplement of the U.S. Current Population Survey (2015) and answered the question how to use job-relevant characteristics, such as education and experience, to best predict wages. Now, we focus on the following inference question:

What is the difference in predicted wages between men and women with the same job-relevant characteristics?

Thus, we analyze if there is a difference in the payment of men and women (*gender wage gap*). The gender wage gap may partly reflect *discrimination* against women in the labor market or may partly reflect a *selection effect*, namely that women are relatively more likely to take on occupations that pay somewhat less (for example, school teaching).

To investigate the gender wage gap, we consider the following log-linear regression model

\begin{align}
\log(Y) &= \beta'X + \epsilon\\
&= \beta_1 D  + \beta_2' W + \epsilon,
\end{align}

where $D$ is the indicator of being female ($1$ if female and $0$ otherwise) and the
$W$'s are controls explaining variation in wages. Considering transformed wages by the logarithm, we are analyzing the relative difference in the payment of men and women.

## Data analysis

We consider the same subsample of the U.S. Current Population Survey (2015) as in the previous lab. Let us load the data set.


```R
load("../data/wage2015_subsample_inference.Rdata")
attach(data) 

dim(data)
```

    The following objects are masked from data (pos = 4):
    
        ad, clg, exp1, exp2, exp3, exp4, hsg, ind, ind2, lwage, mw, ne,
        occ, occ2, scl, sex, shs, so, wage, we
    
    


<ol class=list-inline>
	<li>5150</li>
	<li>20</li>
</ol>



We focus on the subset of college-educated workers (scl, clg variables).


```R
data <- data[data$scl==1 |data$clg==1,]
dim(data)
```


<ol class=list-inline>
	<li>3068</li>
	<li>20</li>
</ol>



We can notice that the number of observations decreases. This change is reasonable because we are using a subset.

To start our (causal) analysis, we compare the sample means given gender:


```R
library(xtable)

Z <- data[which(colnames(data) %in% c("lwage","sex","shs","hsg","scl","clg","ad","ne","mw","so","we","exp1"))]

data_female <- data[data$sex==1,]
Z_female <- data_female[which(colnames(data) %in% c("lwage","sex","shs","hsg","scl","clg","ad","ne","mw","so","we","exp1"))]


data_male <- data[data$sex==0,]
Z_male <- data_male[which(colnames(data) %in% c("lwage","sex","shs","hsg","scl","clg","ad","ne","mw","so","we","exp1"))]

table <- matrix(0, 12, 3)
table[1:12,1]   <- as.numeric(lapply(Z,mean))
table[1:12,2]   <- as.numeric(lapply(Z_male,mean))
table[1:12,3]   <- as.numeric(lapply(Z_female,mean))
rownames(table) <- c("Log Wage","Sex","Less then High School","High School Graduate","Some College","Gollage Graduate","Advanced Degree", "Northeast","Midwest","South","West","Experience")
colnames(table) <- c("All","Men","Women")
tab<- xtable(table, digits = 4)
tab
```


<table>
<thead><tr><th></th><th scope=col>All</th><th scope=col>Men</th><th scope=col>Women</th></tr></thead>
<tbody>
	<tr><th scope=row>Log Wage</th><td> 3.0000223</td><td> 3.0384121</td><td> 2.9569035</td></tr>
	<tr><th scope=row>Sex</th><td> 0.4709909</td><td> 0.0000000</td><td> 1.0000000</td></tr>
	<tr><th scope=row>Less then High School</th><td> 0.0000000</td><td> 0.0000000</td><td> 0.0000000</td></tr>
	<tr><th scope=row>High School Graduate</th><td> 0.0000000</td><td> 0.0000000</td><td> 0.0000000</td></tr>
	<tr><th scope=row>Some College</th><td> 0.4667536</td><td> 0.4818238</td><td> 0.4498270</td></tr>
	<tr><th scope=row>Gollage Graduate</th><td> 0.5332464</td><td> 0.5181762</td><td> 0.5501730</td></tr>
	<tr><th scope=row>Advanced Degree</th><td> 0.0000000</td><td> 0.0000000</td><td> 0.0000000</td></tr>
	<tr><th scope=row>Northeast</th><td> 0.2659713</td><td> 0.2612446</td><td> 0.2712803</td></tr>
	<tr><th scope=row>Midwest</th><td> 0.2858540</td><td> 0.2908195</td><td> 0.2802768</td></tr>
	<tr><th scope=row>South</th><td> 0.2216428</td><td> 0.2285890</td><td> 0.2138408</td></tr>
	<tr><th scope=row>West</th><td> 0.2265319</td><td> 0.2193469</td><td> 0.2346021</td></tr>
	<tr><th scope=row>Experience</th><td>12.7009452</td><td>12.4331485</td><td>13.0017301</td></tr>
</tbody>
</table>



In particular, the table above shows that the difference in average *logwage* between men and women is equal to $0,081$


```R
mean(data_female$lwage)-mean(data_male$lwage)
```


-0.0815085550873591


Thus, the unconditional gender wage gap is about $3,8$\% for the group of never married workers (women get paid less on average in our sample). We also observe that never married working women are relatively more educated than working men and have lower working experience.

This unconditional (predictive) effect of gender equals the coefficient $\beta$ in the univariate ols regression of $Y$ on $D$:

\begin{align}
\log(Y) &=\beta D + \epsilon.
\end{align}

We verify this by running an ols regression in R.


```R
library(sandwich)
nocontrol.fit <- lm(lwage ~ sex, data=data)
nocontrol.est <- summary(nocontrol.fit)$coef["sex",1]
HCV.coefs <- vcovHC(nocontrol.fit, type = 'HC');
nocontrol.se <- sqrt(diag(HCV.coefs))[2] # Estimated std errors

# print unconditional effect of gender and the corresponding standard error
cat ("The estimated gender coefficient is",nocontrol.est," and the corresponding robust standard error is",nocontrol.se)
```

    The estimated gender coefficient is -0.08150856  and the corresponding robust standard error is 0.01957965

Note that the standard error is computed with the *R* package *sandwich* to be robust to heteroskedasticity. 


Next, we run an ols regression of $Y$ on $(D,W)$ to control for the effect of covariates summarized in $W$:

\begin{align}
\log(Y) &=\beta_1 D  + \beta_2' W + \epsilon.
\end{align}

Here, we are considering the flexible model from the previous lab. Hence, $W$ controls for experience, education, region, and occupation and industry indicators plus transformations and two-way interactions.

Let us run the ols regression with controls.


```R
# Ols regression with controls

flex <- lwage ~ sex + (exp1+exp2+exp3+exp4)*(shs+hsg+scl+clg+occ2+ind2+mw+so+we)

#   Note that ()*() operation in formula objects in R creates a formula of the sort:
#  (exp1+exp2+exp3+exp4)+ (shs+hsg+scl+clg+occ2+ind2+mw+so+we) +  (exp1+exp2+exp3+exp4)*(shs+hsg+scl+clg+occ2+ind2+mw+so+we)
#  This is not intuitive at all, but that's what it does.

control.fit <- lm(flex, data=data)
control.est <- summary(control.fit)$coef[2,1]

summary(control.fit)

cat("Coefficient for OLS with controls", control.est)

HCV.coefs <- vcovHC(control.fit, type = 'HC');
control.se <- sqrt(diag(HCV.coefs))[2] # Estimated std errors
```


    
    Call:
    lm(formula = flex, data = data)
    
    Residuals:
         Min       1Q   Median       3Q      Max 
    -1.87897 -0.27894 -0.00777  0.25823  2.85755 
    
    Coefficients: (16 not defined because of singularities)
                  Estimate Std. Error t value Pr(>|t|)    
    (Intercept)  3.6856233  0.5060297   7.283  4.2e-13 ***
    sex         -0.0530623  0.0193532  -2.742 0.006149 ** 
    exp1        -0.1840774  0.1961271  -0.939 0.348036    
    exp2         4.0888929  2.3488332   1.741 0.081824 .  
    exp3        -2.2064389  1.0068217  -2.191 0.028497 *  
    exp4         0.3378726  0.1370444   2.465 0.013744 *  
    shs                 NA         NA      NA       NA    
    hsg                 NA         NA      NA       NA    
    scl         -0.2498673  0.1237850  -2.019 0.043627 *  
    clg                 NA         NA      NA       NA    
    occ22        0.2151993  0.1582208   1.360 0.173900    
    occ23        0.0487642  0.2095297   0.233 0.815986    
    occ24        0.0281449  0.2300084   0.122 0.902619    
    occ25       -0.2711807  0.3944166  -0.688 0.491793    
    occ26       -0.2000530  0.2705614  -0.739 0.459725    
    occ27       -0.1203371  0.4188017  -0.287 0.773875    
    occ28       -0.1719401  0.2721490  -0.632 0.527577    
    occ29       -0.3963629  0.2050361  -1.933 0.053319 .  
    occ210       0.0919819  0.2432203   0.378 0.705323    
    occ211      -0.4994175  0.4368584  -1.143 0.253051    
    occ212       0.1901009  0.3411417   0.557 0.577401    
    occ213      -0.1945287  0.2718809  -0.715 0.474364    
    occ214       0.3010030  0.3808385   0.790 0.429378    
    occ215      -0.3369933  0.3356632  -1.004 0.315482    
    occ216      -0.0407369  0.1712462  -0.238 0.811987    
    occ217      -0.4552186  0.1586012  -2.870 0.004132 ** 
    occ218      -0.0100153  2.2144365  -0.005 0.996392    
    occ219       0.0020488  0.4191796   0.005 0.996101    
    occ220      -0.4223277  0.2607281  -1.620 0.105386    
    occ221      -0.9012886  0.2869692  -3.141 0.001703 ** 
    occ222      -0.0168748  0.4864599  -0.035 0.972330    
    ind23       -0.9374763  0.7630580  -1.229 0.219332    
    ind24        0.0473118  0.5593258   0.085 0.932596    
    ind25       -0.3770690  0.5232052  -0.721 0.471159    
    ind26       -0.5542517  0.5190253  -1.068 0.285670    
    ind27       -0.2812532  0.5714904  -0.492 0.622659    
    ind28       -0.6504243  0.5874717  -1.107 0.268319    
    ind29       -0.8045381  0.5094802  -1.579 0.114416    
    ind210      -0.4506545  0.5675561  -0.794 0.427246    
    ind211      -0.6634660  0.5259447  -1.261 0.207241    
    ind212      -0.6138007  0.5032946  -1.220 0.222731    
    ind213      -0.8964483  0.5817196  -1.541 0.123421    
    ind214      -0.3901374  0.4977512  -0.784 0.433223    
    ind215      -0.4653004  0.6882201  -0.676 0.499037    
    ind216      -0.5080079  0.5281966  -0.962 0.336243    
    ind217      -0.8686633  0.5294785  -1.641 0.100991    
    ind218      -0.6396953  0.5155592  -1.241 0.214790    
    ind219      -0.7415211  0.5552430  -1.335 0.181823    
    ind220      -0.8142791  0.5275884  -1.543 0.122846    
    ind221      -0.4997641  0.5348108  -0.934 0.350142    
    ind222      -0.3786290  0.5405464  -0.700 0.483700    
    mw           0.1958465  0.1068723   1.833 0.066978 .  
    so          -0.0346190  0.1042672  -0.332 0.739897    
    we           0.1261936  0.1184244   1.066 0.286693    
    exp1:shs            NA         NA      NA       NA    
    exp1:hsg            NA         NA      NA       NA    
    exp1:scl    -0.0121646  0.0407919  -0.298 0.765565    
    exp1:clg            NA         NA      NA       NA    
    exp1:occ22  -0.0631144  0.0630037  -1.002 0.316546    
    exp1:occ23   0.0326274  0.0794502   0.411 0.681349    
    exp1:occ24   0.0107059  0.0949665   0.113 0.910250    
    exp1:occ25  -0.0274672  0.2001848  -0.137 0.890875    
    exp1:occ26  -0.0527366  0.1119821  -0.471 0.637721    
    exp1:occ27  -0.1087102  0.1600695  -0.679 0.497102    
    exp1:occ28  -0.0371404  0.1035842  -0.359 0.719956    
    exp1:occ29   0.1021025  0.0830679   1.229 0.219119    
    exp1:occ210  0.0022818  0.0933261   0.024 0.980496    
    exp1:occ211  0.0369873  0.1571990   0.235 0.814001    
    exp1:occ212 -0.1062438  0.1222611  -0.869 0.384926    
    exp1:occ213  0.0483902  0.0983858   0.492 0.622870    
    exp1:occ214 -0.1209127  0.1397766  -0.865 0.387089    
    exp1:occ215  0.0107765  0.1230134   0.088 0.930198    
    exp1:occ216 -0.0377813  0.0639815  -0.591 0.554901    
    exp1:occ217  0.0473737  0.0588764   0.805 0.421101    
    exp1:occ218 -0.1554316  1.1024362  -0.141 0.887888    
    exp1:occ219 -0.0605324  0.1437029  -0.421 0.673617    
    exp1:occ220  0.0931849  0.0910362   1.024 0.306110    
    exp1:occ221  0.3231623  0.1010818   3.197 0.001404 ** 
    exp1:occ222 -0.1560741  0.1581812  -0.987 0.323884    
    exp1:ind23   0.4320231  0.3058459   1.413 0.157897    
    exp1:ind24   0.0409994  0.2080253   0.197 0.843772    
    exp1:ind25   0.1841740  0.2047239   0.900 0.368398    
    exp1:ind26   0.2255280  0.2011211   1.121 0.262232    
    exp1:ind27   0.1073133  0.2233358   0.481 0.630908    
    exp1:ind28   0.2545921  0.2458909   1.035 0.300577    
    exp1:ind29   0.2092253  0.1968917   1.063 0.288035    
    exp1:ind210  0.1807059  0.2171637   0.832 0.405412    
    exp1:ind211  0.2579344  0.2042452   1.263 0.206741    
    exp1:ind212  0.3170780  0.1967145   1.612 0.107102    
    exp1:ind213  0.3800928  0.2177404   1.746 0.080985 .  
    exp1:ind214  0.1408305  0.1946484   0.724 0.469425    
    exp1:ind215  0.1026476  0.3307499   0.310 0.756319    
    exp1:ind216  0.1427221  0.2064100   0.691 0.489340    
    exp1:ind217  0.2977947  0.2040966   1.459 0.144652    
    exp1:ind218  0.1962564  0.1997709   0.982 0.325983    
    exp1:ind219  0.1711574  0.2131201   0.803 0.421983    
    exp1:ind220  0.1746944  0.2031650   0.860 0.389936    
    exp1:ind221  0.2100177  0.2057559   1.021 0.307477    
    exp1:ind222  0.1893985  0.2053893   0.922 0.356532    
    exp1:mw     -0.0619563  0.0418241  -1.481 0.138623    
    exp1:so      0.0057820  0.0396763   0.146 0.884145    
    exp1:we     -0.0478640  0.0437059  -1.095 0.273548    
    exp2:shs            NA         NA      NA       NA    
    exp2:hsg            NA         NA      NA       NA    
    exp2:scl     0.2216086  0.4133059   0.536 0.591873    
    exp2:clg            NA         NA      NA       NA    
    exp2:occ22   0.2989342  0.7038148   0.425 0.671063    
    exp2:occ23  -0.7211942  0.8855311  -0.814 0.415473    
    exp2:occ24  -0.2699265  1.0959123  -0.246 0.805465    
    exp2:occ25   1.4532318  3.0067008   0.483 0.628898    
    exp2:occ26   0.3834942  1.3720465   0.280 0.779877    
    exp2:occ27   1.1812006  1.8784828   0.629 0.529527    
    exp2:occ28  -0.0274218  1.1533003  -0.024 0.981032    
    exp2:occ29  -1.0621384  0.9470416  -1.122 0.262156    
    exp2:occ210 -0.3264796  1.0432172  -0.313 0.754338    
    exp2:occ211 -0.3405652  1.7015462  -0.200 0.841377    
    exp2:occ212  0.6041155  1.3414334   0.450 0.652492    
    exp2:occ213 -0.9011013  1.0454393  -0.862 0.388796    
    exp2:occ214  0.1176365  1.5082483   0.078 0.937837    
    exp2:occ215 -0.5498030  1.3291914  -0.414 0.679171    
    exp2:occ216  0.0849304  0.6979720   0.122 0.903160    
    exp2:occ217 -0.7493648  0.6435325  -1.164 0.244337    
    exp2:occ218  0.7439583  9.3110051   0.080 0.936322    
    exp2:occ219  0.5498894  1.4906630   0.369 0.712238    
    exp2:occ220 -1.0158810  0.9425130  -1.078 0.281195    
    exp2:occ221 -3.9371723  1.0692967  -3.682 0.000236 ***
    exp2:occ222  1.5179725  1.5342157   0.989 0.322546    
    exp2:ind23  -6.4796151  3.7990841  -1.706 0.088197 .  
    exp2:ind24  -2.6872131  2.4441668  -1.099 0.271670    
    exp2:ind25  -4.1468398  2.4445725  -1.696 0.089930 .  
    exp2:ind26  -4.2139999  2.3991488  -1.756 0.079118 .  
    exp2:ind27  -2.7331923  2.6960937  -1.014 0.310784    
    exp2:ind28  -3.6656460  3.0702318  -1.194 0.232605    
    exp2:ind29  -3.8996457  2.3582733  -1.654 0.098319 .  
    exp2:ind210 -3.7035161  2.5382076  -1.459 0.144646    
    exp2:ind211 -4.5216510  2.4414956  -1.852 0.064130 .  
    exp2:ind212 -5.1083392  2.3679500  -2.157 0.031067 *  
    exp2:ind213 -5.6691510  2.5320131  -2.239 0.025234 *  
    exp2:ind214 -3.1313860  2.3469954  -1.334 0.182242    
    exp2:ind215 -2.6414528  3.7445752  -0.705 0.480614    
    exp2:ind216 -3.0267086  2.4664224  -1.227 0.219862    
    exp2:ind217 -4.7822893  2.4320783  -1.966 0.049357 *  
    exp2:ind218 -3.8782338  2.3922113  -1.621 0.105088    
    exp2:ind219 -3.3586261  2.5047964  -1.341 0.180067    
    exp2:ind220 -3.6271074  2.4173138  -1.500 0.133604    
    exp2:ind221 -4.0217328  2.4434433  -1.646 0.099889 .  
    exp2:ind222 -3.7684447  2.4233956  -1.555 0.120051    
    exp2:mw      0.4838242  0.4691702   1.031 0.302519    
    exp2:so     -0.0426958  0.4329768  -0.099 0.921455    
    exp2:we      0.5774804  0.4682555   1.233 0.217581    
    exp3:shs            NA         NA      NA       NA    
    exp3:hsg            NA         NA      NA       NA    
    exp3:scl    -0.1002865  0.1583125  -0.633 0.526477    
    exp3:clg            NA         NA      NA       NA    
    exp3:occ22   0.0005287  0.2849249   0.002 0.998519    
    exp3:occ23   0.3479651  0.3602479   0.966 0.334174    
    exp3:occ24   0.1327043  0.4490244   0.296 0.767604    
    exp3:occ25  -1.2675466  1.6239177  -0.781 0.435133    
    exp3:occ26  -0.0861625  0.6102063  -0.141 0.887720    
    exp3:occ27  -0.5391536  0.7984378  -0.675 0.499565    
    exp3:occ28   0.1250242  0.4640841   0.269 0.787642    
    exp3:occ29   0.3956094  0.3894184   1.016 0.309765    
    exp3:occ210  0.2356222  0.4270044   0.552 0.581127    
    exp3:occ211  0.0850896  0.6938821   0.123 0.902410    
    exp3:occ212  0.0109101  0.5433951   0.020 0.983983    
    exp3:occ213  0.4099807  0.4063159   1.009 0.313051    
    exp3:occ214  0.2328011  0.5737599   0.406 0.684959    
    exp3:occ215  0.3691372  0.5352416   0.690 0.490461    
    exp3:occ216  0.0915397  0.2798629   0.327 0.743626    
    exp3:occ217  0.3684352  0.2584120   1.426 0.154046    
    exp3:occ218 -0.0728607  1.8129821  -0.040 0.967946    
    exp3:occ219 -0.2037610  0.5768151  -0.353 0.723926    
    exp3:occ220  0.3824008  0.3642037   1.050 0.293824    
    exp3:occ221  1.6041311  0.4182354   3.835 0.000128 ***
    exp3:occ222 -0.5099737  0.5635594  -0.905 0.365587    
    exp3:ind23   3.2238995  1.7561719   1.836 0.066499 .  
    exp3:ind24   1.7349800  1.0365754   1.674 0.094288 .  
    exp3:ind25   2.2421191  1.0432430   2.149 0.031704 *  
    exp3:ind26   2.2146931  1.0241983   2.162 0.030673 *  
    exp3:ind27   1.5675521  1.1690776   1.341 0.180078    
    exp3:ind28   1.5399859  1.3940927   1.105 0.269404    
    exp3:ind29   2.0399792  1.0113099   2.017 0.043772 *  
    exp3:ind210  1.9816265  1.0709584   1.850 0.064370 .  
    exp3:ind211  2.3280002  1.0447922   2.228 0.025946 *  
    exp3:ind212  2.4986874  1.0171023   2.457 0.014083 *  
    exp3:ind213  2.6780049  1.0660293   2.512 0.012056 *  
    exp3:ind214  1.7526421  1.0095029   1.736 0.082647 .  
    exp3:ind215  1.5784535  1.4815769   1.065 0.286791    
    exp3:ind216  1.6946544  1.0516350   1.611 0.107193    
    exp3:ind217  2.3526755  1.0380306   2.266 0.023497 *  
    exp3:ind218  2.0716863  1.0267137   2.018 0.043708 *  
    exp3:ind219  1.8267916  1.0604717   1.723 0.085066 .  
    exp3:ind220  1.9671974  1.0307281   1.909 0.056421 .  
    exp3:ind221  2.0920770  1.0421031   2.008 0.044785 *  
    exp3:ind222  2.0075028  1.0304724   1.948 0.051497 .  
    exp3:mw     -0.1453989  0.1922868  -0.756 0.449618    
    exp3:so      0.0184796  0.1727892   0.107 0.914837    
    exp3:we     -0.2308636  0.1843977  -1.252 0.210678    
    exp4:shs            NA         NA      NA       NA    
    exp4:hsg            NA         NA      NA       NA    
    exp4:scl     0.0134666  0.0201340   0.669 0.503646    
    exp4:clg            NA         NA      NA       NA    
    exp4:occ22  -0.0133900  0.0376888  -0.355 0.722407    
    exp4:occ23  -0.0486518  0.0476989  -1.020 0.307826    
    exp4:occ24  -0.0223191  0.0593293  -0.376 0.706803    
    exp4:occ25   0.2845962  0.2824632   1.008 0.313756    
    exp4:occ26   0.0035336  0.0875725   0.040 0.967817    
    exp4:occ27   0.0789030  0.1085605   0.727 0.467402    
    exp4:occ28  -0.0258852  0.0605593  -0.427 0.669095    
    exp4:occ29  -0.0479087  0.0519869  -0.922 0.356840    
    exp4:occ210 -0.0411370  0.0572458  -0.719 0.472444    
    exp4:occ211 -0.0044897  0.0932319  -0.048 0.961595    
    exp4:occ212 -0.0327767  0.0723612  -0.453 0.650612    
    exp4:occ213 -0.0574088  0.0515849  -1.113 0.265846    
    exp4:occ214 -0.0524263  0.0705276  -0.743 0.457335    
    exp4:occ215 -0.0619990  0.0708724  -0.875 0.381758    
    exp4:occ216 -0.0264713  0.0367893  -0.720 0.471869    
    exp4:occ217 -0.0553914  0.0339714  -1.631 0.103100    
    exp4:occ218         NA         NA      NA       NA    
    exp4:occ219  0.0241359  0.0730760   0.330 0.741209    
    exp4:occ220 -0.0471960  0.0464443  -1.016 0.309628    
    exp4:occ221 -0.2092063  0.0539166  -3.880 0.000107 ***
    exp4:occ222  0.0540559  0.0691569   0.782 0.434490    
    exp4:ind23  -0.4970867  0.2682290  -1.853 0.063955 .  
    exp4:ind24  -0.2847302  0.1398614  -2.036 0.041863 *  
    exp4:ind25  -0.3402683  0.1415826  -2.403 0.016311 *  
    exp4:ind26  -0.3338771  0.1389338  -2.403 0.016319 *  
    exp4:ind27  -0.2444006  0.1615297  -1.513 0.130381    
    exp4:ind28  -0.1894363  0.2043155  -0.927 0.353914    
    exp4:ind29  -0.3070943  0.1377034  -2.230 0.025818 *  
    exp4:ind210 -0.3006797  0.1444260  -2.082 0.037441 *  
    exp4:ind211 -0.3499129  0.1421750  -2.461 0.013909 *  
    exp4:ind212 -0.3640899  0.1386132  -2.627 0.008669 ** 
    exp4:ind213 -0.3836270  0.1434293  -2.675 0.007523 ** 
    exp4:ind214 -0.2725083  0.1376981  -1.979 0.047909 *  
    exp4:ind215 -0.2549218  0.1891411  -1.348 0.177835    
    exp4:ind216 -0.2662393  0.1425528  -1.868 0.061913 .  
    exp4:ind217 -0.3434539  0.1408491  -2.438 0.014811 *  
    exp4:ind218 -0.3168784  0.1401819  -2.260 0.023867 *  
    exp4:ind219 -0.2815085  0.1433510  -1.964 0.049654 *  
    exp4:ind220 -0.3038212  0.1397946  -2.173 0.029837 *  
    exp4:ind221 -0.3142711  0.1414218  -2.222 0.026347 *  
    exp4:ind222 -0.3061402  0.1396051  -2.193 0.028395 *  
    exp4:mw      0.0142872  0.0258136   0.553 0.579980    
    exp4:so     -0.0037591  0.0225465  -0.167 0.867598    
    exp4:we      0.0282864  0.0238123   1.188 0.234976    
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    Residual standard error: 0.4635 on 2838 degrees of freedom
    Multiple R-squared:  0.3295,	Adjusted R-squared:  0.2754 
    F-statistic: 6.091 on 229 and 2838 DF,  p-value: < 2.2e-16
    


    Coefficient for OLS with controls -0.05306234

The estimated regression coefficient $\beta_1\approx-0.0696$ measures how our linear prediction of wage changes if we set the gender variable $D$ from 0 to 1, holding the controls $W$ fixed.
We can call this the *predictive effect* (PE), as it measures the impact of a variable on the prediction we make. Overall, we see that the unconditional wage gap of size $4$\% for women increases to about $7$\% after controlling for worker characteristics.  


Next, we are using the Frisch-Waugh-Lovell theorem from the lecture partialling-out the linear effect of the controls via ols.


```R
# Partialling-Out using ols

# models
flex.y <- lwage ~  (exp1+exp2+exp3+exp4)*(shs+hsg+scl+clg+occ2+ind2+mw+so+we) # model for Y
flex.d <- sex ~ (exp1+exp2+exp3+exp4)*(shs+hsg+scl+clg+occ2+ind2+mw+so+we) # model for D

# partialling-out the linear effect of W from Y
t.Y <- lm(flex.y, data=data)$res
# partialling-out the linear effect of W from D
t.D <- lm(flex.d, data=data)$res

# regression of Y on D after partialling-out the effect of W
partial.fit <- lm(t.Y~t.D)
partial.est <- summary(partial.fit)$coef[2,1]

cat("Coefficient for D via partialling-out", partial.est)

# standard error
HCV.coefs <- vcovHC(partial.fit, type = 'HC')
partial.se <- sqrt(diag(HCV.coefs))[2]

# confidence interval
confint(partial.fit)[2,]
```

    Coefficient for D via partialling-out -0.05306234


<dl class=dl-horizontal>
	<dt>2.5 %</dt>
		<dd>-0.0895706989969278</dd>
	<dt>97.5 %</dt>
		<dd>-0.0165539817185744</dd>
</dl>



## Graphics


```R
data_scl <- data[data$scl==1,]
data_clg <- data[data$clg==1,]
```


```R
library(dplyr)

Tabla_scl=data_scl%>% 
  group_by(exp1) %>% 
  summarise(Promlwageo = mean(lwage))

Tabla_clg=data_clg%>% 
  group_by(exp1) %>% 
  summarise(Promlwageo = mean(lwage))
```


```R
nivel_scl = c(unique(data_scl$exp1))
nivel_scl = sort(nivel_scl)
length(nivel_scl)
```


80



```R
Promedio=rep(0,length(unique(data_scl$exp1)))
length(Promedio)
```


80



```R
for (i in 1:80) {Promedio[i]= mean(data_scl$lwage[data_scl$exp1<=nivel_scl[i]])}
```


```R
Tabla_scl$PromMov=Promedio
Tabla_scl
```


<table>
<thead><tr><th scope=col>exp1</th><th scope=col>Promlwageo</th><th scope=col>PromMov</th></tr></thead>
<tbody>
	<tr><td> 3.0    </td><td>2.693883</td><td>2.693883</td></tr>
	<tr><td> 3.5    </td><td>2.729320</td><td>2.714895</td></tr>
	<tr><td> 4.0    </td><td>2.696418</td><td>2.709306</td></tr>
	<tr><td> 4.5    </td><td>2.611629</td><td>2.680130</td></tr>
	<tr><td> 5.0    </td><td>2.727195</td><td>2.688087</td></tr>
	<tr><td> 5.5    </td><td>2.667625</td><td>2.684759</td></tr>
	<tr><td> 6.0    </td><td>2.992093</td><td>2.704670</td></tr>
	<tr><td> 6.5    </td><td>2.742202</td><td>2.709705</td></tr>
	<tr><td> 7.0    </td><td>2.780971</td><td>2.714865</td></tr>
	<tr><td> 7.5    </td><td>2.725832</td><td>2.715878</td></tr>
	<tr><td> 8.0    </td><td>2.802120</td><td>2.720882</td></tr>
	<tr><td> 8.5    </td><td>2.754452</td><td>2.723293</td></tr>
	<tr><td> 9.0    </td><td>2.764071</td><td>2.725509</td></tr>
	<tr><td> 9.5    </td><td>2.798636</td><td>2.730159</td></tr>
	<tr><td>10.0    </td><td>2.945264</td><td>2.740573</td></tr>
	<tr><td>10.5    </td><td>2.752718</td><td>2.741167</td></tr>
	<tr><td>11.0    </td><td>2.810423</td><td>2.742820</td></tr>
	<tr><td>11.5    </td><td>2.715452</td><td>2.741892</td></tr>
	<tr><td>12.0    </td><td>2.859269</td><td>2.744233</td></tr>
	<tr><td>12.5    </td><td>2.752186</td><td>2.744606</td></tr>
	<tr><td>13.0    </td><td>3.016064</td><td>2.750661</td></tr>
	<tr><td>13.5    </td><td>2.976198</td><td>2.756381</td></tr>
	<tr><td>14.0    </td><td>2.906646</td><td>2.759752</td></tr>
	<tr><td>14.5    </td><td>2.845243</td><td>2.761434</td></tr>
	<tr><td>15.0    </td><td>3.236363</td><td>2.770069</td></tr>
	<tr><td>15.5    </td><td>2.862586</td><td>2.772326</td></tr>
	<tr><td>16.0    </td><td>2.675851</td><td>2.771268</td></tr>
	<tr><td>16.5    </td><td>2.952992</td><td>2.775738</td></tr>
	<tr><td>17.0    </td><td>3.448501</td><td>2.783561</td></tr>
	<tr><td>17.5    </td><td>2.854368</td><td>2.785596</td></tr>
	<tr><td>...</td><td>...</td><td>...</td></tr>
	<tr><td>28.0    </td><td>3.198975</td><td>2.823446</td></tr>
	<tr><td>28.5    </td><td>2.889095</td><td>2.824087</td></tr>
	<tr><td>29.0    </td><td>3.041796</td><td>2.826363</td></tr>
	<tr><td>29.5    </td><td>3.038627</td><td>2.828894</td></tr>
	<tr><td>30.0    </td><td>3.129417</td><td>2.831264</td></tr>
	<tr><td>30.5    </td><td>2.899830</td><td>2.832119</td></tr>
	<tr><td>31.0    </td><td>2.954635</td><td>2.832689</td></tr>
	<tr><td>31.5    </td><td>2.777762</td><td>2.832392</td></tr>
	<tr><td>32.0    </td><td>3.241180</td><td>2.835209</td></tr>
	<tr><td>32.5    </td><td>2.623908</td><td>2.833127</td></tr>
	<tr><td>33.0    </td><td>2.967186</td><td>2.834535</td></tr>
	<tr><td>33.5    </td><td>3.068406</td><td>2.836449</td></tr>
	<tr><td>34.0    </td><td>2.964679</td><td>2.837019</td></tr>
	<tr><td>34.5    </td><td>3.020900</td><td>2.838505</td></tr>
	<tr><td>35.0    </td><td>3.171709</td><td>2.840210</td></tr>
	<tr><td>35.5    </td><td>2.773304</td><td>2.839869</td></tr>
	<tr><td>36.0    </td><td>3.159085</td><td>2.840564</td></tr>
	<tr><td>36.5    </td><td>3.058889</td><td>2.841668</td></tr>
	<tr><td>37.0    </td><td>3.029137</td><td>2.842476</td></tr>
	<tr><td>37.5    </td><td>3.161802</td><td>2.843848</td></tr>
	<tr><td>38.0    </td><td>3.637984</td><td>2.846115</td></tr>
	<tr><td>38.5    </td><td>2.899289</td><td>2.846380</td></tr>
	<tr><td>39.0    </td><td>2.844940</td><td>2.846375</td></tr>
	<tr><td>39.5    </td><td>2.908733</td><td>2.846596</td></tr>
	<tr><td>40.0    </td><td>2.696443</td><td>2.846278</td></tr>
	<tr><td>40.5    </td><td>2.889598</td><td>2.846370</td></tr>
	<tr><td>41.0    </td><td>3.011219</td><td>2.846601</td></tr>
	<tr><td>41.5    </td><td>3.097123</td><td>2.847477</td></tr>
	<tr><td>42.0    </td><td>2.668829</td><td>2.847352</td></tr>
	<tr><td>42.5    </td><td>2.822980</td><td>2.847335</td></tr>
</tbody>
</table>



We repeat the procedure for "clg"


```R
nivel_clg = c(unique(data_clg$exp1))
nivel_clg = sort(nivel_clg)
length(nivel_clg)
```


40



```R
Promedio=rep(0,length(unique(data_clg$exp1)))
length(Promedio)
```


40



```R
for (i in 1:40) {Promedio[i]= mean(data_clg$lwage[data_clg$exp1<=nivel_clg[i]])}
Tabla_clg$PromMov=Promedio
Tabla_clg
```


<table>
<thead><tr><th scope=col>exp1</th><th scope=col>Promlwageo</th><th scope=col>PromMov</th></tr></thead>
<tbody>
	<tr><td> 1      </td><td>3.031143</td><td>3.031143</td></tr>
	<tr><td> 2      </td><td>3.019492</td><td>3.025765</td></tr>
	<tr><td> 3      </td><td>3.061553</td><td>3.036540</td></tr>
	<tr><td> 4      </td><td>3.070771</td><td>3.043327</td></tr>
	<tr><td> 5      </td><td>3.030900</td><td>3.041500</td></tr>
	<tr><td> 6      </td><td>3.182292</td><td>3.056320</td></tr>
	<tr><td> 7      </td><td>3.107772</td><td>3.061331</td></tr>
	<tr><td> 8      </td><td>3.142271</td><td>3.066631</td></tr>
	<tr><td> 9      </td><td>3.038090</td><td>3.064546</td></tr>
	<tr><td>10      </td><td>3.139449</td><td>3.069037</td></tr>
	<tr><td>11      </td><td>3.111374</td><td>3.070462</td></tr>
	<tr><td>12      </td><td>3.372184</td><td>3.078424</td></tr>
	<tr><td>13      </td><td>3.134240</td><td>3.080384</td></tr>
	<tr><td>14      </td><td>3.275004</td><td>3.086025</td></tr>
	<tr><td>15      </td><td>3.287349</td><td>3.091045</td></tr>
	<tr><td>16      </td><td>3.254997</td><td>3.093595</td></tr>
	<tr><td>17      </td><td>3.258694</td><td>3.097808</td></tr>
	<tr><td>18      </td><td>3.408159</td><td>3.103874</td></tr>
	<tr><td>19      </td><td>3.153315</td><td>3.104785</td></tr>
	<tr><td>20      </td><td>3.204437</td><td>3.106513</td></tr>
	<tr><td>21      </td><td>3.303849</td><td>3.111446</td></tr>
	<tr><td>22      </td><td>3.200675</td><td>3.112612</td></tr>
	<tr><td>23      </td><td>3.065550</td><td>3.112105</td></tr>
	<tr><td>24      </td><td>3.267125</td><td>3.113757</td></tr>
	<tr><td>25      </td><td>3.214664</td><td>3.115030</td></tr>
	<tr><td>26      </td><td>3.418911</td><td>3.119647</td></tr>
	<tr><td>27      </td><td>3.379309</td><td>3.123534</td></tr>
	<tr><td>28      </td><td>3.223364</td><td>3.124874</td></tr>
	<tr><td>29      </td><td>3.441726</td><td>3.129070</td></tr>
	<tr><td>30      </td><td>3.268815</td><td>3.130263</td></tr>
	<tr><td>31      </td><td>3.239399</td><td>3.131678</td></tr>
	<tr><td>32      </td><td>3.315334</td><td>3.132625</td></tr>
	<tr><td>33      </td><td>3.336597</td><td>3.134061</td></tr>
	<tr><td>34      </td><td>3.381862</td><td>3.136884</td></tr>
	<tr><td>35      </td><td>3.110984</td><td>3.136722</td></tr>
	<tr><td>36      </td><td>3.235879</td><td>3.137094</td></tr>
	<tr><td>37      </td><td>3.121215</td><td>3.136946</td></tr>
	<tr><td>38      </td><td>2.971469</td><td>3.135319</td></tr>
	<tr><td>39      </td><td>2.679251</td><td>3.134201</td></tr>
	<tr><td>40      </td><td>2.960661</td><td>3.133670</td></tr>
</tbody>
</table>




```R
#Figure 1
plot(Tabla_scl$exp1,Tabla_scl$PromMov, xlab = "Years of Potencial Experience", ylab="Log Wage(or Wage Gap)", main="Figure 1", xlim=c(0,43), xaxt='n',type = 'l')
grid(nx = NULL, ny = NULL, lty = 2, col = "gray", lwd = 1)
axis(side = 1, at=seq(0,43,by=5))
```


    
![png](output_36_0.png)
    



```R
#Figure 2
plot(Tabla_clg$exp1,Tabla_clg$PromMov, xlab = "Years of Potencial Experience", ylab="Log Wage(or Wage Gap)", main="Figure 2", xlim=c(0,40), xaxt='n',type = 'l')
grid(nx = NULL, ny = NULL, lty = 2, col = "gray", lwd = 1)
axis(side = 1, at=seq(0,40,by=5))
```


    
![png](output_37_0.png)
    



```R

```



