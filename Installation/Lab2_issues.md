# Installation problems during the second lab

- [1. GitHub is not downloading the files from the repository](#case_1)
- [2. Installing <code>pyread</code> in Python](#case_2)
- [3. Loading Rdata file in R](#case_3)
- [4. Additional recommendations](#additional)

<br />

## <a name="case_1"></a> **1. GitHub is not downloading the files**
It is important to remember to click on "Fetch origin" everytime we start using the "ECO224" file in order to refresh the new files.
Another reason GitHub is not updating the documents could be that it is hosted on the cloud like OneDrive, Google Drive, Dropbox.

> **_RECOMMENDATION:_** 
> 1. Install GitHub Desktop in another file different from the cloud. It usually is "Documents".
> 2. If you already have GitHub Desktop installed in a folder linked to the cloud, we recommend that you reinstall it in a non-linked folder.

<br />

## <a name="case_2"></a> **2. Installing <code>pyread</code> in Python**
Some of us had problems installing <code>pyread</code> while using the *new* environment we've created to run R and Python (which we named "Rtutorial" as the installation guide). In this case, we recommend to run Python in the base-root environment (the default environment in Anaconda), and install such package (<code>pyread</code>) in Jupyter Notebook by running:

```python
pip install pyread
```

You can start Python in the base-root environment by following these steps:

1. Open Anaconda Navigator and click on "base (root)"

<img src="navigator.png">

2. Enter to Jupyter Notebook by clicking "Launch".

<img src="j_launch.png">

3. Open a new notebook and install <code>pyread</code>. After that, you might be able to import such a package.

> **_RECOMMENDATION:_** 
> 1. Run Python in the base-root environment (default), and R, in the *new* environment we've created. In that sense, we recommend you run Python and R in different environments if you're facing problems.

<br />

## <a name="case_3"></a> **3. Loading Rdata file in R**

We had some problems loading Rdata (a data format designed for R) using <code>load</code> function from the package <code>readr</code>. We first recommend you install the package <code>readr</code> by typing:

```R
install.packages("readr")
```

If you still have problems, we suggest to remove the package and reinstall it by:

```R
remove.packages("readr")
install.packages("readr")
```

Finally, if the problem persists, we found the best option to run R in the Jupyter Notebook. It consists in installing R separately from Anaconda and using an [IRKernel](https://irkernel.github.io/installation/#windows-panel), which makes the kernel available to Jupyter Notebook. It can be done by following the steps presented in the [installation guide](https://github.com/alexanderquispe/ECO224/blob/main/Installation/Python_R_installation.md#ikernel) of this course.

 > **_NOTE:_** 
The steps in the [installation guide](https://github.com/alexanderquispe/ECO224/blob/main/Installation/Python_R_installation.md#ikernel) require to have R installed.

<br />

## <a name="additional"></a> **4. Additional recommendations**
So far, we highly recommend you to try the [IRKernel](https://irkernel.github.io/installation/#windows-panel) to use R in Jupyter Notebook. To do so, ollow the steps in the [installation guide](https://github.com/alexanderquispe/ECO224/blob/main/Installation/Python_R_installation.md#ikernel). You will require 
to install R separately (from [CRAN](https://cran.r-project.org/bin/windows/base/)).


