# Calculating the sample variance

The hypothesis tests we have been doing thus far are not particularly realistic.  Normally our null hypothesis contains a statement of the value of ![](https://render.githubusercontent.com/render/math?math=\mu) (the expectation) but it does not give us a value for ![](https://render.githubusercontent.com/render/math?math=\sigma) (the standard deviation).   During most of the rest of this exercise and in the exercise next week we will thus be learning the various tricks that can be performed when we are not told ![](https://render.githubusercontent.com/render/math?math=\sigma).  

The simplest of these tricks is to calculate an estimate for ![](https://render.githubusercontent.com/render/math?math=\sigma).  We have done this before by estimating the sample variance using:

![](https://render.githubusercontent.com/render/math?math=\sigma^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^{n}X_i^2-\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right])

We have used this formula before in other exercises.  __To check that you remember how to use it you need to complete the function called `standardDeviation` in the `main.py`__.  This function tasks a NumPy array called `data` in input, which contains a set of samples from a distribution.  The function should return the value of the standard deviation for this input data set.  
