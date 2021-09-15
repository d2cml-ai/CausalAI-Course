1.1. INTRODUCTION 

In this chapter we will discuss three key notions: (i) potential outcomes, (ii) multiple unity and the usefulness of the stability assumption and (iii) the role of the allocation mechanism. 

1.2. POTENTIAL OUTCOMES
Causality is linked to an action (or manipulation, treatment or intervention), applied to a unit. Now, what is a unit? A unit can be a physical object, a firm, an individual person, or a collection of objects or persons, such as a classroom or a market, at a given time. 

A causal statement presupposes that a unit can be a physical object, a company, an individual person, or a set of objects or persons, such as a classroom or a marketplace, at a given time. The potential outcome, therefore, is the result of a unit after a set of actions. Any treatment must occur temporally before the observation of any associated potential outcome is possible.


1.3. CAUSAL EFFECTS 
In the example that a person is with a headache and must decide whether or not to take aspirin, there are two potential outcomes. The first is when he takes the aspirin and the second is when he does not, one for each level of treatment. The causal effect of treatment
involves the comparison of these two potential outcomes.

There are two important aspects to this definition of causal effect. (i) The definition of causal effect depends on the potential outcomes, but does not depend on what outcome is actually observed. Specifically, whether I take an aspirin (and thus cannot observe the state of my headache without aspirin) or do not take an aspirin (and thus cannot observe the outcome with an aspirin) does not affect the definition of the causal effect. (ii) Causal effect is the comparison of potential outcomes, for the same unit, at the same time post-treatment. In particular, causal effect is not defined in terms of comparisons of outcomes at different times, as in a comparison of before and after my headache before and after deciding to take or not to take aspirin. "The fundamental problem of causal inference."



1.4. CAUSAL EFFECTS IN COMMON USE. 
The purpose of this section is to clarify the way in which we use the definition of causal effect in everyday life. The author makes an example of the concept with the movie "It's a Wonderful Life", where the main character can appreciate the changes in the lives of others if he had not existed. This is called a causal effect in a world in which he would not have existed. 

1.5. LEARNING ABOUT CAUSAL EFFECTS: MULTIPLE UNITS 
Although the definition of causal effects does not require more than one unit, learning causal effects usually requires multiple units. Multiple units, some exposed to the active treatment, some exposed to the alternative (control) treatment, must be observed in order to make causal inferences. 
 
(i) One option is to observe the same physical object under different levels of treatment at different times. For example, in the case of aspirin, you can form your view according to multiple unit comparisons: myself at different times, taking and not taking aspirin.

(ii) Another way to evaluate is to observe different physical objects at approximately the same time. For example, if you and I (who are different units at the same time) are having a headache (assuming they are similar and for the same causes), I decide to take aspirin and you do not. Thus we will observe the efficiency of the aspirin. 

Now the problem is that we are assuming that the fact that you do not take the pills will not affect my improvement. Since it may happen that because you did not take your pill, you will feel overwhelmed and with many complaints, which may delay my improvement after taking the pill. 

1.6. THE STABLE UNIT TREATMENT VALUE ASSUMPTION
The stable unit treatment value assumption, or SUTVA, incorporates this idea that units do not interfere with each other as the concept that for each unit there is only a single version of each level of treatment.

Something that is defined earlier is what is exclusion restriction, which is called the assumption that relies on external information to rule out the existence of a causal effect of a particular treatment relative to the alternative. 



Assumption 1.1 (SUTVA).
"The potential outcomes of any unit do not vary with the treatments assigned to other units and, for each unit, there are no different forms or versions of each level of treatment, leading to different potential outcomes." Basically what is meant by this assumption is that the treatment applied to an entity or unit only affects itself and not anyone else. 
Components: 
No interference: the assumption that the treatment applied to one unit does not affect the outcome of other units. However, this component or may still be controversial for the study of some social policies. For example, in the case of applying treatment to one child, it is very likely that it may have effects on his or her peer, who did not receive treatment. In these cases, what is often done is to define the unit as the communicated unit within which individuals interact or to specifically limit the number of units assigned to a particular treatment. 
There are no hidden variations of treatments: This means that an individual receiving a specific level of treatment cannot receive different forms of that treatment. In the example of aspirin, the requirement is that the label on the aspirin tablet cannot alter the potential outcome of any unit. One strategy to make the SUTVA more plausible is based on redefining the treatment levels represented to comprise a broader set of treatments, e.g., Aspirin - , Aspirin + and non-aspirin instead of just Aspirin and non-aspirin.

1.6.3. Alternatives to SUTVA

SUTVA is only a candidate exclusion constraint for modeling potentially complex interactions between units and the entire set of treatment levels in a particular experiment. However, in many contexts, it appears that SUTVA is the primary choice.

1.7 THE ASSIGNMENT MECHANISM: AN INTRODUCTION

Now You and I are faced with only two treatment levels (e.g., for "You" whether or not you take an aspirin), and the potential outcomes that accompany them are a function of only our individual actions.

Yi = Yi( Wi) = Yi(0) if Wi=0 , Yi(1) if Wi=1
the assignment mechanism, plays a key role. How do we determine which units receive which treatments or, equivalently, which potential outcomes are realized and which are not?

1.8 ATTRIBUTES, PRETREATMENT VARIABLES OR COVARIATES

That is why, often, the presence of unit-specific background attributes, also called pretreatment variables, or covariates, and denoted in this text by the row vector Xi of K components for unit i, can help in making these predictions. In the aspirin example, a pretreatment variable may be headache intensity. The key feature of these covariates is that they are known a priori to be unaffected by treatment assignment. This knowledge usually comes from the fact that they are permanent characteristics of the units.  The information available on these covariates can be used in three ways: 
Covariates often serve to make estimates more precise by explaining some of the variation in the results.
The researcher may be interested in the typical causal effect (e.g., average) of the treatment on subgroups (defined by a covariate) in the population of interest.
The its effect on the allocation mechanism. Unemployed youth may be more interested in training programs aimed at acquiring new skills, or high-risk groups may be more likely to be vaccinated against influenza.

Important: Assumptions about the allocation mechanism and its possible freedom from dependence on potential outcomes are often more plausible within subpopulations that are homogeneous with respect to some covariates, i.e., conditionally given the covariates, rather than unconditionally.



1.9 POTENTIAL RESULTS AND LORD'S PARADOX

Lord did a study on the effects of college dining hall diets on students differentiated by sex. The causal estimate is the difference between the causal effects for males and females, the "differential" causal effect.  He analyzed the data with two statistics. Statistic 1 observes that there is no difference between the September and June weight distributions for either men or women.The second statistic, where he used a technique known as covariance adjustment or regression adjustment, concluded that after "controlling" for initial weight, the diet has a differential positive effect on men relative to women because for men and women with the same initial weight, on average men gain more than women. [...]  For causal inference, both are wrong because these data cannot support any conclusion about the causal effect of diet without making some very strong, and possibly implausible, assumptions. So, by complicating the problem with the introduction of the covariates "male/female" and "initial weight," Lord has created partial confusion. But the point here is that the "paradox" is immediately resolved by explicit use of potential outcomes.

