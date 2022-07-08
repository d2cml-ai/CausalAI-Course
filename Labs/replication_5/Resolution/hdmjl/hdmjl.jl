# HDMJL
    ## 1. Preliminary Functions

        # Import relevant packages for splitting data
        using Distributed

        @everywhere using LinearAlgebra, GLM, DataFrames, Statistics, Random, Distributions, Tables, TableOperations, StatsBase, FreqTables, DataFrames

        # Define a function which turn a list or vector-like object into a proper two
        # dimensional column vector

        function cvec(a)
            """ Turn a list or vector-like object into a proper column vector
            Input
            a: List or vector-like object, has to be a potential input for np.array()
            Output
            vec: two dimensional NumPy array, with the first dimension weakly greater
                than the second (resulting in a column vector for a vector-like input)
            """
            
            # Conver input into a two dimensional NumPy array
            vec = cat([a], dims = 2) 

            # Check whether the second dimension is strictly greater than the first
            # (remembering Python's zero indexing)
            
            if size(vec)[1] < size(vec)[2]
                # If so, transpose the input vector
                vec = transpose(vec)
            end
        
            # Return the column vector
            return vec

        end

        import Statistics.cor
        function corre(y, X)
            
            """ Return correlation coefficients between columns of matrices
            Inputs
            y: n by 1 NumPy array
            X: n by k NumPy array
            Outputs
            corr: list of length k, where the k-th element is the correlation
                coefficient between y and the k-th column of X
            """
            # Concatenate y and X into a single NumPy array
            yX = hcat(y, X)
            
            # Get the correlation coefficients between all columns of that array
            corr = cor(yX)
            
            # Get the first row, starting at the first off-diagonal element (these are
            # the correlation coefficients between y and each column of X
            corr = corr[1, :] 
            
            # Return the result
            return corr

        end

        function init_values(X, y, number::Int64=5, intercetp::Bool=true)
            """ Return an initial parameter guess for a LASSO model
            Inputs
            y: n by 1 NumPy array, outcome variable
            X: n by k NumPy array, RHS variables
            Outputs
            residuals: n ny 1 NumPy array, residuals for initial parameter guess
            coefficients: k by 1 NumPy array, initial coefficient values
            """
            # Make sure y is a proper column vector
            #y = cvec(y)
            
            # Get the absolute value of correlations between y and X
            corr = broadcast(abs, cor(y, X)[1, :])
            
            # Get the number of columns of X
            kx = size(X)[2]
            
            # Make an index selecting the five columns of X which are most correlated
            # with y (since .argsort() always sorts in increasing order, selecting from
            # the back gets the most highly correlated columns)
            index = sortperm(corr, rev=true)[1: min(number, kx)]
            
            # Set up an array of coefficient guesses
            coefficients = zeros(kx)
            
            # Regress y on the five most correlated columns of X, including an intercept
            # if desired
        reg = lm(X[:, index], y)
            
            # Replace the guesses for the estimated coefficients (note that .coef_ does
            # not return the estimated intercept, if one was included in the model)
            
            coefficients[index] = GLM.coef(reg)
            
            # Replace any NANs as zeros
            replace!(coefficients, NaN=>0)
            
            # Get the regression residuals
            residuals = y - predict(reg, X[:, index])
            
            return residuals, reg, index, coefficients, corr
            #return index
            
        end

    ## 2. LassoShooting 

        # function LassoShooting_fit( x, y, lmbda, control::control, 
        #                             XX = nothing, Xy = nothing, beta_start = nothing)

        function LassoShooting_fit( ;x, y, lmbda, maxIter::Int = 1000, 
            optTol::Float64 = 10^(-5), 
            zeroThreshold::Float64 = 10^(-6),
            XX = nothing, Xy = nothing, beta_start = nothing)

        """ Shooting LASSO algorithm with variable dependent penalty weights
        Inputs
        x: n by p NumPy array, RHS variables
        y: n by 1 NumPy array, outcome variable
        lmbda: p by 1 NumPy array, variable dependent penalty terms. The j-th
        element is the penalty term for the j-th RHS variable.
        maxIter: integer, maximum number of shooting LASSO updated
        optTol: scalar, algorithm terminated once the sum of absolute differences
        between the updated and current weights is below optTol
        zeroThreshold: scalar, if any final weights are below zeroThreshold, they
        will be set to zero instead
        XX: k by k NumPy array, pre-calculated version of x'x
        Xy: k by 1 NumPy array, pre-calculated version of x'y
        beta_start: k by 1 NumPy array, initial weights
        Outputs
        w: k by 1 NumPy array, final weights
        wp: k by m + 1 NumPy array, where m is the number of iterations the
        algorithm took. History of weight updates, starting with the initial
        weights.
        m: integer, number of iterations the algorithm took
        """
        n = size(x)[1]
        p = size(x)[2]

        # Check whether XX and Xy were provided, calculate them if not
        if (isnothing(XX))
        XX = x'*x
        end

        if (isnothing(Xy))
        Xy = x'*y
        end

        # Check whether an initial value for the intercept was provided

        if (isnothing(beta_start))
        # If not, use init_values from help_functions, which will return
        # regression estimates for the five variables in x which are most
        # correlated with y, and initialize all other coefficients as zero
        beta = init_values(x, y)[4]

        else
        # Otherwise, use the provided initial weights
        beta = beta_start
        end

        # Set up a history of weights over time, starting with the initial ones
        wp = beta

        # Keep track of the number of iterations
        m = 1

        # Create versions of XX and Xy which are just those matrices times two
        XX2 = XX * 2
        Xy2 = Xy * 2

        #@unpack maxIter, optTol, zeroThreshold = control()

        # Go through all iteration
        while m<maxIter

        # Save the last set of weights (the .copy() is important, otherwise
        # beta_old will be updated every time beta is changed during the
        # following loop)
        beta_old = copy(beta)

        # Go through all parameters
        for j in 1:p

        # Calculate the shoot
        S0 = sum( XX2[j, :].*beta ) - XX2[j, j].*beta[j] - Xy2[j]

        # Update the weights
        if sum(isnothing(XX)) >= 1
        beta[j] = 0

        elseif S0 >lmbda[j]
        beta[j] = (lmbda[j] - S0) / XX2[j,j]

        elseif S0 < -lmbda[j]
        beta[j] = (-lmbda[j] - S0) / XX2[j,j]

        elseif broadcast(abs, S0) <= lmbda[j]
        beta[j] = 0

        end
        end

        # Add the updated weights to the history of weights
        wp = hcat(wp, beta)

        # Check whether the weights are within tolerance
        if sum(broadcast(abs, beta - beta_old)) < optTol
        # If so, break the while loop
        break
        end

        # Increase the iteration counter
        m = m + 1
        end

        # Set the final weights to the last updated weights
        w = beta   

        # Set weights which are within zeroThreshold to zero
        w[broadcast(abs, w) .< zeroThreshold] .= 0

        #return beta,  w
        return Dict("coefficients" => w, "coef_list" => wp, "num_it" => m)
        #return w, wp, m
        #return XX2, Xy2
        end

    ## 3.1 lambdaCalculation 

        function lambdaCalculation(     ; homoskedastic::Bool=false, X_dependent_lambda::Bool=false,
            lambda_start=nothing, c::Float64=1.1, gamma::Float64=0.1, 
            numSim::Int=5000, y=nothing, x=nothing, par::Bool=true, 
            corecap::Float64=Inf, fix_seed::Bool=true)
        # Get number of observations n and number of variables p
        n, p = size(x)

        # Get number of simulations to use (if simulations are necessary)
        R = numSim

        # Go through all possible combinations of homoskedasticy/heteroskedasticity
        # and X-dependent or independent error terms. The first two cases are
        # special cases: Handling the case there homoskedastic was set to None, and
        # where lambda_start was provided.
        #

        # 1) If homoskedastic was set to None (special case)
        if (isnothing(homoskedastic))

        # Initialize lambda
        lmbda0 = lambda_start

        Ups0 = (1 /sqrt(n)) * sqrt.((y.^2)'*(x.^2))

        # Calculate the final vector of penalty terms
        lmbda = lmbda0 * Ups0

        # 2) If lambda_start was provided (special case)
        elseif (isnothing(lambda_start)) == 0

        # Check whether a homogeneous penalty term was provided (a scalar)
        if maximum(size(lambda_start)) == 1
        # If so, repeat that p times as the penalty term
        lmbda = ones(p,1).*lambda_start

        else
        # Otherwise, use the provided vector of penalty terms as is
        lmbda = lambda_start
        end

        # 3) Homoskedastic and X-independent
        elseif homoskedastic == true &&  X_dependent_lambda == false

        # Initilaize lambda
        lmbda0 = 2 * c * sqrt(n) * quantile(Normal(0.0, 1.0),1 - gamma/(2*p))

        # Use ddof=1(corrected = true in Julia) to be consistent with R's var() function (in Julia by defaul the DDF is N-1)
        Ups0 = sqrt(var(y, corrected = true))

        # Calculate the final vector of penalty terms
        lmbda = zeros(p,1) .+ lmbda0 * Ups0

        # 4) Homoskedastic and X-dependent
        elseif homoskedastic == true && X_dependent_lambda == true

        psi = mean.(eachcol(x.^2))
        tXtpsi = (x' ./ sqrt(psi))'

        R = 5000
        sim = zeros(R,1)

        for l in 1:R
        g = reshape(repeat(randn(n), inner = p),(p, n))'
        sim[l] = n * maximum(2*abs.(mean.(eachcol(tXtpsi.* g))))
        end

        # Initialize lambda based on the simulated quantiles
        lmbda0 = c*quantile(vec(sim), 1 - gamma)

        Ups0 = sqrt(var(y, corrected = true))

        # Calculate the final vector of penalty terms
        lmbda = zeros(p,1) .+ lmbda0 * Ups0

        # 5) Heteroskedastic and X-independent
        elseif homoskedastic == false &&  X_dependent_lambda == false

        # The original includes the comment, "1=num endogenous variables"
        lmbda0 = 2 * c * sqrt(n) * quantile(Normal(0.0, 1.0),1 - gamma/(2*p*1))

        Ups0 = (1 /sqrt(n)) * sqrt.((y.^2)'*(x.^2))'

        lmbda = lmbda0 * Ups0

        # 6) Heteroskedastic and X-dependent
        elseif homoskedastic == false &&  X_dependent_lambda == true

        eh = y
        ehat = reshape(repeat(eh, inner = p),(p, n))'

        xehat = x.*ehat
        psi = mean.(eachcol(xehat.^2))'
        tXehattpsi = (xehat./sqrt.(psi))

        R = 5000
        sim = zeros(R,1)

        for l in 1:R
        g = reshape(repeat(randn(n), inner = p),(p, n))'
        sim[l] = n * maximum(2*abs.(mean.(eachcol(tXtpsi.* g))))
        end

        # Initialize lambda based on the simulated quantiles
        lmbda0 = c*quantile(vec(sim), 1 - gamma)

        Ups0 = (1 /sqrt(n)) * sqrt.((y.^2)'*(x.^2))

        lmbda = lmbda0 * Ups0

        end
        return Dict("lambda0" => lmbda0, "lambda" => lmbda, "Ups0" => Ups0) 

        end


    ## 3.2 rlasso
        @everywhere mutable struct rlasso_arg
            x::DataFrame
            y::DataFrame
            colnames::Nothing
            #rlasso_arg_v2(colnames=nothing) = new(colnames)
            post::Bool
            intercept::Bool
            model::Bool
            homoskedastic::Bool
            X_dependent_lambda::Bool
            lambda_start::Nothing
            #rlasso_arg_v2(lambda_start=nothing) = new(lambda_start)
            c::Float64
            gamma::Nothing
            #rlasso_arg_v2(lambda_start=nothing) = new(gamma)
            numSim::Int
            numIter::Int
            tol::Float64 
            threshold::Float64
            par::Bool
            corecap::Float64
            fix_seed::Bool
        end


        # function rlasso(self::rlasso_arg_4)
        #     return self.x
        # end 


        @everywhere function rlasso(self::rlasso_arg)
            
            # Import relevant packages for splitting data
            #using LinearAlgebra, GLM, DataFrames, Statistics, Random, Distributions, Tables, TableOperations, StatsBase, FreqTables, DataFrames
            
            # Initialize internal variables
            if self.x isa DataFrame && isnothing(self.colnames)
                colnames = names(self.x)
                
            end
            
            x = Matrix(self.x)
            y = vec(Matrix(self.y))
            
            n = size(x)[1]
            p = size(x)[2]
            
            if self.x isa DataFrame ==0 && isnothing(self.colnames)
                V = []
                        
                for i in 1:p
                    a = "V" * string(i)
                    V = append!(V, [a])
                end
                
                colnames  = V
            else
                colnames = colnames
                
            end
            
            # Unused line in the original code
            # ind_names = np.arange(self.p) + 1
            
            post               = self.post
            intercept          = self.intercept
            model              = self.model
            homoskedastic      = self.homoskedastic
            X_dependent_lambda = self.X_dependent_lambda
            lambda_start       = self.lambda_start
            c                  = self.c

            if isnothing(self.gamma)
                gamma = .1 / log(n)
            
            else
                gamma = self.gamma
            end
            
            numSim    = self.numSim
            numIter   = self.numIter
            tol       = self.tol
            threshold = self.threshold

            par       = self.par
            corecap   = self.corecap
            fix_seed  = self.fix_seed
            
            if self.post == false && isnothing(self.c)
                c = 0.5
            end
            
            if ( (self.post == false) && (self.homoskedastic == false)
                    && (self.X_dependent_lambda == false)
                    && (isnothing(self.lambda_start)) 
                    && (self.c == 1.1)
                    && (self.gamma == 0.1 / log(n)) )
                
                c = .5
            end
            
            # For now, instantiate estimate as None
            est = nothing
            
            
            # Calculate robust LASSO coefficients
            if self.intercept == true
                meanx = mean.(eachcol(x))
                x = x - ones(n, 1) * mean.(eachcol(x))'
                mu = mean(y)
                y = y .- mu
                
            else
                meanx = zeros(p, 1)
                mu = 0
            end
            
            normx = sqrt.(var(x, corrected = true, dims = 2))
            Psi = mean.(eachcol(x.^2))
            ind = zeros(Bool, p)
            
            XX = x'*x
            Xy = x'*y
            
            startingval = init_values(x, y)[1]
            
            pen = lambdaCalculation(;homoskedastic=homoskedastic,
                                        X_dependent_lambda=X_dependent_lambda,
                                        lambda_start=lambda_start, c=c,
                                        gamma=gamma, numSim=numSim,
                                        y=startingval, x=x, par=par,
                                        corecap=corecap, fix_seed=fix_seed)

            lmbda = vec(pen["lambda"])
            lmbda_half = lmbda/2
            Ups0 = vec(pen["Ups0"])
            Ups1 = vec(pen["Ups0"])
            lmbda0 = pen["lambda0"]
            
            mm = 1
            s0 = sqrt.(var(y, corrected = true, dims = 1))
            
            while mm <= numIter
                if mm == 1 && self.post
        #             coefTemp = LassoShooting_fit(x, y, lmbda/2, XX=XX,
        #                                       Xy=Xy)["coefficients"]
                    
                    global coefTemp = LassoShooting_fit(  ;x=x, y=y, 
                                        lmbda=lmbda_half, 
                                        maxIter = 1000, 
                                        optTol = 10^(-5), 
                                        zeroThreshold = 10^(-6),
                                        XX = XX, 
                                        Xy = Xy, 
                                        beta_start = nothing)["coefficients"]
                else
                    global coefTemp = LassoShooting_fit(  ;x=x, y=y, 
                                        lmbda=lmbda, 
                                        maxIter = 1000, 
                                        optTol = 10^(-5), 
                                        zeroThreshold = 10^(-6),
                                        XX = XX, 
                                        Xy = Xy, 
                                        beta_start = nothing)["coefficients"]
                        
                end
                
                global coefTemp[isnan.(coefTemp)] .= 0
                    
                global ind1 =  broadcast(abs, coefTemp) .> 0
                
                global x1 = x[:, ind1]
                
                if size(x1)[2] == 0
                    if intercept
                        intercept_value = mean(y .+ mu)
                        
                        coefs = vec(zeros(p+1, 1))
                        global coefs = DataFrame([ append!(["Intercept"], colnames), coefs ], :auto)
                        #coefs = DataFrame([ append!(["Intercept"], colnames)], [coefs] , :auto)
                        #coef = 
                    
                    else
                        intercept_value = mean(y)
                        
                        coefs = vec(zeros(p, 1))
                        
                        coefs = DataFrame([ colnames, coefs ], :auto)
                    end
                    
                    
                    global est = Dict("coefficients"=> coefs,
                            "beta"=> zeros(p, 1),
                            "intercept"=> intercept_value,
                            "index"=> DataFrame([ colnames, zeros(Bool, p) ], :auto),
                            "lambda"=> lmbda,
                            "lambda0"=> lmbda0,
                            "loadings"=> Ups0,
                            "residuals"=> y .- mean(y),
                            "sigma"=> var(y, corrected = true, dims = 1),
                            "iter"=> mm,
                            #"call"=> Not a Python option
                            "options"=> Dict("post"=> post, "intercept"=> intercept,
                                        "ind.scale"=> ind, "mu"=> mu, "meanx"=> meanx)
                        )
                        
                    if self.model
                            est["model"] = x
                    else
                        est["model"] = nothing
                    
                    end 
                    
                    est["tss"] = sum((y .- mean(y)).^2)
                    est["rss"] = sum((y .- mean(y)).^2)
                    est["dev"] = y .- mean(y)
                
                end 
                
                # Refinement variance estimation
                if size(x1)[2] != 0 && self.post
                    
                    reg = lm(x1, y)
                    
                    coefT = coef(reg)
                    
                    coefT[isnan.(coefT)] .= 0
                    
                    global e1 = y - x1*coefT
                    
                    coefTemp[ind1] = coefT
                    
                else
                    global e1 = y - x1*coefTemp[ind1]
                    
                end
                
                s1 = sqrt.(var(e1, corrected = true, dims = 1))
                #s5 = sqrt.(var(y, corrected = true, dims = 1))
                
                        
                # Homoskedastic and X-independent
                if (
                            (self.homoskedastic == true) 
                            && (self.X_dependent_lambda == false)
                    )
                    
                    Ups1 = s1 * Psi
                    lmbda = pen["lambda0"] * Ups1
                    
                # Homoskedastic and X-dependent
                elseif (
                            (self.homoskedastic == true)
                            && (self.X_dependent_lambda == true)
                    )

                    Ups1 = s1 * Psi

                    lmbda = pen["lambda0"] * Ups1

                # Heteroskedastic and X-independent
                elseif (
                        (self.homoskedastic == false)
                        && (self.X_dependent_lambda == false)
                    )
                                
                    Ups1 =  (1/sqrt(n)) * sqrt.((e1.^2)' * x.^2)
                    
                    lmbda = pen["lambda0"] * Ups1
                
                # Heteroskedastic and X-dependent
                elseif (
                        (self.homoskedastic == false)
                        && (self.X_dependent_lambda == true)
                        )
                    
                    lc = lambdaCalculation(homoskedastic=homoskedastic,
                            X_dependent_lambda=X_dependent_lambda,
                            lambda_start=lambda_start,
                            c=c, gamma=gamma,
                            numSim=numSim, y=e1, x=x,
                            par=par, corecap=corecap,
                            fix_seed=fix_seed)

                    Ups1 = lc["Ups0"]

                    lmbda = lc["lambda"]
                
                # If homoskedastic is set to None
                elseif isnothing(self.homoskedastic)
                    
                    Ups1 =  (
                            (1/sqrt(n)) * sqrt.((e1.^2) * x.^2)
                        )
                    
                    lmbda = pen["lambda0"] * Ups1
                end
                
                mm = mm + 1
                
                if broadcast(abs, s0 - s1)[1] < self.tol
                    break
                    
                end
                
                s0 = s1
                
            end
            
            if size(x1)[2] == 0
                #coefTemp = nothing 
                ind1 = vec(zeros(p, 1))
            end
            
            global coefTemp = coefTemp
            
            coefTemp[broadcast(abs, coefTemp) .< threshold] .= 0
            
            coefTemp_df = DataFrame([ colnames, coefTemp ], :auto)

            global ind1 = ind1
            
            ind1_df = DataFrame([ colnames, ind1 ], :auto)
            
            if self.intercept
                
                if isnothing(mu)
                    mu = 0
                end
                
                if isnothing(meanx)
                    meanx = zeros( size(coefTemp)[1], 1)
                end
                
                if sum(ind) == 0
                    intercept_value = mu - sum(meanx .* coefTemp)
                else
                    intercept_value = mu - sum(meanx .* coefTemp)
                end
            
            else
                intercept_value = NaN
            end
            
            #s1 = sqrt.(var(e1, corrected = true, dims = 1))
            
            if self.intercept
                beta = vcat(intercept_value, coefTemp)
                
                beta = DataFrame([ append!(["Intercept"], colnames), beta ], :auto)
            
            else
                beta = coefTemp
                
            end
            
            s1 = sqrt.(var(e1, corrected = true, dims = 1))
            
            
            est = Dict(
            "coefficients"=> beta,
            "beta"=> DataFrame([ colnames, coefTemp ], :auto), 
            "intercept"=> intercept_value,
            "index"=> ind1,
            "lambda"=> DataFrame([ colnames, vec(lmbda) ], :auto),
            "lambda0"=> lmbda0,
            "loadings"=> Ups1,
            "residuals"=> e1,
            "sigma"=> s1,
            "iter"=> mm,
            #"call"=> Not a Python option
            "options"=> Dict("post"=> self.post, "intercept"=> self.intercept,
                        "ind.scale"=> ind, "mu"=> mu, "meanx"=> meanx),
            "model"=> model
            )
            
            if model
                x = x + ones(n, 1) * mean.(eachcol(x))'
                
                est["model"] = x
                
            else
                est["model"] = nothing
                
            end
            
            est["tss"] = sum((y .- mean(y)).^2)
            est["rss"] = sum((y .- mean(y)).^2)
            est["dev"] = y .- mean(y)
            est["Xy"] = Xy
            est["startingval"] = startingval
            est["pen"] = pen
            est["x1"] = x1
            
        return est
        #return Dict("reg" => reg)
        #return coefTemp
        #return colnames, coefTemp, lmbda
                
        end