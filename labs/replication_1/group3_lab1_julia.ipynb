{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Workgroup - group 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Math Demonstrations**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Prove the Frisch-Waugh-Lovell theorem"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the model:\n",
    "\\begin{align*}\n",
    "y &= D \\beta_1 + W \\beta_2 + \\mu\n",
    "\\end{align*}\n",
    "where $y$ is an $n \\times 1$ vector, $D$ is an $n \\times k_1$ matrix, $\\beta_1$ is a $k_1 \\times 1$ vector, $W$ is an $n \\times k_2$ matrix, $\\beta_2$ is a $k_2 \\times 1$ vector, and $\\mu$ is an $n \\times 1$ vector of error terms.\n",
    "\n",
    "We can construct the following equation:\n",
    "\n",
    "\\begin{align*}\n",
    "\\epsilon_y &= \\epsilon_D \\phi + \\xi\n",
    "\\end{align*}\n",
    "\n",
    "Running $y$ on $W$, we get:\n",
    "\n",
    "\\begin{align*}\n",
    "y &= W\\hat{\\alpha}_1 + \\epsilon_y \\iff \\epsilon_y &= y - W\\hat{\\alpha}_1\n",
    "\\end{align*}\n",
    "\n",
    "Similarly, running $D$ on $W$ gives us:\n",
    "\n",
    "\\begin{align*}\n",
    "D &= W\\hat{\\alpha}_2 + \\epsilon_D \\iff \\epsilon_D &= D - W\\hat{\\alpha}_2\n",
    "\\end{align*}\n",
    "\n",
    "Running $\\epsilon_y$ on $\\epsilon_D$:\n",
    "\\begin{align*}\n",
    "y - W \\hat{\\alpha}_1 &= (D - W \\hat{\\alpha}_2) \\phi + \\xi \\\\\n",
    "y &= W \\hat{\\alpha}_1 + (D - W \\hat{\\alpha}_2) \\phi + \\xi \\\\\n",
    "y &= W \\hat{\\alpha}_1 + D \\phi - W \\hat{\\alpha}_2 \\phi + \\xi \\\\\n",
    "y &= D \\phi + W (\\hat{\\alpha}_1 - \\hat{\\alpha}_2 \\phi) + \\xi\n",
    "\\end{align*}\n",
    "\n",
    "Comparing the original model with this, we can see that:\n",
    "\\begin{align*}\n",
    "    \\beta_1 &= \\phi \\\\\n",
    "    \\beta_2 &= \\hat{\\alpha}_1 - \\hat{\\alpha}_2 \\phi \\\\\n",
    "    \\mu &= \\xi\n",
    "\\end{align*}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Show that the Conditional Expectation Function minimizes expected squared error"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the model:\n",
    "\\begin{align*}\n",
    "Y &= m(X) + e\n",
    "\\end{align*}\n",
    "where $m(X)$ represents the conditional expectation of $Y$ on $X$. Let's define an arbitrary model:\n",
    "\\begin{align*}\n",
    "Y &= g(X) + w\n",
    "\\end{align*}\n",
    "where $g(X)$ represents any function of $X$.\n",
    "\n",
    "Working with the expected squared error from the arbitrary model:\n",
    "\\begin{align*}\n",
    "E[(Y-g(X))^2] &= E[(Y-m(X) + m(X)-g(X))^2] \\\\\n",
    "&= E[(Y-m(X))^2 + 2(Y-m(X))(m(X)-g(X)) + (m(X)-g(X))^2] \\\\\n",
    "&= E[e^2] + 2E[(Y-m(X))(m(X)-g(X))] + E[(m(X)-g(X))^2]\n",
    "\\end{align*}\n",
    "Using the law of iterated expectations:\n",
    "\\begin{align*}\n",
    "E[(Y-g(X))^2] &= E[e^2] + 2E[E[(Y-m(X))(m(X)-g(X)) | X]] + E[(m(X)-g(X))^2]\n",
    "\\end{align*}\n",
    "Since $m(X)$ and $g(X)$ are functions of $X$, the term $(m(X)-g(X))$ can be thought of as constant when conditioning on $X$. Thus:\n",
    "\\begin{align*}\n",
    "E[(Y-g(X))^2] &= E[e^2] + 2E[E[Y-m(X) | X](m(X)-g(X))] + E[(m(X)-g(X))^2]\n",
    "\\end{align*}\n",
    "It is important to note that $E[Y-m(X) | X] = 0$ by definition of $m(X)$, so we get:\n",
    "\\begin{align*}\n",
    "E[(Y-g(X))^2] &= E[e^2] + E[(m(X)-g(X))^2]\n",
    "\\end{align*}\n",
    "Because the second term in the equation is always non-negative, it is clear that the function is minimized when $g(X)$ equals $m(X)$. In which case:\n",
    "\\begin{align*}\n",
    "E[(Y-g(X))^2] &= E[e^2]\n",
    "\\end{align*}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This notebook contains an example for teaching."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Replication 1 - Code**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the previous lab, we already analyzed data from the March Supplement of the U.S. Current Population Survey (2015) and answered the question how to use job-relevant characteristics, such as education and experience, to best predict wages. Now, we focus on the following inference question:\n",
    "\n",
    "What is the difference in predicted wages between men and women with the same job-relevant characteristics?\n",
    "\n",
    "Thus, we analyze if there is a difference in the payment of men and women (*gender wage gap*). The gender wage gap may partly reflect *discrimination* against women in the labor market or may partly reflect a *selection effect*, namely that women are relatively more likely to take on occupations that pay somewhat less (for example, school teaching)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To investigate the gender wage gap, we consider the following log-linear regression model\n",
    "\n",
    "\\begin{align}\n",
    "\\log(Y) &= \\beta'X + \\epsilon\\\\\n",
    "&= \\beta_1 D  + \\beta_2' W + \\epsilon,\n",
    "\\end{align}\n",
    "\n",
    "where $D$ is the indicator of being female ($1$ if female and $0$ otherwise) and the\n",
    "$W$'s are controls explaining variation in wages. Considering transformed wages by the logarithm, we are analyzing the relative difference in the payment of men and women."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We consider the same subsample of the U.S. Current Population Survey (2015) as in the previous lab. Let us load the data set.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m registry at `~/.julia/registries/General.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `~/.julia/environments/v1.10/Manifest.toml`\n"
     ]
    },
    {
     "ename": "LoadError",
     "evalue": "ArgumentError: Package RData not found in current path.\n- Run `import Pkg; Pkg.add(\"RData\")` to install the RData package.",
     "output_type": "error",
     "traceback": [
      "ArgumentError: Package RData not found in current path.\n- Run `import Pkg; Pkg.add(\"RData\")` to install the RData package.",
      "",
      "Stacktrace:",
      " [1] macro expansion",
      "   @ ./loading.jl:1772 [inlined]",
      " [2] macro expansion",
      "   @ ./lock.jl:267 [inlined]",
      " [3] __require(into::Module, mod::Symbol)",
      "   @ Base ./loading.jl:1753",
      " [4] #invoke_in_world#3",
      "   @ ./essentials.jl:926 [inlined]",
      " [5] invoke_in_world",
      "   @ ./essentials.jl:923 [inlined]",
      " [6] require(into::Module, mod::Symbol)",
      "   @ Base ./loading.jl:1746"
     ]
    }
   ],
   "source": [
    "using Pkg\n",
    "\n",
    "Pkg.add(\"DataFrames\")\n",
    "Pkg.add(\"Dates\")\n",
    "Pkg.add(\"Plots\")\n",
    "Pkg.add(\"CategoricalArrays\")\n",
    "\n",
    "using DataFrames\n",
    "using Dates\n",
    "using Plots\n",
    "using Statistics,RData  #upload data of R format \n",
    "using CategoricalArrays # categorical data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Rows : 5150\n",
      "Number of Columns : 20\n"
     ]
    }
   ],
   "source": [
    "rdata_read = load(\"../../../data/wage2015_subsample_inference.RData\")\n",
    "data = rdata_read[\"data\"]\n",
    "names(data)\n",
    "println(\"Number of Rows : \", size(data)[1],\"\\n\",\"Number of Columns : \", size(data)[2],) #rows and columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***Variable description***\n",
    "\n",
    "- occ : occupational classification\n",
    "- ind : industry classification\n",
    "- lwage : log hourly wage\n",
    "- sex : gender (1 female) (0 male)\n",
    "- shs : some high school\n",
    "- hsg : High school graduated\n",
    "- scl : Some College\n",
    "- clg: College Graduate\n",
    "- ad: Advanced Degree\n",
    "- ne: Northeast\n",
    "- mw: Midwest\n",
    "- so: South\n",
    "- we: West\n",
    "- exp1: experience"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>20 rows × 7 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>variable</th><th>mean</th><th>min</th><th>median</th><th>max</th><th>nmissing</th><th>eltype</th></tr><tr><th></th><th title=\"Symbol\">Symbol</th><th title=\"Union{Nothing, Float64}\">Union…</th><th title=\"Any\">Any</th><th title=\"Union{Nothing, Float64}\">Union…</th><th title=\"Any\">Any</th><th title=\"Int64\">Int64</th><th title=\"DataType\">DataType</th></tr></thead><tbody><tr><th>1</th><td>wage</td><td>23.4104</td><td>3.02198</td><td>19.2308</td><td>528.846</td><td>0</td><td>Float64</td></tr><tr><th>2</th><td>lwage</td><td>2.97079</td><td>1.10591</td><td>2.95651</td><td>6.2707</td><td>0</td><td>Float64</td></tr><tr><th>3</th><td>sex</td><td>0.444466</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>4</th><td>shs</td><td>0.023301</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>5</th><td>hsg</td><td>0.243883</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>6</th><td>scl</td><td>0.278058</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>7</th><td>clg</td><td>0.31767</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>8</th><td>ad</td><td>0.137087</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>9</th><td>mw</td><td>0.259612</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>10</th><td>so</td><td>0.296505</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>11</th><td>we</td><td>0.216117</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>12</th><td>ne</td><td>0.227767</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>13</th><td>exp1</td><td>13.7606</td><td>0.0</td><td>10.0</td><td>47.0</td><td>0</td><td>Float64</td></tr><tr><th>14</th><td>exp2</td><td>3.01893</td><td>0.0</td><td>1.0</td><td>22.09</td><td>0</td><td>Float64</td></tr><tr><th>15</th><td>exp3</td><td>8.23587</td><td>0.0</td><td>1.0</td><td>103.823</td><td>0</td><td>Float64</td></tr><tr><th>16</th><td>exp4</td><td>25.118</td><td>0.0</td><td>1.0</td><td>487.968</td><td>0</td><td>Float64</td></tr><tr><th>17</th><td>occ</td><td></td><td>10</td><td></td><td>1e+05</td><td>0</td><td>CategoricalValue{String, UInt16}</td></tr><tr><th>18</th><td>occ2</td><td></td><td>1</td><td></td><td>22</td><td>0</td><td>CategoricalValue{String, UInt8}</td></tr><tr><th>19</th><td>ind</td><td></td><td>370</td><td></td><td>1e+05</td><td>0</td><td>CategoricalValue{String, UInt8}</td></tr><tr><th>20</th><td>ind2</td><td></td><td>2</td><td></td><td>22</td><td>0</td><td>CategoricalValue{String, UInt8}</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccccccc}\n",
       "\t& variable & mean & min & median & max & nmissing & eltype\\\\\n",
       "\t\\hline\n",
       "\t& Symbol & Union… & Any & Union… & Any & Int64 & DataType\\\\\n",
       "\t\\hline\n",
       "\t1 & wage & 23.4104 & 3.02198 & 19.2308 & 528.846 & 0 & Float64 \\\\\n",
       "\t2 & lwage & 2.97079 & 1.10591 & 2.95651 & 6.2707 & 0 & Float64 \\\\\n",
       "\t3 & sex & 0.444466 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t4 & shs & 0.023301 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t5 & hsg & 0.243883 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t6 & scl & 0.278058 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t7 & clg & 0.31767 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t8 & ad & 0.137087 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t9 & mw & 0.259612 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t10 & so & 0.296505 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t11 & we & 0.216117 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t12 & ne & 0.227767 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t13 & exp1 & 13.7606 & 0.0 & 10.0 & 47.0 & 0 & Float64 \\\\\n",
       "\t14 & exp2 & 3.01893 & 0.0 & 1.0 & 22.09 & 0 & Float64 \\\\\n",
       "\t15 & exp3 & 8.23587 & 0.0 & 1.0 & 103.823 & 0 & Float64 \\\\\n",
       "\t16 & exp4 & 25.118 & 0.0 & 1.0 & 487.968 & 0 & Float64 \\\\\n",
       "\t17 & occ &  & 10 &  & 1e+05 & 0 & CategoricalValue\\{String, UInt16\\} \\\\\n",
       "\t18 & occ2 &  & 1 &  & 22 & 0 & CategoricalValue\\{String, UInt8\\} \\\\\n",
       "\t19 & ind &  & 370 &  & 1e+05 & 0 & CategoricalValue\\{String, UInt8\\} \\\\\n",
       "\t20 & ind2 &  & 2 &  & 22 & 0 & CategoricalValue\\{String, UInt8\\} \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m20×7 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m variable \u001b[0m\u001b[1m mean     \u001b[0m\u001b[1m min     \u001b[0m\u001b[1m median  \u001b[0m\u001b[1m max     \u001b[0m\u001b[1m nmissing \u001b[0m\u001b[1m eltype        \u001b[0m ⋯\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Symbol   \u001b[0m\u001b[90m Union…   \u001b[0m\u001b[90m Any     \u001b[0m\u001b[90m Union…  \u001b[0m\u001b[90m Any     \u001b[0m\u001b[90m Int64    \u001b[0m\u001b[90m DataType      \u001b[0m ⋯\n",
       "─────┼──────────────────────────────────────────────────────────────────────────\n",
       "   1 │ wage      23.4104   3.02198  19.2308  528.846         0  Float64        ⋯\n",
       "   2 │ lwage     2.97079   1.10591  2.95651  6.2707          0  Float64\n",
       "   3 │ sex       0.444466  0.0      0.0      1.0             0  Float64\n",
       "   4 │ shs       0.023301  0.0      0.0      1.0             0  Float64\n",
       "   5 │ hsg       0.243883  0.0      0.0      1.0             0  Float64        ⋯\n",
       "   6 │ scl       0.278058  0.0      0.0      1.0             0  Float64\n",
       "   7 │ clg       0.31767   0.0      0.0      1.0             0  Float64\n",
       "   8 │ ad        0.137087  0.0      0.0      1.0             0  Float64\n",
       "   9 │ mw        0.259612  0.0      0.0      1.0             0  Float64        ⋯\n",
       "  10 │ so        0.296505  0.0      0.0      1.0             0  Float64\n",
       "  11 │ we        0.216117  0.0      0.0      1.0             0  Float64\n",
       "  12 │ ne        0.227767  0.0      0.0      1.0             0  Float64\n",
       "  13 │ exp1      13.7606   0.0      10.0     47.0            0  Float64        ⋯\n",
       "  14 │ exp2      3.01893   0.0      1.0      22.09           0  Float64\n",
       "  15 │ exp3      8.23587   0.0      1.0      103.823         0  Float64\n",
       "  16 │ exp4      25.118    0.0      1.0      487.968         0  Float64\n",
       "  17 │ occ      \u001b[90m          \u001b[0m 10      \u001b[90m         \u001b[0m 1e+05           0  CategoricalVal ⋯\n",
       "  18 │ occ2     \u001b[90m          \u001b[0m 1       \u001b[90m         \u001b[0m 22              0  CategoricalVal\n",
       "  19 │ ind      \u001b[90m          \u001b[0m 370     \u001b[90m         \u001b[0m 1e+05           0  CategoricalVal\n",
       "  20 │ ind2     \u001b[90m          \u001b[0m 2       \u001b[90m         \u001b[0m 22              0  CategoricalVal\n",
       "\u001b[36m                                                                1 column omitted\u001b[0m"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "describe(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To start our (causal) analysis, we compare the sample means given gender:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>12 rows × 4 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>variables</th><th>All</th><th>Men</th><th>Female</th></tr><tr><th></th><th title=\"String\">String</th><th title=\"Float64\">Float64</th><th title=\"Float64\">Float64</th><th title=\"Float64\">Float64</th></tr></thead><tbody><tr><th>1</th><td>lwage</td><td>2.97079</td><td>2.98783</td><td>2.94948</td></tr><tr><th>2</th><td>sex</td><td>0.444466</td><td>0.0</td><td>1.0</td></tr><tr><th>3</th><td>shs</td><td>0.023301</td><td>0.0318071</td><td>0.0126693</td></tr><tr><th>4</th><td>hsg</td><td>0.243883</td><td>0.294303</td><td>0.180865</td></tr><tr><th>5</th><td>scl</td><td>0.278058</td><td>0.273331</td><td>0.283967</td></tr><tr><th>6</th><td>clg</td><td>0.31767</td><td>0.293953</td><td>0.347313</td></tr><tr><th>7</th><td>ad</td><td>0.137087</td><td>0.106606</td><td>0.175186</td></tr><tr><th>8</th><td>ne</td><td>0.227767</td><td>0.22195</td><td>0.235037</td></tr><tr><th>9</th><td>mw</td><td>0.259612</td><td>0.259</td><td>0.260376</td></tr><tr><th>10</th><td>so</td><td>0.296505</td><td>0.298148</td><td>0.294452</td></tr><tr><th>11</th><td>we</td><td>0.216117</td><td>0.220902</td><td>0.210135</td></tr><tr><th>12</th><td>exp1</td><td>13.7606</td><td>13.784</td><td>13.7313</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|cccc}\n",
       "\t& variables & All & Men & Female\\\\\n",
       "\t\\hline\n",
       "\t& String & Float64 & Float64 & Float64\\\\\n",
       "\t\\hline\n",
       "\t1 & lwage & 2.97079 & 2.98783 & 2.94948 \\\\\n",
       "\t2 & sex & 0.444466 & 0.0 & 1.0 \\\\\n",
       "\t3 & shs & 0.023301 & 0.0318071 & 0.0126693 \\\\\n",
       "\t4 & hsg & 0.243883 & 0.294303 & 0.180865 \\\\\n",
       "\t5 & scl & 0.278058 & 0.273331 & 0.283967 \\\\\n",
       "\t6 & clg & 0.31767 & 0.293953 & 0.347313 \\\\\n",
       "\t7 & ad & 0.137087 & 0.106606 & 0.175186 \\\\\n",
       "\t8 & ne & 0.227767 & 0.22195 & 0.235037 \\\\\n",
       "\t9 & mw & 0.259612 & 0.259 & 0.260376 \\\\\n",
       "\t10 & so & 0.296505 & 0.298148 & 0.294452 \\\\\n",
       "\t11 & we & 0.216117 & 0.220902 & 0.210135 \\\\\n",
       "\t12 & exp1 & 13.7606 & 13.784 & 13.7313 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m12×4 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m variables \u001b[0m\u001b[1m All       \u001b[0m\u001b[1m Men        \u001b[0m\u001b[1m Female     \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m String    \u001b[0m\u001b[90m Float64   \u001b[0m\u001b[90m Float64    \u001b[0m\u001b[90m Float64    \u001b[0m\n",
       "─────┼──────────────────────────────────────────────\n",
       "   1 │ lwage       2.97079    2.98783     2.94948\n",
       "   2 │ sex         0.444466   0.0         1.0\n",
       "   3 │ shs         0.023301   0.0318071   0.0126693\n",
       "   4 │ hsg         0.243883   0.294303    0.180865\n",
       "   5 │ scl         0.278058   0.273331    0.283967\n",
       "   6 │ clg         0.31767    0.293953    0.347313\n",
       "   7 │ ad          0.137087   0.106606    0.175186\n",
       "   8 │ ne          0.227767   0.22195     0.235037\n",
       "   9 │ mw          0.259612   0.259       0.260376\n",
       "  10 │ so          0.296505   0.298148    0.294452\n",
       "  11 │ we          0.216117   0.220902    0.210135\n",
       "  12 │ exp1       13.7606    13.784      13.7313"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Z = select(data, [\"lwage\",\"sex\",\"shs\",\"hsg\",\"scl\",\"clg\",\"ad\",\"ne\",\"mw\",\"so\",\"we\",\"exp1\"])\n",
    "\n",
    "data_female = filter(row -> row.sex == 1, data)\n",
    "Z_female = select(data_female,[\"lwage\",\"sex\",\"shs\",\"hsg\",\"scl\",\"clg\",\"ad\",\"ne\",\"mw\",\"so\",\"we\",\"exp1\"] )\n",
    "\n",
    "data_male = filter(row -> row.sex == 0, data)\n",
    "Z_male = select(data_male,[\"lwage\",\"sex\",\"shs\",\"hsg\",\"scl\",\"clg\",\"ad\",\"ne\",\"mw\",\"so\",\"we\",\"exp1\"] )\n",
    "\n",
    "means = DataFrame( variables = names(Z), All = describe(Z, :mean)[!,2], Men = describe(Z_male,:mean)[!,2], Female = describe(Z_female,:mean)[!,2])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In particular, the table above shows that the difference in average logwage between men and women is equal to $0,038$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.03834473367441493"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean(Z_female[:,:lwage]) - mean(Z_male[:,:lwage])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Thus, the unconditional gender wage gap is about $3,8$\\% for the group of never married workers (women get paid less on average in our sample). We also observe that never married working women are relatively more educated than working men and have lower working experience."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This unconditional (predictive) effect of gender equals the coefficient $\\beta$ in the univariate ols regression of $Y$ on $D$:\n",
    "\n",
    "\\begin{align}\n",
    "\\log(Y) &=\\beta D + \\epsilon.\n",
    "\\end{align}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We verify this by running an ols regression in Julia."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m MLBase ─ v0.9.2\n",
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      " \u001b[90m [f0e99cf1] \u001b[39m\u001b[92m+ MLBase v0.9.2\u001b[39m\n",
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      " \u001b[90m [f0e99cf1] \u001b[39m\u001b[93m↑ MLBase v0.9.0 ⇒ v0.9.2\u001b[39m\n",
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m project...\n",
      "\u001b[32m  ✓ \u001b[39mMLBase\n",
      "\u001b[32m  ✓ \u001b[39mLasso\n",
      "  2 dependencies successfully precompiled in 4 seconds (323 already precompiled)\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling CovarianceMatrices [60f91f6f-d783-54cb-84f9-544141854719]\n"
     ]
    }
   ],
   "source": [
    "#install all the package that we can need\n",
    "Pkg.add(\"GLM\") # package to run models \n",
    "Pkg.add(\"StatsPlots\")\n",
    "Pkg.add(\"MLBase\")\n",
    "Pkg.add(\"Tables\")\n",
    "Pkg.add(\"CovarianceMatrices\") # robust standar error \n",
    "# Load the installed packages\n",
    "using DataFrames\n",
    "using CSV\n",
    "using Tables\n",
    "using GLM\n",
    "using CovarianceMatrices\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The estimated gender coefficient is -0.03834473367440746 and the corresponding robust standard error is 0.015905023733117172\n"
     ]
    }
   ],
   "source": [
    "nocontrol_model = lm(@formula(lwage ~ sex), data)\n",
    "nocontrol_est = GLM.coef(nocontrol_model)[2]\n",
    "nocontrol_se = GLM.coeftable(nocontrol_model).cols[2][2]\n",
    "\n",
    "nocontrol_se1 = stderror(HC1(), nocontrol_model)[2]\n",
    "println(\"The estimated gender coefficient is \", nocontrol_est ,\" and the corresponding robust standard error is \" ,nocontrol_se1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we run an ols regression of $Y$ on $(D,W)$ to control for the effect of covariates summarized in $W$:\n",
    "\n",
    "\\begin{align}\n",
    "\\log(Y) &=\\beta_1 D  + \\beta_2' W + \\epsilon.\n",
    "\\end{align}\n",
    "\n",
    "Here, we are considering the flexible model from the previous lab. Hence, $W$ controls for experience, education, region, and occupation and industry indicators plus transformations and two-way interactions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let us run the ols regression with controls."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ols regression with controls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.015000474421752112"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "flex = @formula(lwage ~ sex + (exp1+exp2+exp3+exp4) * (shs+hsg+scl+clg+occ2+ind2+mw+so+we))\n",
    "control_model = lm(flex , data)\n",
    "control_est = GLM.coef(control_model)[2]\n",
    "control_se = GLM.coeftable(control_model).cols[2][2]\n",
    "control_se1 = stderror( HC0(), control_model)[2]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "StatsModels.TableRegressionModel{LinearModel{GLM.LmResp{Vector{Float64}}, GLM.DensePredChol{Float64, LinearAlgebra.CholeskyPivoted{Float64, Matrix{Float64}}}}, Matrix{Float64}}\n",
       "\n",
       "lwage ~ 1 + sex + exp1 + exp2 + exp3 + exp4 + shs + hsg + scl + clg + occ2 + ind2 + mw + so + we + exp1 & shs + exp1 & hsg + exp1 & scl + exp1 & clg + exp1 & occ2 + exp1 & ind2 + exp1 & mw + exp1 & so + exp1 & we + exp2 & shs + exp2 & hsg + exp2 & scl + exp2 & clg + exp2 & occ2 + exp2 & ind2 + exp2 & mw + exp2 & so + exp2 & we + exp3 & shs + exp3 & hsg + exp3 & scl + exp3 & clg + exp3 & occ2 + exp3 & ind2 + exp3 & mw + exp3 & so + exp3 & we + exp4 & shs + exp4 & hsg + exp4 & scl + exp4 & clg + exp4 & occ2 + exp4 & ind2 + exp4 & mw + exp4 & so + exp4 & we\n",
       "\n",
       "Coefficients:\n",
       "────────────────────────────────────────────────────────────────────────────────────\n",
       "                        Coef.  Std. Error      t  Pr(>|t|)    Lower 95%    Upper 95%\n",
       "────────────────────────────────────────────────────────────────────────────────────\n",
       "(Intercept)       3.86026       0.428619    9.01    <1e-18    3.01998     4.70055\n",
       "sex              -0.0695532     0.015218   -4.57    <1e-05   -0.0993874  -0.039719\n",
       "exp1             -0.0677247     0.151976   -0.45    0.6559   -0.365665    0.230215\n",
       "exp2              1.63629       1.69093     0.97    0.3332   -1.67868     4.95127\n",
       "exp3             -0.915474      0.688025   -1.33    0.1834   -2.26431     0.433363\n",
       "exp4              0.142936      0.0907569   1.57    0.1153   -0.0349885   0.32086\n",
       "shs              -0.123309      0.906832   -0.14    0.8918   -1.90111     1.65449\n",
       "hsg              -0.528902      0.197756   -2.67    0.0075   -0.916593   -0.141212\n",
       "scl              -0.292058      0.126016   -2.32    0.0205   -0.539105   -0.0450112\n",
       "clg              -0.0411641     0.0703862  -0.58    0.5587   -0.179153    0.0968245\n",
       "occ2: 2           0.16134       0.129724    1.24    0.2137   -0.0929781   0.415657\n",
       "occ2: 3           0.210151      0.168677    1.25    0.2129   -0.120532    0.540835\n",
       "occ2: 4           0.070857      0.183717    0.39    0.6997   -0.28931     0.431024\n",
       "occ2: 5          -0.396008      0.18854    -2.10    0.0357   -0.76563    -0.026385\n",
       "occ2: 6          -0.231061      0.186966   -1.24    0.2166   -0.597599    0.135476\n",
       "occ2: 7           0.314725      0.194152    1.62    0.1051   -0.0658997   0.69535\n",
       "occ2: 8          -0.187542      0.169299   -1.11    0.2680   -0.519443    0.14436\n",
       "occ2: 9          -0.339027      0.16723    -2.03    0.0427   -0.666873   -0.0111811\n",
       "occ2: 10          0.0209545     0.156498    0.13    0.8935   -0.285852    0.327761\n",
       "occ2: 11         -0.642418      0.30909    -2.08    0.0377   -1.24837    -0.036463\n",
       "occ2: 12         -0.0674774     0.252049   -0.27    0.7889   -0.561605    0.426651\n",
       "occ2: 13         -0.232978      0.231538   -1.01    0.3144   -0.686896    0.22094\n",
       "occ2: 14          0.256201      0.322673    0.79    0.4272   -0.376382    0.888784\n",
       "occ2: 15         -0.193858      0.259508   -0.75    0.4551   -0.702611    0.314894\n",
       "occ2: 16         -0.0551256     0.147066   -0.37    0.7078   -0.34344     0.233189\n",
       "occ2: 17         -0.415609      0.136114   -3.05    0.0023   -0.682454   -0.148764\n",
       "occ2: 18         -0.482217      1.04435    -0.46    0.6443   -2.52962     1.56518\n",
       "occ2: 19         -0.257941      0.332522   -0.78    0.4380   -0.909832    0.39395\n",
       "occ2: 20         -0.30102       0.234102   -1.29    0.1986   -0.759965    0.157925\n",
       "occ2: 21         -0.427181      0.220649   -1.94    0.0529   -0.859751    0.00538904\n",
       "occ2: 22         -0.869453      0.297522   -2.92    0.0035   -1.45273    -0.286176\n",
       "ind2: 3          -1.24737       0.645494   -1.93    0.0534   -2.51282     0.018092\n",
       "ind2: 4          -0.0948281     0.463602   -0.20    0.8379   -1.0037      0.81404\n",
       "ind2: 5          -0.529386      0.434599   -1.22    0.2232   -1.38139     0.322623\n",
       "ind2: 6          -0.622169      0.434723   -1.43    0.1524   -1.47442     0.230082\n",
       "ind2: 7          -0.50475       0.502477   -1.00    0.3152   -1.48983     0.48033\n",
       "ind2: 8          -0.729544      0.467401   -1.56    0.1186   -1.64586     0.186771\n",
       "ind2: 9          -0.802533      0.425246   -1.89    0.0592   -1.63621     0.0311395\n",
       "ind2: 10         -0.580584      0.480878   -1.21    0.2274   -1.52332     0.362151\n",
       "ind2: 11         -0.985235      0.448157   -2.20    0.0280   -1.86382    -0.106647\n",
       "ind2: 12         -0.737578      0.424326   -1.74    0.0822   -1.56945     0.0942913\n",
       "ind2: 13         -1.01833       0.482654   -2.11    0.0349   -1.96455    -0.0721096\n",
       "ind2: 14         -0.586017      0.415903   -1.41    0.1589   -1.40137     0.229339\n",
       "ind2: 15         -0.380136      0.590852   -0.64    0.5200   -1.53847     0.778198\n",
       "ind2: 16         -0.570391      0.438658   -1.30    0.1936   -1.43036     0.289575\n",
       "ind2: 17         -0.820184      0.425985   -1.93    0.0542   -1.6553      0.0149362\n",
       "ind2: 18         -0.76136       0.423829   -1.80    0.0725   -1.59225     0.0695337\n",
       "ind2: 19         -0.881282      0.456567   -1.93    0.0536   -1.77636     0.0137945\n",
       "ind2: 20         -0.909902      0.44842    -2.03    0.0425   -1.78901    -0.0307984\n",
       "ind2: 21         -0.758653      0.44058    -1.72    0.0851   -1.62239     0.105081\n",
       "ind2: 22         -0.404077      0.432873   -0.93    0.3506   -1.2527      0.444548\n",
       "mw                0.110683      0.0814463   1.36    0.1742   -0.0489879   0.270355\n",
       "so                0.0224244     0.0743855   0.30    0.7631   -0.123404    0.168253\n",
       "we               -0.0215659     0.0841591  -0.26    0.7978   -0.186556    0.143424\n",
       "exp1 & shs       -0.191998      0.195541   -0.98    0.3262   -0.575346    0.191349\n",
       "exp1 & hsg       -0.0173433     0.0572279  -0.30    0.7619   -0.129536    0.0948491\n",
       "exp1 & scl       -0.0664505     0.043373   -1.53    0.1256   -0.151481    0.01858\n",
       "exp1 & clg       -0.0550346     0.0310279  -1.77    0.0762   -0.115863    0.00579393\n",
       "exp1 & occ2: 2   -0.0736239     0.0501108  -1.47    0.1418   -0.171863    0.0246157\n",
       "exp1 & occ2: 3   -0.0714859     0.0637688  -1.12    0.2623   -0.196501    0.0535296\n",
       "exp1 & occ2: 4   -0.0723997     0.0747715  -0.97    0.3330   -0.218985    0.0741859\n",
       "exp1 & occ2: 5    0.0946732     0.0794005   1.19    0.2332   -0.0609873   0.250334\n",
       "exp1 & occ2: 6   -0.0348928     0.0712136  -0.49    0.6242   -0.174503    0.104718\n",
       "exp1 & occ2: 7   -0.227934      0.078486   -2.90    0.0037   -0.381802   -0.074066\n",
       "exp1 & occ2: 8   -0.0727459     0.0645883  -1.13    0.2601   -0.199368    0.0538762\n",
       "exp1 & occ2: 9    0.0274143     0.0669517   0.41    0.6822   -0.103841    0.15867\n",
       "exp1 & occ2: 10   0.00756285    0.0581715   0.13    0.8966   -0.106479    0.121605\n",
       "exp1 & occ2: 11   0.101422      0.100509    1.01    0.3130   -0.0956214   0.298466\n",
       "exp1 & occ2: 12  -0.0862744     0.0874768  -0.99    0.3241   -0.257768    0.0852193\n",
       "exp1 & occ2: 13   0.00671485    0.0761825   0.09    0.9298   -0.142637    0.156067\n",
       "exp1 & occ2: 14  -0.136915      0.0974458  -1.41    0.1601   -0.327953    0.0541221\n",
       "exp1 & occ2: 15  -0.0400425     0.0898931  -0.45    0.6560   -0.216273    0.136188\n",
       "exp1 & occ2: 16  -0.0539314     0.0520926  -1.04    0.3006   -0.156056    0.0481934\n",
       "exp1 & occ2: 17   0.0147277     0.0467903   0.31    0.7530   -0.0770023   0.106458\n",
       "exp1 & occ2: 18   0.10741       0.471844    0.23    0.8199   -0.817616    1.03244\n",
       "exp1 & occ2: 19   0.0047165     0.106074    0.04    0.9645   -0.203237    0.21267\n",
       "exp1 & occ2: 20   0.0243156     0.0743274   0.33    0.7436   -0.121399    0.170031\n",
       "exp1 & occ2: 21   0.0791776     0.0696947   1.14    0.2560   -0.0574551   0.21581\n",
       "exp1 & occ2: 22   0.109325      0.0880828   1.24    0.2146   -0.063357    0.282006\n",
       "exp1 & ind2: 3    0.475889      0.222748    2.14    0.0327    0.0392024   0.912576\n",
       "exp1 & ind2: 4    0.0147304     0.15711     0.09    0.9253   -0.293276    0.322737\n",
       "exp1 & ind2: 5    0.125699      0.153163    0.82    0.4119   -0.174569    0.425966\n",
       "exp1 & ind2: 6    0.154027      0.152429    1.01    0.3123   -0.144801    0.452856\n",
       "exp1 & ind2: 7    0.102925      0.178694    0.58    0.5647   -0.247396    0.453245\n",
       "exp1 & ind2: 8    0.235767      0.16892     1.40    0.1629   -0.0953924   0.566926\n",
       "exp1 & ind2: 9    0.135908      0.148949    0.91    0.3616   -0.156098    0.427914\n",
       "exp1 & ind2: 10   0.151258      0.164434    0.92    0.3577   -0.171107    0.473622\n",
       "exp1 & ind2: 11   0.317489      0.159002    2.00    0.0459    0.0057729   0.629204\n",
       "exp1 & ind2: 12   0.259109      0.151059    1.72    0.0864   -0.0370341   0.555252\n",
       "exp1 & ind2: 13   0.339609      0.166924    2.03    0.0420    0.0123634   0.666855\n",
       "exp1 & ind2: 14   0.144141      0.147799    0.98    0.3295   -0.145612    0.433894\n",
       "exp1 & ind2: 15  -0.0568181     0.234985   -0.24    0.8089   -0.517494    0.403858\n",
       "exp1 & ind2: 16   0.0847295     0.155043    0.55    0.5848   -0.219223    0.388682\n",
       "exp1 & ind2: 17   0.172887      0.151328    1.14    0.2533   -0.123784    0.469557\n",
       "exp1 & ind2: 18   0.15654       0.149417    1.05    0.2948   -0.136385    0.449464\n",
       "exp1 & ind2: 19   0.15161       0.162085    0.94    0.3496   -0.166149    0.46937\n",
       "exp1 & ind2: 20   0.132663      0.156688    0.85    0.3972   -0.174516    0.439842\n",
       "exp1 & ind2: 21   0.21909       0.155505    1.41    0.1589   -0.0857694   0.52395\n",
       "exp1 & ind2: 22   0.114581      0.152343    0.75    0.4520   -0.184079    0.413241\n",
       "exp1 & mw        -0.0279931     0.0296572  -0.94    0.3453   -0.0861345   0.0301484\n",
       "exp1 & so        -0.00996775    0.0266868  -0.37    0.7088   -0.0622858   0.0423503\n",
       "exp1 & we         0.00630768    0.0301417   0.21    0.8342   -0.0527835   0.0653989\n",
       "exp2 & shs        1.90051       1.45025     1.31    0.1901   -0.94263     4.74364\n",
       "exp2 & hsg        0.117164      0.550973    0.21    0.8316   -0.962989    1.19732\n",
       "exp2 & scl        0.621792      0.462999    1.34    0.1793   -0.285892    1.52948\n",
       "exp2 & clg        0.409675      0.380217    1.08    0.2813   -0.335721    1.15507\n",
       "exp2 & occ2: 2    0.663217      0.552322    1.20    0.2299   -0.419581    1.74602\n",
       "exp2 & occ2: 3    0.641546      0.710278    0.90    0.3664   -0.750918    2.03401\n",
       "exp2 & occ2: 4    0.974842      0.865535    1.13    0.2601   -0.721994    2.67168\n",
       "exp2 & occ2: 5   -0.977882      0.973799   -1.00    0.3153   -2.88696     0.9312\n",
       "exp2 & occ2: 6    0.105086      0.800227    0.13    0.8955   -1.46372     1.67389\n",
       "exp2 & occ2: 7    3.14071       0.938942    3.34    0.0008    1.29996     4.98146\n",
       "exp2 & occ2: 8    0.671088      0.719208    0.93    0.3508   -0.738881    2.08106\n",
       "exp2 & occ2: 9    0.0231977     0.762914    0.03    0.9757   -1.47246     1.51885\n",
       "exp2 & occ2: 10  -0.269229      0.640527   -0.42    0.6743   -1.52495     0.986491\n",
       "exp2 & occ2: 11  -1.08165       1.00576    -1.08    0.2822   -3.05339     0.890081\n",
       "exp2 & occ2: 12   0.832374      0.934125    0.89    0.3729   -0.998929    2.66368\n",
       "exp2 & occ2: 13  -0.220981      0.772846   -0.29    0.7749   -1.73611     1.29414\n",
       "exp2 & occ2: 14   0.751116      0.927255    0.81    0.4180   -1.06672     2.56895\n",
       "exp2 & occ2: 15  -0.0326858     0.940912   -0.03    0.9723   -1.87729     1.81192\n",
       "exp2 & occ2: 16   0.363581      0.550955    0.66    0.5093   -0.716537    1.4437\n",
       "exp2 & occ2: 17  -0.265929      0.486113   -0.55    0.5844   -1.21893     0.687071\n",
       "exp2 & occ2: 18  -2.56088       5.17009    -0.50    0.6204  -12.6966      7.57482\n",
       "exp2 & occ2: 19  -0.129176      1.06169    -0.12    0.9032   -2.21056     1.95221\n",
       "exp2 & occ2: 20  -0.33233       0.722907   -0.46    0.6457   -1.74955     1.08489\n",
       "exp2 & occ2: 21  -0.91          0.685411   -1.33    0.1843   -2.25371     0.433714\n",
       "exp2 & occ2: 22  -0.855054      0.827941   -1.03    0.3018   -2.47819     0.768082\n",
       "exp2 & ind2: 3   -5.93689       2.40679    -2.47    0.0137  -10.6553     -1.2185\n",
       "exp2 & ind2: 4   -1.10534       1.7102     -0.65    0.5181   -4.4581      2.24741\n",
       "exp2 & ind2: 5   -2.01492       1.69192    -1.19    0.2337   -5.33184     1.302\n",
       "exp2 & ind2: 6   -2.22777       1.68169    -1.32    0.1853   -5.52464     1.06909\n",
       "exp2 & ind2: 7   -1.46481       2.01379    -0.73    0.4670   -5.41274     2.48312\n",
       "exp2 & ind2: 8   -2.94799       1.85954    -1.59    0.1130   -6.59353     0.697541\n",
       "exp2 & ind2: 9   -1.77962       1.64712    -1.08    0.2800   -5.00872     1.44948\n",
       "exp2 & ind2: 10  -2.19733       1.77386    -1.24    0.2155   -5.6749      1.28024\n",
       "exp2 & ind2: 11  -3.87768       1.76374    -2.20    0.0280   -7.3354     -0.419966\n",
       "exp2 & ind2: 12  -3.16904       1.68194    -1.88    0.0596   -6.46639     0.128306\n",
       "exp2 & ind2: 13  -3.9652        1.81307    -2.19    0.0288   -7.51963    -0.410767\n",
       "exp2 & ind2: 14  -2.07833       1.64904    -1.26    0.2076   -5.31118     1.15452\n",
       "exp2 & ind2: 15   0.191169      2.60754     0.07    0.9416   -4.92078     5.30311\n",
       "exp2 & ind2: 16  -1.32659       1.71856    -0.77    0.4402   -4.69574     2.04257\n",
       "exp2 & ind2: 17  -2.20029       1.68372    -1.31    0.1913   -5.50113     1.10055\n",
       "exp2 & ind2: 18  -2.20062       1.65666    -1.33    0.1841   -5.44842     1.04718\n",
       "exp2 & ind2: 19  -1.93085       1.78767    -1.08    0.2802   -5.43548     1.57377\n",
       "exp2 & ind2: 20  -1.94673       1.7244     -1.13    0.2590   -5.32732     1.43387\n",
       "exp2 & ind2: 21  -3.11274       1.72379    -1.81    0.0710   -6.49214     0.266666\n",
       "exp2 & ind2: 22  -1.85783       1.68495    -1.10    0.2703   -5.1611      1.44543\n",
       "exp2 & mw         0.200561      0.317291    0.63    0.5273   -0.421472    0.822594\n",
       "exp2 & so         0.0544354     0.281566    0.19    0.8467   -0.49756     0.606431\n",
       "exp2 & we         0.00127174    0.320787    0.00    0.9968   -0.627615    0.630159\n",
       "exp3 & shs       -0.672124      0.442663   -1.52    0.1290   -1.53994     0.195693\n",
       "exp3 & hsg       -0.0179937     0.208318   -0.09    0.9312   -0.426389    0.390402\n",
       "exp3 & scl       -0.199788      0.185519   -1.08    0.2816   -0.563488    0.163912\n",
       "exp3 & clg       -0.102523      0.164365   -0.62    0.5328   -0.424752    0.219706\n",
       "exp3 & occ2: 2   -0.20394       0.221139   -0.92    0.3565   -0.637471    0.22959\n",
       "exp3 & occ2: 3   -0.236962      0.287037   -0.83    0.4091   -0.799683    0.325759\n",
       "exp3 & occ2: 4   -0.436696      0.352017   -1.24    0.2148   -1.12681     0.253415\n",
       "exp3 & occ2: 5    0.38853       0.411886    0.94    0.3456   -0.418951    1.19601\n",
       "exp3 & occ2: 6    0.0484737     0.329353    0.15    0.8830   -0.597205    0.694152\n",
       "exp3 & occ2: 7   -1.39493       0.405011   -3.44    0.0006   -2.18893    -0.600926\n",
       "exp3 & occ2: 8   -0.20539       0.289573   -0.71    0.4782   -0.773082    0.362302\n",
       "exp3 & occ2: 9   -0.090966      0.314335   -0.29    0.7723   -0.707203    0.525271\n",
       "exp3 & occ2: 10   0.185475      0.257556    0.72    0.4715   -0.319451    0.690401\n",
       "exp3 & occ2: 11   0.393155      0.381776    1.03    0.3032   -0.355296    1.14161\n",
       "exp3 & occ2: 12  -0.220256      0.366021   -0.60    0.5474   -0.93782     0.497308\n",
       "exp3 & occ2: 13   0.0950356     0.290437    0.33    0.7435   -0.474351    0.664422\n",
       "exp3 & occ2: 14  -0.144393      0.334162   -0.43    0.6657   -0.799501    0.510714\n",
       "exp3 & occ2: 15   0.147708      0.364519    0.41    0.6853   -0.566913    0.862328\n",
       "exp3 & occ2: 16  -0.0378548     0.215129   -0.18    0.8603   -0.459604    0.383894\n",
       "exp3 & occ2: 17   0.15105       0.187808    0.80    0.4213   -0.217138    0.519238\n",
       "exp3 & occ2: 18   1.40844       1.88525     0.75    0.4550   -2.28748     5.10437\n",
       "exp3 & occ2: 19   0.0923425     0.404231    0.23    0.8193   -0.700131    0.884816\n",
       "exp3 & occ2: 20   0.180699      0.265208    0.68    0.4957   -0.339227    0.700626\n",
       "exp3 & occ2: 21   0.377908      0.255303    1.48    0.1389   -0.1226      0.878417\n",
       "exp3 & occ2: 22   0.285506      0.298421    0.96    0.3388   -0.299532    0.870544\n",
       "exp3 & ind2: 3    2.66658       0.98075     2.72    0.0066    0.743872    4.58929\n",
       "exp3 & ind2: 4    0.729843      0.687981    1.06    0.2888   -0.618908    2.07859\n",
       "exp3 & ind2: 5    0.994225      0.684243    1.45    0.1463   -0.347199    2.33565\n",
       "exp3 & ind2: 6    1.06414       0.680095    1.56    0.1177   -0.269148    2.39743\n",
       "exp3 & ind2: 7    0.708909      0.833796    0.85    0.3952   -0.925705    2.34352\n",
       "exp3 & ind2: 8    1.23409       0.748347    1.65    0.0992   -0.233001    2.70119\n",
       "exp3 & ind2: 9    0.828731      0.66759     1.24    0.2145   -0.480045    2.13751\n",
       "exp3 & ind2: 10   1.04482       0.706672    1.48    0.1393   -0.340577    2.43021\n",
       "exp3 & ind2: 11   1.68776       0.716215    2.36    0.0185    0.283655    3.09186\n",
       "exp3 & ind2: 12   1.37345       0.683557    2.01    0.0446    0.0333676   2.71352\n",
       "exp3 & ind2: 13   1.63767       0.72593     2.26    0.0241    0.214519    3.06082\n",
       "exp3 & ind2: 14   1.01629       0.671452    1.51    0.1302   -0.300056    2.33264\n",
       "exp3 & ind2: 15   0.187948      1.02997     0.18    0.8552   -1.83125     2.20715\n",
       "exp3 & ind2: 16   0.688968      0.696803    0.99    0.3228   -0.677078    2.05501\n",
       "exp3 & ind2: 17   1.00855       0.683699    1.48    0.1402   -0.331803    2.34891\n",
       "exp3 & ind2: 18   1.06056       0.672523    1.58    0.1149   -0.257887    2.37901\n",
       "exp3 & ind2: 19   0.895987      0.72256     1.24    0.2150   -0.520555    2.31253\n",
       "exp3 & ind2: 20   0.976894      0.695582    1.40    0.1603   -0.386758    2.34055\n",
       "exp3 & ind2: 21   1.44152       0.699648    2.06    0.0394    0.069898    2.81314\n",
       "exp3 & ind2: 22   0.968788      0.68285     1.42    0.1560   -0.369903    2.30748\n",
       "exp3 & mw        -0.0625771     0.124129   -0.50    0.6142   -0.305926    0.180772\n",
       "exp3 & so        -0.0115842     0.108422   -0.11    0.9149   -0.224139    0.200971\n",
       "exp3 & we        -0.0124875     0.125138   -0.10    0.9205   -0.257813    0.232838\n",
       "exp4 & shs        0.0777418     0.0475427   1.64    0.1021   -0.0154632   0.170947\n",
       "exp4 & hsg        0.000491255   0.0265964   0.02    0.9853   -0.0516497   0.0526322\n",
       "exp4 & scl        0.021076      0.0245289   0.86    0.3903   -0.0270117   0.0691637\n",
       "exp4 & clg        0.00786949    0.0227528   0.35    0.7295   -0.0367363   0.0524753\n",
       "exp4 & occ2: 2    0.0176389     0.0289257   0.61    0.5420   -0.0390683   0.0743462\n",
       "exp4 & occ2: 3    0.0303057     0.0376552   0.80    0.4210   -0.0435153   0.104127\n",
       "exp4 & occ2: 4    0.0584146     0.0457704   1.28    0.2019   -0.0313159   0.148145\n",
       "exp4 & occ2: 5   -0.0515181     0.0549489  -0.94    0.3485   -0.159243    0.0562063\n",
       "exp4 & occ2: 6   -0.0170182     0.0440847  -0.39    0.6995   -0.103444    0.0694076\n",
       "exp4 & occ2: 7    0.190535      0.0558757   3.41    0.0007    0.0809939   0.300077\n",
       "exp4 & occ2: 8    0.0196522     0.0379084   0.52    0.6042   -0.0546653   0.0939697\n",
       "exp4 & occ2: 9    0.0190014     0.0421099   0.45    0.6518   -0.0635528   0.101556\n",
       "exp4 & occ2: 10  -0.0333347     0.0338825  -0.98    0.3252   -0.0997595   0.0330901\n",
       "exp4 & occ2: 11  -0.0465914     0.0479018  -0.97    0.3308   -0.1405      0.0473175\n",
       "exp4 & occ2: 12   0.0110212     0.0470536   0.23    0.8148   -0.0812249   0.103267\n",
       "exp4 & occ2: 13  -0.0136895     0.0358988  -0.38    0.7030   -0.0840673   0.0566883\n",
       "exp4 & occ2: 14   0.00555824    0.0400331   0.14    0.8896   -0.0729245   0.084041\n",
       "exp4 & occ2: 15  -0.0327444     0.0462379  -0.71    0.4789   -0.123391    0.0579026\n",
       "exp4 & occ2: 16  -0.00897062    0.0275729  -0.33    0.7449   -0.0630259   0.0450847\n",
       "exp4 & occ2: 17  -0.0256735     0.0239306  -1.07    0.2834   -0.0725881   0.0212412\n",
       "exp4 & occ2: 18  -0.212137      0.2204     -0.96    0.3358   -0.64422     0.219946\n",
       "exp4 & occ2: 19  -0.0169398     0.0513428  -0.33    0.7415   -0.117595    0.083715\n",
       "exp4 & occ2: 20  -0.0296125     0.0323353  -0.92    0.3598   -0.0930042   0.0337791\n",
       "exp4 & occ2: 21  -0.0524577     0.0317251  -1.65    0.0983   -0.114653    0.00973765\n",
       "exp4 & occ2: 22  -0.0350646     0.0360687  -0.97    0.3310   -0.105775    0.0356463\n",
       "exp4 & ind2: 3   -0.385179      0.132907   -2.90    0.0038   -0.645735   -0.124623\n",
       "exp4 & ind2: 4   -0.120948      0.089958   -1.34    0.1789   -0.297306    0.0554102\n",
       "exp4 & ind2: 5   -0.144105      0.0897994  -1.60    0.1086   -0.320152    0.0319425\n",
       "exp4 & ind2: 6   -0.152611      0.0892689  -1.71    0.0874   -0.327618    0.0223961\n",
       "exp4 & ind2: 7   -0.100199      0.11194    -0.90    0.3708   -0.319652    0.119253\n",
       "exp4 & ind2: 8   -0.160966      0.097978   -1.64    0.1005   -0.353047    0.0311143\n",
       "exp4 & ind2: 9   -0.117808      0.0877821  -1.34    0.1796   -0.2899      0.0542842\n",
       "exp4 & ind2: 10  -0.148284      0.0918416  -1.61    0.1065   -0.328335    0.0317665\n",
       "exp4 & ind2: 11  -0.232296      0.0944506  -2.46    0.0139   -0.417462   -0.0471307\n",
       "exp4 & ind2: 12  -0.187291      0.0899985  -2.08    0.0375   -0.363728   -0.0108538\n",
       "exp4 & ind2: 13  -0.215562      0.0946011  -2.28    0.0227   -0.401022   -0.0301012\n",
       "exp4 & ind2: 14  -0.148352      0.0884992  -1.68    0.0937   -0.32185     0.0251456\n",
       "exp4 & ind2: 15  -0.0532195     0.131382   -0.41    0.6854   -0.310786    0.204347\n",
       "exp4 & ind2: 16  -0.104434      0.0916252  -1.14    0.2544   -0.28406     0.0751928\n",
       "exp4 & ind2: 17  -0.142735      0.0899315  -1.59    0.1125   -0.319041    0.0335711\n",
       "exp4 & ind2: 18  -0.154625      0.0885883  -1.75    0.0810   -0.328298    0.019048\n",
       "exp4 & ind2: 19  -0.126959      0.0948784  -1.34    0.1809   -0.312963    0.059045\n",
       "exp4 & ind2: 20  -0.146855      0.0911188  -1.61    0.1071   -0.325489    0.0317784\n",
       "exp4 & ind2: 21  -0.203262      0.0920972  -2.21    0.0274   -0.383814   -0.0227102\n",
       "exp4 & ind2: 22  -0.148095      0.0897937  -1.65    0.0992   -0.324131    0.0279408\n",
       "exp4 & mw         0.00624394    0.0158699   0.39    0.6940   -0.0248681   0.037356\n",
       "exp4 & so         0.000314457   0.0136275   0.02    0.9816   -0.0264016   0.0270305\n",
       "exp4 & we         0.00176845    0.0159602   0.11    0.9118   -0.0295206   0.0330575\n",
       "────────────────────────────────────────────────────────────────────────────────────"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "control_model "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coefficient for OLS with controls -0.06955320329637253robust standard error:0.015000474421752112\n"
     ]
    }
   ],
   "source": [
    "println(\"Coefficient for OLS with controls \" , control_est, \"robust standard error:\", control_se1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The estimated regression coefficient $\\beta_1\\approx-0.0696$ measures how our linear prediction of wage changes if we set the gender variable $D$ from 0 to 1, holding the controls $W$ fixed.\n",
    "We can call this the *predictive effect* (PE), as it measures the impact of a variable on the prediction we make. Overall, we see that the unconditional wage gap of size $4$\\% for women increases to about $7$\\% after controlling for worker characteristics.  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we are using the Frisch-Waugh-Lovell theorem from the lecture partialling-out the linear effect of the controls via ols."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Partialling-Out using ols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2-element Vector{Float64}:\n",
       " -0.09867142357486275\n",
       " -0.04043498301882939"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# models\n",
    "# model for Y\n",
    "flex_y = @formula(lwage ~ (exp1+exp2+exp3+exp4) * (shs+hsg+scl+clg+occ2+ind2+mw+so+we))\n",
    "flex_d = @formula(sex ~ (exp1+exp2+exp3+exp4) * (shs+hsg+scl+clg+occ2+ind2+mw+so+we))\n",
    "\n",
    "# partialling-out the linear effect of W from Y\n",
    "t_Y = residuals(lm(flex_y, data))\n",
    "\n",
    "# partialling-out the linear effect of W from D\n",
    "t_D = residuals(lm(flex_d, data))\n",
    "\n",
    "data_res = DataFrame(t_Y = t_Y, t_D = t_D )\n",
    "# regression of Y on D after partialling-out the effect of W\n",
    "\n",
    "partial_fit = lm(@formula(t_Y ~ t_D), data_res)\n",
    "\n",
    "partial_est = GLM.coef(partial_fit)[2]\n",
    "\n",
    "# standard error\n",
    "partial_se = GLM.coeftable(partial_fit).cols[2][2]\n",
    "\n",
    "partial_se1 = stderror( HC0(), partial_fit)[2]\n",
    "\n",
    "#condifence interval\n",
    "GLM.confint(partial_fit)[2,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coefficient for D via partiallig-out -0.06955320329684607 robust standard error:0.015000474421752112\n"
     ]
    }
   ],
   "source": [
    "println(\"Coefficient for D via partiallig-out \", partial_est, \" robust standard error:\", control_se1 )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Again, the estimated coefficient measures the linear predictive effect (PE) of $D$ on $Y$ after taking out the linear effect of $W$ on both of these variables. This coefficient equals the estimated coefficient from the ols regression with controls."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We know that the partialling-out approach works well when the dimension of $W$ is low\n",
    "in relation to the sample size $n$. When the dimension of $W$ is relatively high, we need to use variable selection\n",
    "or penalization for regularization purposes. \n",
    "\n",
    "In the following, we illustrate the partialling-out approach using lasso instead of ols. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Summarize the results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>3 rows × 3 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>modelos</th><th>Estimate</th><th>StdError</th></tr><tr><th></th><th title=\"String\">String</th><th title=\"Float64\">Float64</th><th title=\"Float64\">Float64</th></tr></thead><tbody><tr><th>1</th><td>Without controls</td><td>-0.0383447</td><td>0.015905</td></tr><tr><th>2</th><td>full reg</td><td>-0.0695532</td><td>0.0150005</td></tr><tr><th>3</th><td>partial reg</td><td>-0.0695532</td><td>0.0150005</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccc}\n",
       "\t& modelos & Estimate & StdError\\\\\n",
       "\t\\hline\n",
       "\t& String & Float64 & Float64\\\\\n",
       "\t\\hline\n",
       "\t1 & Without controls & -0.0383447 & 0.015905 \\\\\n",
       "\t2 & full reg & -0.0695532 & 0.0150005 \\\\\n",
       "\t3 & partial reg & -0.0695532 & 0.0150005 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m3×3 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m modelos          \u001b[0m\u001b[1m Estimate   \u001b[0m\u001b[1m StdError  \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m String           \u001b[0m\u001b[90m Float64    \u001b[0m\u001b[90m Float64   \u001b[0m\n",
       "─────┼─────────────────────────────────────────\n",
       "   1 │ Without controls  -0.0383447  0.015905\n",
       "   2 │ full reg          -0.0695532  0.0150005\n",
       "   3 │ partial reg       -0.0695532  0.0150005"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "DataFrame(modelos = [ \"Without controls\", \"full reg\", \"partial reg\" ], \n",
    "Estimate = [nocontrol_est,control_est, partial_est], \n",
    "StdError = [nocontrol_se1,control_se1, partial_se1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It it worth to notice that controlling for worker characteristics increases the gender wage gap from less that 4\\% to 7\\%. The controls we used in our analysis include 5 educational attainment indicators (less than high school graduates, high school graduates, some college, college graduate, and advanced degree), 4 region indicators (midwest, south, west, and northeast);  a quartic term (first, second, third, and fourth power) in experience and 22 occupation and 23 industry indicators.\n",
    "\n",
    "Keep in mind that the predictive effect (PE) does not only measures discrimination (causal effect of being female), it also may reflect\n",
    "selection effects of unobserved differences in covariates between men and women in our sample.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next we try \"extra\" flexible model, where we take interactions of all controls, giving us about 1000 controls."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### \"Extra\" flexible model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      " \u001b[90m [861a8166] \u001b[39m\u001b[92m+ Combinatorics v1.0.2\u001b[39m\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n",
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Project.toml`\n",
      " \u001b[90m [c8e1da08] \u001b[39m\u001b[92m+ IterTools v1.4.0\u001b[39m\n",
      "\u001b[32m\u001b[1m  No Changes\u001b[22m\u001b[39m to `C:\\Users\\Alexander\\.julia\\environments\\v1.7\\Manifest.toml`\n"
     ]
    }
   ],
   "source": [
    "import Pkg\n",
    "Pkg.add(\"StatsModels\")\n",
    "Pkg.add(\"Combinatorics\")\n",
    "Pkg.add(\"IterTools\")\n",
    "# we have to configure the package internaly with the itertools package, this because \n",
    "#julia dont iunderstand (a formula) ^2, it takes as an entire term not as interactions \n",
    "#between variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#this code fix the problem mencioned above\n",
    "using StatsModels, Combinatorics, IterTools\n",
    "\n",
    "combinations_upto(x, n) = Iterators.flatten(combinations(x, i) for i in 1:n)\n",
    "expand_exp(args, deg::ConstantTerm) =\n",
    "    tuple(((&)(terms...) for terms in combinations_upto(args, deg.n))...)\n",
    "\n",
    "StatsModels.apply_schema(t::FunctionTerm{typeof(^)}, sch::StatsModels.Schema, ctx::Type) =\n",
    "    apply_schema.(expand_exp(t.args_parsed...), Ref(sch), ctx)\n",
    "\n",
    "StatsModels.apply_schema(t::FunctionTerm{typeof(^)}, sch::StatsModels.FullRank, ctx::Type) =\n",
    "    apply_schema.(expand_exp(t.args_parsed...), Ref(sch), ctx)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Extra-Flex Controls: 979\n",
      "Coefficient for OLS with extra flex controls -0.061270463792332606\n"
     ]
    }
   ],
   "source": [
    "extra_flex = @formula(lwage ~  sex + (exp1+exp2+exp3+exp4+shs+hsg+scl+clg+occ2+ind2+mw+so+we)^2)\n",
    "\n",
    "control_fit = lm(extra_flex, data)\n",
    "control_est = GLM.coef(control_fit)[2]\n",
    "\n",
    "println(\"Number of Extra-Flex Controls: \", size(modelmatrix(control_fit))[2] -1) #minus the intercept\n",
    "println(\"Coefficient for OLS with extra flex controls \", control_est)\n",
    "\n",
    "#std error\n",
    "control_se = GLM.stderror(control_fit)[2];"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Cross-Validation in Lasso Regression - Manual Implementation Task**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "ename": "LoadError",
     "evalue": "The following package names could not be resolved:\n * StandardScaler (not found in project, manifest or registry)\n\u001b[36m   Suggestions:\u001b[39m \u001b[0m\u001b[1mS\u001b[22m\u001b[0m\u001b[1mt\u001b[22m\u001b[0m\u001b[1ma\u001b[22m\u001b[0m\u001b[1mn\u001b[22m\u001b[0m\u001b[1md\u001b[22m\u001b[0m\u001b[1ma\u001b[22m\u001b[0m\u001b[1mr\u001b[22m\u001b[0m\u001b[1md\u001b[22mizedRe\u001b[0m\u001b[1ms\u001b[22mtri\u001b[0m\u001b[1mc\u001b[22mtedBoltzm\u001b[0m\u001b[1ma\u001b[22mnnMachines",
     "output_type": "error",
     "traceback": [
      "The following package names could not be resolved:\n * StandardScaler (not found in project, manifest or registry)\n\u001b[36m   Suggestions:\u001b[39m \u001b[0m\u001b[1mS\u001b[22m\u001b[0m\u001b[1mt\u001b[22m\u001b[0m\u001b[1ma\u001b[22m\u001b[0m\u001b[1mn\u001b[22m\u001b[0m\u001b[1md\u001b[22m\u001b[0m\u001b[1ma\u001b[22m\u001b[0m\u001b[1mr\u001b[22m\u001b[0m\u001b[1md\u001b[22mizedRe\u001b[0m\u001b[1ms\u001b[22mtri\u001b[0m\u001b[1mc\u001b[22mtedBoltzm\u001b[0m\u001b[1ma\u001b[22mnnMachines",
      "",
      "Stacktrace:",
      " [1] pkgerror(msg::String)",
      "   @ Pkg.Types /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/Types.jl:70",
      " [2] ensure_resolved(ctx::Pkg.Types.Context, manifest::Pkg.Types.Manifest, pkgs::Vector{Pkg.Types.PackageSpec}; registry::Bool)",
      "   @ Pkg.Types /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/Types.jl:1030",
      " [3] ensure_resolved",
      "   @ /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/Types.jl:981 [inlined]",
      " [4] add(ctx::Pkg.Types.Context, pkgs::Vector{Pkg.Types.PackageSpec}; preserve::Pkg.Types.PreserveLevel, platform::Base.BinaryPlatforms.Platform, kwargs::@Kwargs{io::IJulia.IJuliaStdio{Base.PipeEndpoint}})",
      "   @ Pkg.API /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/API.jl:267",
      " [5] add(pkgs::Vector{Pkg.Types.PackageSpec}; io::IJulia.IJuliaStdio{Base.PipeEndpoint}, kwargs::@Kwargs{})",
      "   @ Pkg.API /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/API.jl:159",
      " [6] add(pkgs::Vector{Pkg.Types.PackageSpec})",
      "   @ Pkg.API /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/API.jl:148",
      " [7] add",
      "   @ /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/API.jl:147 [inlined]",
      " [8] add(pkg::String)",
      "   @ Pkg.API /Applications/Julia-1.10.app/Contents/Resources/julia/share/julia/stdlib/v1.10/Pkg/src/API.jl:146",
      " [9] top-level scope",
      "   @ In[94]:1"
     ]
    }
   ],
   "source": [
    "# import Pkg; Pkg.add(\"ScikitLearn\")\n",
    "# import Pkg; Pkg.add(\"StatsBase\")\n",
    "# import Pkg; Pkg.add(\"CSVFiles\")\n",
    "# import Pkg; Pkg.add(\"RDatasets\")\n",
    "# import Pkg; Pkg.add(\"MLJ\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[32m\u001b[1m   Resolving\u001b[22m\u001b[39m package versions...\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ShowCases ──────────── v0.1.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ContextVariablesX ──── v0.1.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Accessors ──────────── v0.1.36\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ZipFile ────────────── v0.9.4\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m HTML_Entities ──────── v1.0.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m TimerOutputs ───────── v0.5.23\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m NNlibCUDA ──────────── v0.2.6\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m NNlib ──────────────── v0.8.21\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Pidfile ────────────── v1.3.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Optimisers ─────────── v0.2.15\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m FuncPipelines ──────── v0.2.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m InitialValues ──────── v0.3.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m CEnum ──────────────── v0.4.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m FunctionWrappers ───── v1.1.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m BFloat16s ──────────── v0.2.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m GPUArrays ──────────── v8.8.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ZygoteRules ────────── v0.2.5\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m PrettyPrint ────────── v0.2.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m HuggingFaceApi ─────── v0.1.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Static ─────────────── v0.7.8\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m RandomNumbers ──────── v1.5.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Tricks ─────────────── v0.1.8\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m RealDot ────────────── v0.1.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m TupleTools ─────────── v1.5.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Fetch ──────────────── v0.1.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m IRTools ────────────── v0.4.12\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m LLVM ───────────────── v4.17.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m FLoopsBase ─────────── v0.1.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Functors ───────────── v0.3.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ProgressLogging ────── v0.1.4\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m IfElse ─────────────── v0.1.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m MicroCollections ───── v0.1.4\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Zygote ─────────────── v0.6.69\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m DoubleArrayTries ───── v0.0.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m StringEncodings ────── v0.3.7\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m DefineSingletons ───── v0.1.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m OneHotArrays ───────── v0.2.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m NameResolution ─────── v0.1.5\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m MLUtils ────────────── v0.3.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m UnsafeAtomicsLLVM ──── v0.1.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Random123 ──────────── v1.7.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m StringViews ────────── v1.3.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ValSplit ───────────── v0.1.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m BinaryProvider ─────── v0.5.10\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ChainRules ─────────── v1.63.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m CommonSubexpressions ─ v0.3.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m BytePairEncoding ───── v0.3.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m MLStyle ────────────── v0.4.17\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m BangBang ───────────── v0.3.37\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m FLoops ─────────────── v0.2.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ArgCheck ───────────── v2.3.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m DiffRules ──────────── v1.15.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m PrimitiveOneHot ────── v0.1.4\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m JSON3 ──────────────── v1.14.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m DataDeps ───────────── v0.7.8\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m DiffResults ────────── v1.1.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Flux ───────────────── v0.13.13\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m NeuralAttentionlib ─── v0.1.5\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m OhMyArtifacts ──────── v0.3.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m LLVMExtra_jll ──────── v0.0.18+0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m CompositionsBase ───── v0.1.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m KernelAbstractions ─── v0.9.18\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Strided ────────────── v1.2.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m StrTables ──────────── v1.0.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m AbstractTrees ──────── v0.4.5\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m PartialFunctions ───── v1.2.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m UnsafeAtomics ──────── v0.2.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m JuliaVariables ─────── v0.2.4\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m SparseInverseSubset ── v0.1.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m SimpleTraits ───────── v0.9.4\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m GPUArraysCore ──────── v0.1.5\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Adapt ──────────────── v3.7.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Atomix ─────────────── v0.1.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m StructWalk ─────────── v0.2.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m InternedStrings ────── v0.7.0\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Transducers ────────── v0.4.80\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Baselet ────────────── v0.1.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m GPUCompiler ────────── v0.17.3\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m FoldsThreads ───────── v0.1.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m StructArrays ───────── v0.6.18\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m ForwardDiff ────────── v0.10.36\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m SplittablesBase ────── v0.1.15\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m LightXML ───────────── v0.9.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m WordTokenizers ─────── v0.5.6\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Pickle ─────────────── v0.3.2\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m CUDA ───────────────── v3.13.1\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m TextEncodeBase ─────── v0.5.12\n",
      "\u001b[32m\u001b[1m   Installed\u001b[22m\u001b[39m Transformers ───────── v0.1.25\n",
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m `~/.julia/environments/v1.10/Project.toml`\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[21ca0261] \u001b[39m\u001b[92m+ Transformers v0.1.25\u001b[39m\n",
      "\u001b[32m\u001b[1m    Updating\u001b[22m\u001b[39m `~/.julia/environments/v1.10/Manifest.toml`\n",
      "  \u001b[90m[1520ce14] \u001b[39m\u001b[92m+ AbstractTrees v0.4.5\u001b[39m\n",
      "  \u001b[90m[7d9f7c33] \u001b[39m\u001b[92m+ Accessors v0.1.36\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[79e6a3ab] \u001b[39m\u001b[95m↓ Adapt v4.0.4 ⇒ v3.7.2\u001b[39m\n",
      "  \u001b[90m[dce04be8] \u001b[39m\u001b[92m+ ArgCheck v2.3.0\u001b[39m\n",
      "  \u001b[90m[a9b6321e] \u001b[39m\u001b[92m+ Atomix v0.1.0\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[ab4f0b2a] \u001b[39m\u001b[92m+ BFloat16s v0.2.0\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[198e06fe] \u001b[39m\u001b[92m+ BangBang v0.3.37\u001b[39m\n",
      "  \u001b[90m[9718e550] \u001b[39m\u001b[92m+ Baselet v0.1.1\u001b[39m\n",
      "  \u001b[90m[b99e7846] \u001b[39m\u001b[92m+ BinaryProvider v0.5.10\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[a4280ba5] \u001b[39m\u001b[92m+ BytePairEncoding v0.3.1\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[fa961155] \u001b[39m\u001b[92m+ CEnum v0.4.2\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[052768ef] \u001b[39m\u001b[92m+ CUDA v3.13.1\u001b[39m\n",
      "  \u001b[90m[082447d4] \u001b[39m\u001b[92m+ ChainRules v1.63.0\u001b[39m\n",
      "  \u001b[90m[bbf7d656] \u001b[39m\u001b[92m+ CommonSubexpressions v0.3.0\u001b[39m\n",
      "  \u001b[90m[a33af91c] \u001b[39m\u001b[92m+ CompositionsBase v0.1.2\u001b[39m\n",
      "  \u001b[90m[6add18c4] \u001b[39m\u001b[92m+ ContextVariablesX v0.1.3\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[124859b0] \u001b[39m\u001b[92m+ DataDeps v0.7.8\u001b[39m\n",
      "  \u001b[90m[244e2a9f] \u001b[39m\u001b[92m+ DefineSingletons v0.1.2\u001b[39m\n",
      "  \u001b[90m[163ba53b] \u001b[39m\u001b[92m+ DiffResults v1.1.0\u001b[39m\n",
      "  \u001b[90m[b552c78f] \u001b[39m\u001b[92m+ DiffRules v1.15.1\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[abbaa0e5] \u001b[39m\u001b[92m+ DoubleArrayTries v0.0.3\u001b[39m\n",
      "  \u001b[90m[cc61a311] \u001b[39m\u001b[92m+ FLoops v0.2.1\u001b[39m\n",
      "  \u001b[90m[b9860ae5] \u001b[39m\u001b[92m+ FLoopsBase v0.1.1\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[bb354801] \u001b[39m\u001b[92m+ Fetch v0.1.3\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[587475ba] \u001b[39m\u001b[92m+ Flux v0.13.13\u001b[39m\n",
      "  \u001b[90m[9c68100b] \u001b[39m\u001b[92m+ FoldsThreads v0.1.2\u001b[39m\n",
      "  \u001b[90m[f6369f11] \u001b[39m\u001b[92m+ ForwardDiff v0.10.36\u001b[39m\n",
      "  \u001b[90m[9ed96fbb] \u001b[39m\u001b[92m+ FuncPipelines v0.2.3\u001b[39m\n",
      "  \u001b[90m[069b7b12] \u001b[39m\u001b[92m+ FunctionWrappers v1.1.3\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[d9f16b24] \u001b[39m\u001b[92m+ Functors v0.3.0\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[0c68f7d7] \u001b[39m\u001b[92m+ GPUArrays v8.8.1\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[46192b85] \u001b[39m\u001b[92m+ GPUArraysCore v0.1.5\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[61eb1bfa] \u001b[39m\u001b[92m+ GPUCompiler v0.17.3\u001b[39m\n",
      "  \u001b[90m[7693890a] \u001b[39m\u001b[92m+ HTML_Entities v1.0.1\u001b[39m\n",
      "  \u001b[90m[3cc741c3] \u001b[39m\u001b[92m+ HuggingFaceApi v0.1.0\u001b[39m\n",
      "  \u001b[90m[7869d1d1] \u001b[39m\u001b[92m+ IRTools v0.4.12\u001b[39m\n",
      "  \u001b[90m[615f187c] \u001b[39m\u001b[92m+ IfElse v0.1.1\u001b[39m\n",
      "  \u001b[90m[22cec73e] \u001b[39m\u001b[92m+ InitialValues v0.3.1\u001b[39m\n",
      "  \u001b[90m[7d512f48] \u001b[39m\u001b[92m+ InternedStrings v0.7.0\u001b[39m\n",
      "  \u001b[90m[0f8b85d8] \u001b[39m\u001b[92m+ JSON3 v1.14.0\u001b[39m\n",
      "  \u001b[90m[b14d175d] \u001b[39m\u001b[92m+ JuliaVariables v0.2.4\u001b[39m\n",
      "  \u001b[90m[63c18a36] \u001b[39m\u001b[92m+ KernelAbstractions v0.9.18\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[929cbde3] \u001b[39m\u001b[92m+ LLVM v4.17.1\u001b[39m\n",
      "  \u001b[90m[9c8b4983] \u001b[39m\u001b[92m+ LightXML v0.9.1\u001b[39m\n",
      "  \u001b[90m[d8e11817] \u001b[39m\u001b[92m+ MLStyle v0.4.17\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[f1d291b0] \u001b[39m\u001b[92m+ MLUtils v0.3.1\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[128add7d] \u001b[39m\u001b[92m+ MicroCollections v0.1.4\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[872c559c] \u001b[39m\u001b[92m+ NNlib v0.8.21\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[a00861dc] \u001b[39m\u001b[92m+ NNlibCUDA v0.2.6\u001b[39m\n",
      "  \u001b[90m[71a1bf82] \u001b[39m\u001b[92m+ NameResolution v0.1.5\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[12afc1b8] \u001b[39m\u001b[92m+ NeuralAttentionlib v0.1.5\u001b[39m\n",
      "  \u001b[90m[cf8be1f4] \u001b[39m\u001b[92m+ OhMyArtifacts v0.3.1\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[0b1bfda6] \u001b[39m\u001b[92m+ OneHotArrays v0.2.0\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[3bd65402] \u001b[39m\u001b[92m+ Optimisers v0.2.15\u001b[39m\n",
      "  \u001b[90m[570af359] \u001b[39m\u001b[92m+ PartialFunctions v1.2.0\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[fbb45041] \u001b[39m\u001b[92m+ Pickle v0.3.2\u001b[39m\n",
      "  \u001b[90m[fa939f87] \u001b[39m\u001b[92m+ Pidfile v1.3.0\u001b[39m\n",
      "  \u001b[90m[8162dcfd] \u001b[39m\u001b[92m+ PrettyPrint v0.2.0\u001b[39m\n",
      "  \u001b[90m[13d12f88] \u001b[39m\u001b[92m+ PrimitiveOneHot v0.1.4\u001b[39m\n",
      "  \u001b[90m[33c8b6b6] \u001b[39m\u001b[92m+ ProgressLogging v0.1.4\u001b[39m\n",
      "  \u001b[90m[74087812] \u001b[39m\u001b[92m+ Random123 v1.7.0\u001b[39m\n",
      "  \u001b[90m[e6cf234a] \u001b[39m\u001b[92m+ RandomNumbers v1.5.3\u001b[39m\n",
      "  \u001b[90m[c1ae055f] \u001b[39m\u001b[92m+ RealDot v0.1.0\u001b[39m\n",
      "  \u001b[90m[605ecd9f] \u001b[39m\u001b[92m+ ShowCases v0.1.0\u001b[39m\n",
      "  \u001b[90m[699a6c99] \u001b[39m\u001b[92m+ SimpleTraits v0.9.4\u001b[39m\n",
      "  \u001b[90m[dc90abb0] \u001b[39m\u001b[92m+ SparseInverseSubset v0.1.2\u001b[39m\n",
      "  \u001b[90m[171d559e] \u001b[39m\u001b[92m+ SplittablesBase v0.1.15\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[aedffcd0] \u001b[39m\u001b[92m+ Static v0.7.8\u001b[39m\n",
      "  \u001b[90m[9700d1a9] \u001b[39m\u001b[92m+ StrTables v1.0.1\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[5e0ebb24] \u001b[39m\u001b[92m+ Strided v1.2.3\u001b[39m\n",
      "  \u001b[90m[69024149] \u001b[39m\u001b[92m+ StringEncodings v0.3.7\u001b[39m\n",
      "  \u001b[90m[354b36f9] \u001b[39m\u001b[92m+ StringViews v1.3.3\u001b[39m\n",
      "  \u001b[90m[09ab397b] \u001b[39m\u001b[92m+ StructArrays v0.6.18\u001b[39m\n",
      "  \u001b[90m[31cdf514] \u001b[39m\u001b[92m+ StructWalk v0.2.1\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[f92c20c0] \u001b[39m\u001b[92m+ TextEncodeBase v0.5.12\u001b[39m\n",
      "  \u001b[90m[a759f4b9] \u001b[39m\u001b[92m+ TimerOutputs v0.5.23\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[28d57a85] \u001b[39m\u001b[92m+ Transducers v0.4.80\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[21ca0261] \u001b[39m\u001b[92m+ Transformers v0.1.25\u001b[39m\n",
      "  \u001b[90m[410a4b4d] \u001b[39m\u001b[92m+ Tricks v0.1.8\u001b[39m\n",
      "  \u001b[90m[9d95972d] \u001b[39m\u001b[92m+ TupleTools v1.5.0\u001b[39m\n",
      "  \u001b[90m[013be700] \u001b[39m\u001b[92m+ UnsafeAtomics v0.2.1\u001b[39m\n",
      "\u001b[32m⌃\u001b[39m \u001b[90m[d80eeb9a] \u001b[39m\u001b[92m+ UnsafeAtomicsLLVM v0.1.1\u001b[39m\n",
      "  \u001b[90m[0625e100] \u001b[39m\u001b[92m+ ValSplit v0.1.1\u001b[39m\n",
      "  \u001b[90m[796a5d58] \u001b[39m\u001b[92m+ WordTokenizers v0.5.6\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[a5390f91] \u001b[39m\u001b[92m+ ZipFile v0.9.4\u001b[39m\n",
      "  \u001b[90m[e88e6eb3] \u001b[39m\u001b[92m+ Zygote v0.6.69\u001b[39m\n",
      "  \u001b[90m[700de1a5] \u001b[39m\u001b[92m+ ZygoteRules v0.2.5\u001b[39m\n",
      "\u001b[33m⌅\u001b[39m \u001b[90m[dad2f222] \u001b[39m\u001b[92m+ LLVMExtra_jll v0.0.18+0\u001b[39m\n",
      "\u001b[36m\u001b[1m        Info\u001b[22m\u001b[39m Packages marked with \u001b[32m⌃\u001b[39m and \u001b[33m⌅\u001b[39m have new versions available. Those with \u001b[32m⌃\u001b[39m may be upgradable, but those with \u001b[33m⌅\u001b[39m are restricted by compatibility constraints from upgrading. To see why use `status --outdated -m`\n",
      "\u001b[32m\u001b[1m    Building\u001b[22m\u001b[39m DataDeps ─────→ `~/.julia/scratchspaces/44cfe95a-1eb2-52ea-b672-e2afdf69b78f/e299d8267135ef2f9c941a764006697082c1e7e8/build.log`\n",
      "\u001b[32m\u001b[1m    Building\u001b[22m\u001b[39m HTML_Entities → `~/.julia/scratchspaces/44cfe95a-1eb2-52ea-b672-e2afdf69b78f/c4144ed3bc5f67f595622ad03c0e39fa6c70ccc7/build.log`\n",
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m project...\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mTricks\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStringViews\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFunctionWrappers\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mInitialValues\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mCEnum\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStrTables\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mPrettyPrint\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFuncPipelines\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mArgCheck\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mUnsafeAtomics\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mShowCases\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mRealDot\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mInternedStrings\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mPidfile\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mCompositionsBase\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mBFloat16s\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAbstractTrees\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mDefineSingletons\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mIfElse\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAdapt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mProgressLogging\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mIRTools\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFunctors\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mTupleTools\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mTimerOutputs\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mSimpleTraits\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mCommonSubexpressions\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mBaselet\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mPartialFunctions\u001b[39m\n",
      "\u001b[91m  ✗ \u001b[39m\u001b[90mBinaryProvider\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mZipFile\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mSparseInverseSubset\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mRandomNumbers\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mDiffResults\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mLLVMExtra_jll\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mContextVariablesX\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStringEncodings\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStructWalk\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mLightXML\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStructArrays\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mSplittablesBase\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mDiffRules\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mZygoteRules\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mValSplit\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mHTML_Entities\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mNameResolution\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAtomix\u001b[39m\n",
      "\u001b[33m  ? \u001b[39mLathe\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mOhMyArtifacts\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mCompositionsBase → CompositionsBaseInverseFunctionsExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStatic\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mOffsetArrays → OffsetArraysAdaptExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAdapt → AdaptStaticArraysExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStrided\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mDataDeps\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mOptimisers\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFLoopsBase\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mRandom123\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mJSON3\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mBangBang\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAccessors\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mGPUArraysCore\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mDoubleArrayTries\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mForwardDiff\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mLLVM\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mMLStyle\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mWordTokenizers\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mInterpolations\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mPickle\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mHuggingFaceApi\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFetch\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAccessors → AccessorsStructArraysExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mMicroCollections\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStructArrays → StructArraysGPUArraysCoreExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mUnsafeAtomicsLLVM\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mForwardDiff → ForwardDiffStaticArraysExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mGPUArrays\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAccessors → AccessorsStaticArraysExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mInterpolations → InterpolationsUnitfulExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStructArrays → StructArraysStaticArraysExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mJuliaVariables\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mAccessors → AccessorsUnitfulExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStructArrays → StructArraysSparseArraysExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mStructArrays → StructArraysAdaptExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mKernelDensity\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mTransducers\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mKernelAbstractions\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mTransducers → TransducersDataFramesExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFoldsThreads\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mNNlib\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFLoops\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mChainRules\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mPrimitiveOneHot\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mTextEncodeBase\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mGPUCompiler\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mMLUtils\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mBytePairEncoding\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mOneHotArrays\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mZygote\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mZygote → ZygoteDistancesExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mZygote → ZygoteColorsExt\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mCUDA\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mNNlibCUDA\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mNeuralAttentionlib\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39m\u001b[90mFlux\u001b[39m\n",
      "\u001b[32m  ✓ \u001b[39mTransformers\n",
      "\u001b[32m  ✓ \u001b[39mStatsPlots\n",
      "  105 dependencies successfully precompiled in 123 seconds. 279 already precompiled.\n",
      "  \u001b[33m1\u001b[39m dependency failed but may be precompilable after restarting julia\n",
      "  \u001b[33m2\u001b[39m dependencies had output during precompilation:\u001b[33m\n",
      "┌ \u001b[39mBFloat16s\u001b[33m\n",
      "│  \u001b[39mWARNING: could not import Printf.ini_hex into BFloat16s\u001b[33m\n",
      "│  \u001b[39mWARNING: could not import Printf.ini_HEX into BFloat16s\u001b[33m\n",
      "└  \u001b[39m\u001b[33m\n",
      "┌ \u001b[39mLathe\u001b[33m\n",
      "│  \u001b[39mWARNING: Method definition PowerLog(Float64, Float64) in module models at /Users/valerie/.julia/packages/Lathe/ZRJQf/src/models/toolbox.jl:14 overwritten on the same line (check for duplicate calls to `include`).\u001b[33m\n",
      "│  \u001b[39mERROR: Method overwriting is not permitted during Module precompilation. Use `__precompile__(false)` to opt-out of precompilation.\u001b[33m\n",
      "└  \u001b[39m\n"
     ]
    }
   ],
   "source": [
    "using Pkg\n",
    "Pkg.add(\"Transformers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m Transformers\n",
      "\u001b[91m  ✗ \u001b[39m\u001b[90mBinaryProvider\u001b[39m\n",
      "  0 dependencies successfully precompiled in 2 seconds. 183 already precompiled.\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling Transformers [21ca0261-441d-5938-ace7-c90938fde4d4]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule HTTP with build ID fafbfcfd-fb7e-58a8-0000-0286b56ffd08 is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean HTTP [cd3eb016-35fb-5094-929b-558a96fad6f3] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing Transformers [21ca0261-441d-5938-ace7-c90938fde4d4].\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling ZygoteColorsExt [e68c091a-8ea5-5ca7-be4f-380657d4ad79]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule Colors with build ID fafbfcfd-6f69-f41e-0000-2644de38854d is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean Colors [5ae59095-9a9b-59fe-a467-6f913c188581] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing ZygoteColorsExt [e68c091a-8ea5-5ca7-be4f-380657d4ad79].\n",
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m TextEncodeBase\n",
      "\u001b[91m  ✗ \u001b[39m\u001b[90mBinaryProvider\u001b[39m\n",
      "  0 dependencies successfully precompiled in 3 seconds. 47 already precompiled.\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling TextEncodeBase [f92c20c0-9f2a-4705-8116-881385faba05]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule HTTP with build ID fafbfcfd-fb7e-58a8-0000-0286b56ffd08 is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean HTTP [cd3eb016-35fb-5094-929b-558a96fad6f3] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing TextEncodeBase [f92c20c0-9f2a-4705-8116-881385faba05].\n",
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m WordTokenizers\n",
      "\u001b[91m  ✗ \u001b[39m\u001b[90mBinaryProvider\u001b[39m\n",
      "  0 dependencies successfully precompiled in 1 seconds. 9 already precompiled.\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling WordTokenizers [796a5d58-b03d-544a-977e-18100b691f6e]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule HTTP with build ID fafbfcfd-fb7e-58a8-0000-0286b56ffd08 is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean HTTP [cd3eb016-35fb-5094-929b-558a96fad6f3] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing WordTokenizers [796a5d58-b03d-544a-977e-18100b691f6e].\n",
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m DataDeps\n",
      "\u001b[91m  ✗ \u001b[39m\u001b[90mBinaryProvider\u001b[39m\n",
      "  0 dependencies successfully precompiled in 27 seconds. 6 already precompiled.\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling DataDeps [124859b0-ceae-595e-8997-d05f6a7a8dfe]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule HTTP with build ID fafbfcfd-fb7e-58a8-0000-0286b56ffd08 is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean HTTP [cd3eb016-35fb-5094-929b-558a96fad6f3] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing DataDeps [124859b0-ceae-595e-8997-d05f6a7a8dfe].\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling Fetch [bb354801-46f6-40b6-9c3d-d42d7a74c775]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule HTTP with build ID fafbfcfd-fb7e-58a8-0000-0286b56ffd08 is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean HTTP [cd3eb016-35fb-5094-929b-558a96fad6f3] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing Fetch [bb354801-46f6-40b6-9c3d-d42d7a74c775].\n",
      "\u001b[32m\u001b[1mPrecompiling\u001b[22m\u001b[39m BytePairEncoding\n",
      "\u001b[91m  ✗ \u001b[39m\u001b[90mBinaryProvider\u001b[39m\n",
      "  0 dependencies successfully precompiled in 1 seconds. 48 already precompiled.\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mPrecompiling BytePairEncoding [a4280ba5-8788-555a-8ca8-4a8c3d966a71]\n",
      "\u001b[33m\u001b[1m┌ \u001b[22m\u001b[39m\u001b[33m\u001b[1mWarning: \u001b[22m\u001b[39mModule TextEncodeBase with build ID ffffffff-ffff-ffff-0000-2ecbcb9e8568 is missing from the cache.\n",
      "\u001b[33m\u001b[1m│ \u001b[22m\u001b[39mThis may mean TextEncodeBase [f92c20c0-9f2a-4705-8116-881385faba05] does not support precompilation but is imported by a module that does.\n",
      "\u001b[33m\u001b[1m└ \u001b[22m\u001b[39m\u001b[90m@ Base loading.jl:1948\u001b[39m\n",
      "\u001b[36m\u001b[1m[ \u001b[22m\u001b[39m\u001b[36m\u001b[1mInfo: \u001b[22m\u001b[39mSkipping precompilation since __precompile__(false). Importing BytePairEncoding [a4280ba5-8788-555a-8ca8-4a8c3d966a71].\n",
      "WARNING: could not import ScikitLearn.cross_val_score into Main\n"
     ]
    }
   ],
   "source": [
    "using Pkg\n",
    "using RData\n",
    "using DataFrames\n",
    "using RDatasets\n",
    "using Random\n",
    "using StatsBase\n",
    "using GLM\n",
    "using PyCall\n",
    "using Statistics\n",
    "using Plots\n",
    "using CSV\n",
    "using Transformers\n",
    "\n",
    "import PyPlot\n",
    "import DataFrames\n",
    "import StatsModels\n",
    "import Random\n",
    "import ScikitLearn: cross_val_score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Data Preparation**\n",
    "\n",
    "Load the March Supplement of the U.S. Current Population Survey, year 2015. (wage2015_subsample_inference.Rdata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20-element Vector{String}:\n",
       " \"wage\"\n",
       " \"lwage\"\n",
       " \"sex\"\n",
       " \"shs\"\n",
       " \"hsg\"\n",
       " \"scl\"\n",
       " \"clg\"\n",
       " \"ad\"\n",
       " \"mw\"\n",
       " \"so\"\n",
       " \"we\"\n",
       " \"ne\"\n",
       " \"exp1\"\n",
       " \"exp2\"\n",
       " \"exp3\"\n",
       " \"exp4\"\n",
       " \"occ\"\n",
       " \"occ2\"\n",
       " \"ind\"\n",
       " \"ind2\""
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rdata_read = RData.load(\"../../data/wage2015_subsample_inference.RData\")\n",
    "data = rdata_read[\"data\"]\n",
    "names(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"data-frame\"><thead><tr><th></th><th>variable</th><th>mean</th><th>min</th><th>median</th><th>max</th><th>nmissing</th><th>eltype</th></tr><tr><th></th><th>Symbol</th><th>Union…</th><th>Any</th><th>Union…</th><th>Any</th><th>Int64</th><th>DataType</th></tr></thead><tbody><p>20 rows × 7 columns</p><tr><th>1</th><td>wage</td><td>23.4104</td><td>3.02198</td><td>19.2308</td><td>528.846</td><td>0</td><td>Float64</td></tr><tr><th>2</th><td>lwage</td><td>2.97079</td><td>1.10591</td><td>2.95651</td><td>6.2707</td><td>0</td><td>Float64</td></tr><tr><th>3</th><td>sex</td><td>0.444466</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>4</th><td>shs</td><td>0.023301</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>5</th><td>hsg</td><td>0.243883</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>6</th><td>scl</td><td>0.278058</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>7</th><td>clg</td><td>0.31767</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>8</th><td>ad</td><td>0.137087</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>9</th><td>mw</td><td>0.259612</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>10</th><td>so</td><td>0.296505</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>11</th><td>we</td><td>0.216117</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>12</th><td>ne</td><td>0.227767</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0</td><td>Float64</td></tr><tr><th>13</th><td>exp1</td><td>13.7606</td><td>0.0</td><td>10.0</td><td>47.0</td><td>0</td><td>Float64</td></tr><tr><th>14</th><td>exp2</td><td>3.01893</td><td>0.0</td><td>1.0</td><td>22.09</td><td>0</td><td>Float64</td></tr><tr><th>15</th><td>exp3</td><td>8.23587</td><td>0.0</td><td>1.0</td><td>103.823</td><td>0</td><td>Float64</td></tr><tr><th>16</th><td>exp4</td><td>25.118</td><td>0.0</td><td>1.0</td><td>487.968</td><td>0</td><td>Float64</td></tr><tr><th>17</th><td>occ</td><td></td><td>10</td><td></td><td>1e+05</td><td>0</td><td>CategoricalValue{String, UInt16}</td></tr><tr><th>18</th><td>occ2</td><td></td><td>1</td><td></td><td>22</td><td>0</td><td>CategoricalValue{String, UInt8}</td></tr><tr><th>19</th><td>ind</td><td></td><td>370</td><td></td><td>1e+05</td><td>0</td><td>CategoricalValue{String, UInt8}</td></tr><tr><th>20</th><td>ind2</td><td></td><td>2</td><td></td><td>22</td><td>0</td><td>CategoricalValue{String, UInt8}</td></tr></tbody></table>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccccccc}\n",
       "\t& variable & mean & min & median & max & nmissing & eltype\\\\\n",
       "\t\\hline\n",
       "\t& Symbol & Union… & Any & Union… & Any & Int64 & DataType\\\\\n",
       "\t\\hline\n",
       "\t1 & wage & 23.4104 & 3.02198 & 19.2308 & 528.846 & 0 & Float64 \\\\\n",
       "\t2 & lwage & 2.97079 & 1.10591 & 2.95651 & 6.2707 & 0 & Float64 \\\\\n",
       "\t3 & sex & 0.444466 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t4 & shs & 0.023301 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t5 & hsg & 0.243883 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t6 & scl & 0.278058 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t7 & clg & 0.31767 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t8 & ad & 0.137087 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t9 & mw & 0.259612 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t10 & so & 0.296505 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t11 & we & 0.216117 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t12 & ne & 0.227767 & 0.0 & 0.0 & 1.0 & 0 & Float64 \\\\\n",
       "\t13 & exp1 & 13.7606 & 0.0 & 10.0 & 47.0 & 0 & Float64 \\\\\n",
       "\t14 & exp2 & 3.01893 & 0.0 & 1.0 & 22.09 & 0 & Float64 \\\\\n",
       "\t15 & exp3 & 8.23587 & 0.0 & 1.0 & 103.823 & 0 & Float64 \\\\\n",
       "\t16 & exp4 & 25.118 & 0.0 & 1.0 & 487.968 & 0 & Float64 \\\\\n",
       "\t17 & occ &  & 10 &  & 1e+05 & 0 & CategoricalValue\\{String, UInt16\\} \\\\\n",
       "\t18 & occ2 &  & 1 &  & 22 & 0 & CategoricalValue\\{String, UInt8\\} \\\\\n",
       "\t19 & ind &  & 370 &  & 1e+05 & 0 & CategoricalValue\\{String, UInt8\\} \\\\\n",
       "\t20 & ind2 &  & 2 &  & 22 & 0 & CategoricalValue\\{String, UInt8\\} \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m20×7 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m variable \u001b[0m\u001b[1m mean     \u001b[0m\u001b[1m min     \u001b[0m\u001b[1m median  \u001b[0m\u001b[1m max     \u001b[0m\u001b[1m nmissing \u001b[0m\u001b[1m eltype        \u001b[0m ⋯\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Symbol   \u001b[0m\u001b[90m Union…   \u001b[0m\u001b[90m Any     \u001b[0m\u001b[90m Union…  \u001b[0m\u001b[90m Any     \u001b[0m\u001b[90m Int64    \u001b[0m\u001b[90m DataType      \u001b[0m ⋯\n",
       "─────┼──────────────────────────────────────────────────────────────────────────\n",
       "   1 │ wage      23.4104   3.02198  19.2308  528.846         0  Float64        ⋯\n",
       "   2 │ lwage     2.97079   1.10591  2.95651  6.2707          0  Float64\n",
       "   3 │ sex       0.444466  0.0      0.0      1.0             0  Float64\n",
       "   4 │ shs       0.023301  0.0      0.0      1.0             0  Float64\n",
       "   5 │ hsg       0.243883  0.0      0.0      1.0             0  Float64        ⋯\n",
       "   6 │ scl       0.278058  0.0      0.0      1.0             0  Float64\n",
       "   7 │ clg       0.31767   0.0      0.0      1.0             0  Float64\n",
       "   8 │ ad        0.137087  0.0      0.0      1.0             0  Float64\n",
       "   9 │ mw        0.259612  0.0      0.0      1.0             0  Float64        ⋯\n",
       "  10 │ so        0.296505  0.0      0.0      1.0             0  Float64\n",
       "  11 │ we        0.216117  0.0      0.0      1.0             0  Float64\n",
       "  12 │ ne        0.227767  0.0      0.0      1.0             0  Float64\n",
       "  13 │ exp1      13.7606   0.0      10.0     47.0            0  Float64        ⋯\n",
       "  14 │ exp2      3.01893   0.0      1.0      22.09           0  Float64\n",
       "  15 │ exp3      8.23587   0.0      1.0      103.823         0  Float64\n",
       "  16 │ exp4      25.118    0.0      1.0      487.968         0  Float64\n",
       "  17 │ occ      \u001b[90m          \u001b[0m 10      \u001b[90m         \u001b[0m 1e+05           0  CategoricalVal ⋯\n",
       "  18 │ occ2     \u001b[90m          \u001b[0m 1       \u001b[90m         \u001b[0m 22              0  CategoricalVal\n",
       "  19 │ ind      \u001b[90m          \u001b[0m 370     \u001b[90m         \u001b[0m 1e+05           0  CategoricalVal\n",
       "  20 │ ind2     \u001b[90m          \u001b[0m 2       \u001b[90m         \u001b[0m 22              0  CategoricalVal\n",
       "\u001b[36m                                                                1 column omitted\u001b[0m"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# a quick description of the data\n",
    "describe(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "# flexible model\n",
    "# flex = @formula(lwage ~ sex + shs + hsg + scl + clg + occ2 + ind2 + mw + so + we + (exp1 + exp2 + exp3 + exp4) * (shs + hsg + scl + clg + occ2 + ind2 + mw + so + we))\n",
    "# flex_results_0 = lm(flex, data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Get exogenous variables (X matrix) from the flexible model\n",
    "# X = Matrix(modelmatrix(flex_results_0))\n",
    "\n",
    "# # Set endogenous variable (response variable)\n",
    "# y = data[!, \"lwage\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(\u001b[1m105×5 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m SepalLength \u001b[0m\u001b[1m SepalWidth \u001b[0m\u001b[1m PetalLength \u001b[0m\u001b[1m PetalWidth \u001b[0m\u001b[1m Species    \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Float64     \u001b[0m\u001b[90m Float64    \u001b[0m\u001b[90m Float64     \u001b[0m\u001b[90m Float64    \u001b[0m\u001b[90m Cat…       \u001b[0m\n",
       "─────┼──────────────────────────────────────────────────────────────\n",
       "   1 │         6.1         3.0          4.9         1.8  virginica\n",
       "   2 │         5.5         2.6          4.4         1.2  versicolor\n",
       "   3 │         5.6         2.7          4.2         1.3  versicolor\n",
       "   4 │         5.3         3.7          1.5         0.2  setosa\n",
       "   5 │         6.2         2.2          4.5         1.5  versicolor\n",
       "   6 │         7.7         3.8          6.7         2.2  virginica\n",
       "   7 │         6.5         2.8          4.6         1.5  versicolor\n",
       "   8 │         6.6         2.9          4.6         1.3  versicolor\n",
       "   9 │         5.5         3.5          1.3         0.2  setosa\n",
       "  10 │         6.0         2.9          4.5         1.5  versicolor\n",
       "  11 │         5.5         2.3          4.0         1.3  versicolor\n",
       "  ⋮  │      ⋮           ⋮            ⋮           ⋮           ⋮\n",
       "  96 │         5.8         2.7          5.1         1.9  virginica\n",
       "  97 │         7.6         3.0          6.6         2.1  virginica\n",
       "  98 │         6.5         3.0          5.5         1.8  virginica\n",
       "  99 │         6.7         3.1          4.4         1.4  versicolor\n",
       " 100 │         5.6         2.9          3.6         1.3  versicolor\n",
       " 101 │         6.8         3.0          5.5         2.1  virginica\n",
       " 102 │         6.1         3.0          4.6         1.4  versicolor\n",
       " 103 │         5.2         3.4          1.4         0.2  setosa\n",
       " 104 │         6.5         3.0          5.8         2.2  virginica\n",
       " 105 │         6.2         2.8          4.8         1.8  virginica\n",
       "\u001b[36m                                                     84 rows omitted\u001b[0m, \u001b[1m45×5 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m SepalLength \u001b[0m\u001b[1m SepalWidth \u001b[0m\u001b[1m PetalLength \u001b[0m\u001b[1m PetalWidth \u001b[0m\u001b[1m Species    \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Float64     \u001b[0m\u001b[90m Float64    \u001b[0m\u001b[90m Float64     \u001b[0m\u001b[90m Float64    \u001b[0m\u001b[90m Cat…       \u001b[0m\n",
       "─────┼──────────────────────────────────────────────────────────────\n",
       "   1 │         6.1         2.8          4.7         1.2  versicolor\n",
       "   2 │         5.0         3.0          1.6         0.2  setosa\n",
       "   3 │         6.3         2.3          4.4         1.3  versicolor\n",
       "   4 │         4.4         3.0          1.3         0.2  setosa\n",
       "   5 │         4.6         3.2          1.4         0.2  setosa\n",
       "   6 │         5.0         3.2          1.2         0.2  setosa\n",
       "   7 │         6.7         3.0          5.2         2.3  virginica\n",
       "   8 │         5.1         3.8          1.9         0.4  setosa\n",
       "   9 │         4.8         3.0          1.4         0.1  setosa\n",
       "  10 │         5.2         3.5          1.5         0.2  setosa\n",
       "  11 │         5.1         3.8          1.6         0.2  setosa\n",
       "  ⋮  │      ⋮           ⋮            ⋮           ⋮           ⋮\n",
       "  36 │         5.7         3.8          1.7         0.3  setosa\n",
       "  37 │         5.6         3.0          4.5         1.5  versicolor\n",
       "  38 │         6.3         2.5          5.0         1.9  virginica\n",
       "  39 │         4.8         3.1          1.6         0.2  setosa\n",
       "  40 │         6.0         3.4          4.5         1.6  versicolor\n",
       "  41 │         4.8         3.4          1.6         0.2  setosa\n",
       "  42 │         6.7         3.0          5.0         1.7  versicolor\n",
       "  43 │         5.9         3.0          5.1         1.8  virginica\n",
       "  44 │         5.0         3.5          1.6         0.6  setosa\n",
       "  45 │         6.3         3.4          5.6         2.4  virginica\n",
       "\u001b[36m                                                     24 rows omitted\u001b[0m)"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "function partitionTrainTest(data, at = 0.7)\n",
    "    n = nrow(data)\n",
    "    idx = shuffle(1:n)\n",
    "    train_idx = view(idx, 1:floor(Int, at*n))\n",
    "    test_idx = view(idx, (floor(Int, at*n)+1):n)\n",
    "    data[train_idx,:], data[test_idx,:]\n",
    "end\n",
    "\n",
    "iris = dataset(\"datasets\", \"iris\")\n",
    "X_train,X_test = partitionTrainTest(iris, 0.7) # 70% train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "ename": "LoadError",
     "evalue": "UndefVarError: `StandardScaler` not defined",
     "output_type": "error",
     "traceback": [
      "UndefVarError: `StandardScaler` not defined",
      "",
      "Stacktrace:",
      " [1] top-level scope",
      "   @ In[102]:1"
     ]
    }
   ],
   "source": [
    "scaler = StandardScaler()\n",
    "\n",
    "# Fit and transform on training data\n",
    "X_train = MLJ.transform(scaler, X_train)\n",
    "\n",
    "# Transform test data using the same scaler\n",
    "X_test = MLJ.transform(scaler, X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Define a Range of Alpha (Lambda in our equation) Values**\n",
    "\n",
    "We create a list or array of alpha values to iterate over. These will be the different regularization parameters we test. We started testing from 0.1 to 0.5 and found that the MSE in cross-validation was reducing when the alpha value was incrementing. Therefore, we tried with higher values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create alphas using a loop\n",
    "alphas = [45 + i * 5 for i in 0:4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**3. Partition the Dataset for k-Fold Cross-Validation**\n",
    "\n",
    "We divide the dataset into 5 subsets (or folds). Since we are working with a regression task (predicting the log of wage), we use the K-Fold cross-validator from sklearn. We ensure the data is shuffled by adding 'shuffle=True' and set a random state for a reproducible output.\n",
    "\n",
    "Source: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create KFold\n",
    "kf = KFold(n_splits = 5, shuffle = true, random_state = 24)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**4. Lasso Regression Implementation**\n",
    "\n",
    "Implement a function to fit a Lasso Regression model given a training dataset and an alpha value. The function should return the model's coefficients and intercept."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "function lasso_regression(X_train, y_train, alpha, iterations=100, learning_rate=0.01)\n",
    "    \"\"\"\n",
    "    Fits a Lasso Regression model\n",
    "\n",
    "    Args:\n",
    "        X_train: Training features\n",
    "        y_train: Target values\n",
    "        alpha: Regularization parameter (L1 penalty)\n",
    "        iterations: Number of iterations for gradient descent (default: 100)\n",
    "        learning_rate: Learning rate for gradient descent (default: 0.01)\n",
    "\n",
    "    Returns:\n",
    "        W: Model coefficients (weights)\n",
    "        b: Model intercept (bias)\n",
    "    \"\"\"\n",
    "    m, n = size(X_train)\n",
    "    W = zeros(n)\n",
    "    b = 0.0\n",
    "\n",
    "    for _ in 1:iterations\n",
    "        Y_pred = X_train * W .+ b\n",
    "        dW = zeros(n)\n",
    "        for j in 1:n\n",
    "            if W[j] > 0\n",
    "                dW[j] = (-2 * dot(X_train[:, j], y_train - Y_pred) + alpha) / m\n",
    "            else\n",
    "                dW[j] = (-2 * dot(X_train[:, j], y_train - Y_pred) - alpha) / m\n",
    "            end\n",
    "        end\n",
    "        db = -2 * sum(y_train - Y_pred) / m\n",
    "        W .-= learning_rate * dW\n",
    "        b -= learning_rate * db\n",
    "    end\n",
    "\n",
    "    return W, b\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**5. Cross-Validation Loop and 6. Selection of Optimal Alpha**\n",
    "\n",
    "We immplement a for loop to fit the lasso regression. Also, we find the best value of alpha that reduces the average MSE for each fold."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "function cross_validate_lasso(X_train, y_train, alphas, kf)\n",
    "    avg_mse_values = Float64[]\n",
    "    best_alpha = nothing\n",
    "    min_avg_mse = Inf\n",
    "\n",
    "    for alpha in alphas\n",
    "        mse_list = Float64[]\n",
    "        for (train_index, val_index) in kf\n",
    "            X_train_fold, X_val_fold = X_train[train_index, :], X_train[val_index, :]\n",
    "            y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]\n",
    "\n",
    "            # Train Lasso regression model with the current alpha\n",
    "            W, b = lasso_regression(X_train_fold, y_train_fold, alpha)\n",
    "            y_pred_val = X_val_fold * W .+ b\n",
    "\n",
    "            # Calculate MSE for this fold\n",
    "            mse_fold = mean((y_val_fold .- y_pred_val).^2)\n",
    "            push!(mse_list, mse_fold)\n",
    "        end\n",
    "\n",
    "        # Calculate average MSE across all folds\n",
    "        avg_mse = mean(mse_list)\n",
    "        push!(avg_mse_values, avg_mse)\n",
    "        println(\"Alpha=$(round(alpha, digits=1)), Average MSE: $(round(avg_mse, digits=5))\")\n",
    "\n",
    "        # Update the best alpha and minimum average MSE\n",
    "        if avg_mse < min_avg_mse\n",
    "            min_avg_mse = avg_mse\n",
    "            best_alpha = alpha\n",
    "        end\n",
    "    end\n",
    "\n",
    "    println(\"Best Alpha: $(round(best_alpha, digits=1)), Minimum Average MSE: $(round(min_avg_mse, digits=5))\")\n",
    "\n",
    "    # Plotting the cross-validated MSE for each alpha value\n",
    "    plt = plot(alphas, avg_mse_values, marker = :o, linestyle = :solid, xlabel = \"Alpha\", ylabel = \"Average MSE\",\n",
    "               title = \"Cross-Validated MSE for Different Alpha Values\", legend = false)\n",
    "    xticks!(plt, alphas)\n",
    "    grid!(plt, true)\n",
    "    display(plt)\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**7. Model Training and Evaluation**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Train Lasso regression model with the best alpha\n",
    "W, b = lasso_regression(X_train, y_train, best_alpha)\n",
    "\n",
    "# Make predictions on test data\n",
    "y_pred = X_test * W .+ b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lasso_corr = cor(y_test, y_pred)\n",
    "lasso_mae = mean(abs.(y_test .- y_pred))\n",
    "lasso_mse = mean((y_test .- y_pred).^2)\n",
    "\n",
    "# Print results\n",
    "println(\"Correlation: $(round(lasso_corr, digits=4))\")\n",
    "println(\"MAE: $(round(lasso_mae, digits=4))\")\n",
    "println(\"MSE: $(round(lasso_mse, digits=4))\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**8. Report Results**\n",
    "\n",
    "We began by selecting the parameters for a flexible model, one that includes interactions. After selecting the parameters, we found that the alpha value that produced the lowest mean squared error (MSE) in cross-validation was 60. We then trained the model using all the available training data with the best alpha value. Using the fitted betas, we predicted the lwage using the test X vector. The resulting MSE in the test data was 0.3569, which was lower than in the training data (which was 0.41906). This indicates that the model is not overfitting and that we have found a good correlation score (R square) of 50%."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Replication"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Wage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using Statistics\n",
    "using Plots\n",
    "\n",
    "\n",
    "wage_sorted = sort(data.wage)\n",
    "cumulative_sum = cumsum(wage_sorted)\n",
    "deciles = [percentile(cumulative_sum, p) for p in 0:10:100]\n",
    "population_fraction = collect(0:0.1:1)\n",
    "\n",
    "# Calcular la fracción acumulativa de salarios\n",
    "salary_fraction = [percentile(deciles ./ sum(data.wage), p) for p in 0:10:100]\n",
    "\n",
    "# Graficar la curva de Lorenz\n",
    "plot(population_fraction, salary_fraction, linewidth=2, color=:blue, label=\"\")\n",
    "plot!([0, 1], [0, 1], linestyle=:dash, linewidth=1, color=:red, label=\"Equality line\",\n",
    "    title=\"Lorenz Curve for Higher Education Salaries\",\n",
    "    xlabel=\"Cumulative fraction of the population\",\n",
    "    ylabel=\"Cumulative fraction of salaries\",\n",
    "    legend=:bottomright)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "LwAGE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using Plots\n",
    "using StatsPlots\n",
    "\n",
    "# Configurar el estilo\n",
    "default(; legend = false)\n",
    "\n",
    "# Crear el histograma de los salarios\n",
    "histogram(data.lwage, bins=30, color=:lightblue, edgecolor=:black, normed=true, xlabel=\"Lwage\", ylabel=\"Density\",\n",
    "    title=\"Histogram of Salaries\")\n",
    "\n",
    "# Crear la función de densidad\n",
    "density!(data.lwage, color=:red, linewidth=1)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Sex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import Pkg\n",
    "Pkg.add(\"PyPlot\")\n",
    "Pkg.add(\"Distributions\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Statistics\n",
    "using Plots\n",
    "\n",
    "# Calcular las proporciones de sexos\n",
    "proportions = combine(groupby(data, :sex), nrow => :count)\n",
    "\n",
    "# Calcular el total de observaciones\n",
    "total_obs = sum(proportions.count)\n",
    "\n",
    "# Asignar etiquetas 'Male' y 'Female'\n",
    "proportions[!, :sex_label] = ifelse.(proportions.sex .== 0, \"Male\", \"Female\")\n",
    "\n",
    "# Calcular las proporciones\n",
    "proportions[!, :percentage] = proportions.count ./ total_obs * 100\n",
    "\n",
    "# Graficar las proporciones sin leyenda\n",
    "display(bar(proportions.sex_label, proportions[!, :percentage],\n",
    "    xlabel = \"Sex\", ylabel = \"Percentage\",\n",
    "    title = \"Proportion of Males and Females\",\n",
    "    ylims = (0, 100),\n",
    "    bar_width = 0.5,\n",
    "    fmt = :png))\n",
    "\n",
    "# Mostrar el número total de observaciones\n",
    "println(\"Total observations: \", total_obs)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Dummies college"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Statistics\n",
    "using Plots\n",
    "\n",
    "# Crear la variable 'Education_Status'\n",
    "data[!, \"Education_Status\"] .= ifelse.(data.scl .== 1, \"Some College\",\n",
    "                                      ifelse.(data.clg .== 1, \"College Graduate\", \"Advanced Degree\"))\n",
    "\n",
    "# Calcular la frecuencia de educación\n",
    "edu_freq = combine(groupby(data, :Education_Status), nrow => :Frequency)\n",
    "\n",
    "# Calcular el total de observaciones\n",
    "total_obs = sum(edu_freq.Frequency)\n",
    "\n",
    "# Calcular el porcentaje\n",
    "edu_freq[!, :Percentage] = edu_freq.Frequency / total_obs * 100\n",
    "\n",
    "# Definir colores y etiquetas\n",
    "# Crear el gráfico de pastel\n",
    "pie(edu_freq.Frequency, labels=string.(labels, \": \", round.(edu_freq.Percentage, digits=1), \"%\"), startangle=90, \n",
    "    title=\"Education Status Distribution\", \n",
    "    legend=:topright, \n",
    "    fmt=:png, \n",
    "    aspect_ratio=1,\n",
    "    pct=true)\n",
    "\n",
    "# Añadir el número total de observaciones\n",
    "annotate!(1, -1.2, text(\"Total observations: $total_obs\", halign=:center, valign=:center))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Experience Higher Education"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Plots\n",
    "\n",
    "plt = plot(size=(800, 600))\n",
    "boxplot!(data.exp1, box=:box, whiskerwidth=0.2, title=\"Distribution of Experience in Individuals with Higher Education\",\n",
    "    ylabel=\"Experience (exp1)\", legend=false)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "COEFFICIENTS FOR DIFFERENT MODELS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using GLM\n",
    "using Statistics\n",
    "using Plots\n",
    "\n",
    "\n",
    "# Ajustar los modelos\n",
    "flex_y = @formula(lwage ~ exp1+exp2+exp3+exp4+scl+clg+ad+occ2+ind2+mw+so+we+(exp1+exp2+exp3+exp4)*(scl+clg+ad+occ2+ind2+mw+so+we) ) # modelo para Y\n",
    "flex_d = @formula(sex ~ exp1+exp2+exp3+exp4+scl+clg+ad+occ2+ind2+mw+so+we+(exp1+exp2+exp3+exp4)*(scl+clg+ad+occ2+ind2+mw+so+we))  # modelo para D\n",
    "\n",
    "# Ajustar el efecto lineal parcial de W desde Y\n",
    "t_Y = residuals(lm(flex_y, data))\n",
    "# Ajustar el efecto lineal parcial de W desde D\n",
    "t_D = residuals(lm(flex_d, data))\n",
    "# Crear un nuevo DataFrame con las variables relevantes para t_Y y t_D\n",
    "residuals_df = DataFrame(t_Y=t_Y, t_D=t_D)\n",
    "\n",
    "# Ajustar la regresión lineal entre t_Y y t_D\n",
    "partial_fit = lm(@formula(t_D ~ t_Y), residuals_df)\n",
    "\n",
    "# Ajustar los modelos\n",
    "basic_fit = lm(@formula(lwage ~ sex + exp1 + scl + clg + ad + mw + so + we + occ2 + ind2), data)\n",
    "\n",
    "control_fit = lm(@formula(lwage ~ sex + exp1+exp2+exp3+exp4+scl+clg+ad+occ2+ind2+mw+so+we+(exp1+exp2+exp3+exp4)*(scl+clg+ad+occ2+ind2+mw+so+we)), data)\n",
    "\n",
    "using Plots\n",
    "\n",
    "# Extraer los coeficientes para sex y los errores estándar de las últimas dos regresiones\n",
    "coefs = Dict(\"Basic\" => coef(basic_fit)[2],\n",
    "             \"Controls\" => coef(control_fit)[2],\n",
    "             \"Partialling out\" => coef(partial_fit)[2])  # El coeficiente de interés es el segundo en partial_fit\n",
    "\n",
    "ses = Dict(\"Basic\" => stderror(basic_fit)[2],\n",
    "           \"Controls\" => stderror(control_fit)[2],\n",
    "           \"Partialling out\" => stderror(partial_fit)[2])  # El error estándar correspondiente al coeficiente de interés\n",
    "\n",
    "# Gráfico de dispersión con barras de error\n",
    "scatter_plot = scatter(coefs, yerr=1.96 .* collect(values(ses)), legend=false, \n",
    "    xlabel=\"Model\", ylabel=\"Coefficient\", title=\"Effect of sex on lwage\",\n",
    "    markershape=:circle, markercolor=:blue, markerstrokecolor=:black,\n",
    "    markersize=8, markeralpha=0.8)\n",
    "\n",
    "# Línea horizontal en y=0\n",
    "hline!(scatter_plot, [0], color=\"gray\", linestyle=:dash)\n",
    "\n",
    "# Mostrar el gráfico\n",
    "display(scatter_plot)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#The coefficient associated with the gender variable, which indicates the prediction of being female on salary, is initially \n",
    "# negative. This suggests that, on average, women have lower salaries than men. However, after adding these controls, \n",
    "# such as work experience or educational level, the negative coefficient associated with the gender variable becomes \n",
    "# less negative.\n",
    "# \n",
    "# This change in the gender coefficient could be explained by the fact that the control variables are capturing\n",
    "# some of the variability in salaries that was previously incorrectly attributed to gender. This suggests \n",
    "# that additional factors, beyond gender, are influencing salaries, and the impact of gender on salaries \n",
    "# is less pronounced once these other variables are taken into account.Besides, both FWL and including control \n",
    "# variables in the regression model yield coefficient estimates for the variable of interest that reflect its net\n",
    "# impact on the dependent variable, once the effects of other explanatory variables have been taken into account.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Women and male graph (quartic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import Pkg\n",
    "Pkg.add(\"StatsModels\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import Pkg\n",
    "Pkg.add(\"Loess\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Statistics\n",
    "using Plots\n",
    "\n",
    "# Supongamos que tienes un DataFrame llamado data con las columnas lwage, exp4 y sex\n",
    "\n",
    "# Creamos un DataFrame separado para hombres y mujeres\n",
    "data_male = filter(row -> row.sex == 0, data)\n",
    "\n",
    "\n",
    "# Calculamos las medias de lwage para cada valor único de exp4 para hombres\n",
    "mean_lwage_male = combine(groupby(data_male, :exp4), :lwage => mean => :mean_lwage)\n",
    "\n",
    "# Ordenar el DataFrame por exp4\n",
    "sort!(mean_lwage_male, :exp4)\n",
    "\n",
    "# Crear el gráfico para hombres\n",
    "plot(mean_lwage_male.exp4, mean_lwage_male.mean_lwage, color=:blue, label=\"Mean lwage (Male)\",\n",
    "    xlabel=\"Experiencia (exp4)\", ylabel=\"Media de lwage (lwage)\", title=\"Media de lwage por exp4 (Hombres)\", marker=:circle)\n",
    "plot!(mean_lwage_male.exp4, mean_lwage_male.mean_lwage, color=:blue, linewidth=2, linestyle=:solid, label=\"\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using Pkg\n",
    "Pkg.add(\"Loess\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Plots\n",
    "using Loess\n",
    "\n",
    "# Supongamos que tienes un DataFrame llamado data con las columnas lwage, exp4 y sex\n",
    "\n",
    "# Creamos un DataFrame separado solo para varones\n",
    "data_male = filter(row -> row.sex == 0, data)\n",
    "\n",
    "# Extraemos las variables independientes y dependientes para el modelo LOESS\n",
    "exp4_male = data_male.exp4\n",
    "lwage_male = data_male.lwage\n",
    "\n",
    "# Ajustamos un modelo LOESS para varones con un span de ** para menos suavizamiento\n",
    "loess_model_male = loess(exp4_male, lwage_male, span=0.95)\n",
    "\n",
    "# Generamos predicciones para el modelo LOESS\n",
    "exp4_range_male = range(minimum(exp4_male), maximum(exp4_male), length=500)\n",
    "lwage_pred_male = predict(loess_model_male, exp4_range_male)\n",
    "\n",
    "# Creamos el gráfico para varones con la línea suavizada\n",
    "plot(exp4_range_male, lwage_pred_male, color=:red, label=\"Smoothed lwage (Male)\")\n",
    "xlabel!(\"Experiencia (exp4)\")\n",
    "ylabel!(\"lwage\")\n",
    "title!(\"Línea suavizada de lwage por exp4 (Varones)\")\n",
    "xlims!(0, 40)  # Limitar el eje x de 0 a 40\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_female = filter(row -> row.sex == 1, data)\n",
    "# Calculamos las medias de lwage para cada valor único de exp4 para mujeres\n",
    "mean_lwage_female = combine(groupby(data_female, :exp4), :lwage => mean => :mean_lwage)\n",
    "\n",
    "# Ordenar el DataFrame por exp4\n",
    "sort!(mean_lwage_female, :exp4)\n",
    "\n",
    "# Crear el gráfico para mujeres\n",
    "plot(mean_lwage_female.exp4, mean_lwage_female.mean_lwage, color=:red, label=\"Mean lwage (Female)\",\n",
    "    xlabel=\"Experiencia (exp4)\", ylabel=\"Media de lwage (lwage)\", title=\"Media de lwage por exp4 (Mujeres)\", marker=:circle)\n",
    "plot!(mean_lwage_female.exp4, mean_lwage_female.mean_lwage, color=:red, linewidth=2, linestyle=:solid, label=\"\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Plots\n",
    "using Loess\n",
    "\n",
    "# Supongamos que tienes un DataFrame llamado data con las columnas lwage, exp4 y sex\n",
    "\n",
    "# Creamos un DataFrame separado solo para mujeres\n",
    "data_female = filter(row -> row.sex == 1, data)\n",
    "\n",
    "# Extraemos las variables independientes y dependientes para el modelo LOESS\n",
    "exp4_female = data_female.exp4\n",
    "lwage_female = data_female.lwage\n",
    "\n",
    "# Ajustamos un modelo LOESS para mujeres con un span de 0.95 para menos suavizamiento\n",
    "loess_model_female = loess(exp4_female, lwage_female, span=0.95)\n",
    "\n",
    "# Generamos predicciones para el modelo LOESS\n",
    "exp4_range_female = range(minimum(exp4_female), maximum(exp4_female), length=500)\n",
    "lwage_pred_female = predict(loess_model_female, exp4_range_female)\n",
    "\n",
    "# Creamos el gráfico para mujeres con la línea suavizada\n",
    "plot(exp4_range_female, lwage_pred_female, color=:red, label=\"Smoothed lwage (Female)\")\n",
    "xlabel!(\"Experiencia (exp4)\")\n",
    "ylabel!(\"lwage\")\n",
    "title!(\"Línea suavizada de lwage por exp4 (Mujeres)\")\n",
    "xlims!(0, 40)  # Limitar el eje x de 0 a 40\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "using DataFrames\n",
    "using Plots\n",
    "using Loess\n",
    "\n",
    "# Supongamos que tienes un DataFrame llamado data con las columnas lwage, exp4 y sex\n",
    "\n",
    "# Creamos un DataFrame separado solo para mujeres\n",
    "data_female = filter(row -> row.sex == 1, data)\n",
    "\n",
    "# Calculamos las medias de lwage para cada valor único de exp4 para mujeres\n",
    "mean_lwage_female = combine(groupby(data_female, :exp4), :lwage => mean => :mean_lwage)\n",
    "\n",
    "# Ordenar el DataFrame por exp4\n",
    "sort!(mean_lwage_female, :exp4)\n",
    "\n",
    "# Extraemos las variables independientes y dependientes para el modelo LOESS\n",
    "exp4_female = data_female.exp4\n",
    "lwage_female = data_female.lwage\n",
    "\n",
    "# Ajustamos un modelo LOESS para mujeres con un span de 0.95 para menos suavizamiento\n",
    "loess_model_female = loess(exp4_female, lwage_female, span=0.95)\n",
    "\n",
    "# Generamos predicciones para el modelo LOESS\n",
    "exp4_range_female = range(minimum(exp4_female), maximum(exp4_female), length=500)\n",
    "lwage_pred_female = predict(loess_model_female, exp4_range_female)\n",
    "\n",
    "# Creamos el gráfico para mujeres con la línea suavizada y los puntos unidos\n",
    "plot(exp4_range_female, lwage_pred_female, color=:red, label=\"Smoothed lwage (Female)\", linewidth=2)\n",
    "scatter!(mean_lwage_female.exp4, mean_lwage_female.mean_lwage, color=:red, label=\"\", marker=:circle, seriestype=:line)\n",
    "xlabel!(\"Experiencia (exp4)\")\n",
    "ylabel!(\"lwage\")\n",
    "title!(\"Media de lwage y línea suavizada por exp4 (Mujeres)\")\n",
    "xlims!(0, 40)  # Limitar el eje x de 0 a 40\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Julia 1.10.2",
   "language": "julia",
   "name": "julia-1.10"
  },
  "language_info": {
   "file_extension": ".jl",
   "mimetype": "application/julia",
   "name": "julia",
   "version": "1.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
