## Python environment and Jupyter

The following commands create a python environment
<code>conda create --name myenv python==3.10</code>
<code>conda activate myenv</code>
<code>conda install scikit-learn</code>

Opening jupyter notebooks
<code>conda install jupyter</code>
<code>cd dir</code>
<code>jupyter notebook</code>
Es mejor usar <code>start jupyter notebook</code>. No bloquea la terminal de anaconda, y puedes instalar paquetes con conda install en vez de pip desde jupyter.

If we're on our environment, running the following should output the environment path such as USER\anaconda3\envs\causalml\python.exe
<code>import sys</code>
<code>sys.executable</code> 

*Obs 1.* Instead of pip installing in Jupyter, it's better to Conda installing packages and then just running the import lines of the code in Jupyter. 
*Obs 2.* Jupyter may be running in your Conda environment but executing pip install lines can inherit things from the base environment. To see if this is the case run <code>!where pip</code>. If it shows something like C:\ProgramData\anaconda3\envs\causalml\Scripts\pip.exe then all is good. If it shows something like C:\ProgramData\anaconda3\Scripts\pip.exe then this problem is occurring. 

To make sure pip runs in the same environment execute pip install lines as follows (just replace pip with !{sys.executable} -m pip)
<code>import sys</code>
<code>!{sys.executable} -m pip install pandas numpy openpyxl statsmodels</code>


## R environment and Jupyter 

Install R, begin an R session just typing R. One can quit an R session by typing q()
<code>conda install -c conda-forge r-base</code>
<code>R</code>
<code>install.packages('IRkernel', repos = 'https://cloud.r-project.org')</code>
<code>IRkernel::installspec(user = FALSE)</code>
After this just re-open Jupyter notebooks, open an .R notebook and change the Kernel in the menu

*Obs 1.* Matrix package which is a dependency for glmnet is not available for some versions of R. It is available on r-base=4.3.3 

<code>conda remove r-base</code>
<code>conda install r-base=4.4</code>
<code>conda install -c conda-forge r-base=4.4</code>



<code>python def hello(): print("Hello, world!") </code>

 Possible errors
 1. install.packages("dplyr") installed the dependency install.packages("vctrs"). The version of this package required is higher than the one installed in conda by default. 
	 - Solution: Go to conda, open and R session and do remove.packages("vctrs") and then install.packages("vctrs", repos = "https://cloud.r-project.org")
2. Matrix package (glmnet dependency) requires R version >=4.4 (I installed version 4.4.3)

## Julia environment and Jupyter

**Not recommended to be run in an environment** 
Just download locally from https://julialang.org/downloads and install it system-wide
In the Julia terminal you then add the IKernrel to Jupyter
<code>using Pkg</code>
<code>Pkg.add("IJulia")</code>

GLM
I'm on version 1.10.2 and everything runs good x