"""BESSEL CORRECTION: Sample variance is a biased estimator of population variance. It tends
to understiamate or overestimate the point estimate.

This comes as the sample mean may vary from the population mean (as for always having fewer observation),
thus yielding a biased estimate of the population variance.

"""

import numpy as np # Mathematical operations
import matplotlib.pyplot as plt #Plot results 
import pandas as pd # Not necessary, but used for basic data manipulation

np.random.seed(2024) # Fix random output


# 1) Generate population data

def data(replications): # Create random sample data for a population distribution of tech salaries. mu = $100,000, std = $15,000; As seen, unit of measure is USD
      data = np.random.normal(100000, 15000,replications) # Tech salaries (made up data)
      mu = np.mean(data) # Compute mean
      sample_size = len(data) # Compute sample size/nº of observations
      return data, mu, sample_size 

# 2) Compute sample variance and standard deviation

def biased_std(data, mu, sample_size): # Without Bessel's Correction
      numerator = 0
      for i in data: # Create list comprenhension
            operation = (i - mu)**2 # Squared difference
            numerator += operation  # Sum of squared differences
      var = round(numerator / sample_size,2) # Rounded to 2 decimal places for better readibility
      std = round(np.sqrt(var),2) 
      manual_value = [var, std] # By 'manual' I mean, computing via the coded algorithm instead of calling a np's function/method
      original_metrics = (round(np.var(data, ddof=0),2),round(np.std(data, ddof=0),2)) # Original metrics meaning the ones computed by numpy
      margin_of_error = np.subtract(np.array(manual_value), np.array(original_metrics)) # Difference between manual and numpy's computation
      print(f"\nNO BESSEL'S CORRECTION:\n-Manual algorithm: {manual_value}\n-Numpy: {original_metrics})\n-Difference (ME): {margin_of_error}\n") #If ME is 0, then manual algorithm has been written correclty
      return manual_value
            

def non_biased_std(data,mu, sample_size): # Applying Bessel's Correction
      numerator = 0 
      for i in data: # Create list comprenhension
            operation = (i - mu)**2
            numerator += operation
      var = round(numerator / (sample_size - 1),2) # Biased
      std = round(np.sqrt(var),2)
      manual_value = [var,std]
      original_metrics = [round(np.var(data, ddof=1),2),round(np.std(data, ddof=1),2)]
      margin_of_error = np.subtract(np.array(manual_value), np.array(original_metrics))
      print(f"\nBESELL'S CORRECTION:\n-Manual algorithm: {manual_value}\nNumpy: {original_metrics})\n-Difference (ME): {margin_of_error}\n")
      return manual_value

# 3) Replicate the process to observe effects with LLN (law of large numbers)

def replicating(iterations): # Will compute point estimate for each iteration and store it in a dictionary
      resulst = dict() # Bessel's Correction dict 
      results2 = dict() # No Bessel's Correction dict
      for i in range(2,iterations +1): # First only with non_biased
            dataset = data(i)
            parameters = non_biased_std(*dataset) # '*' just unpacks the tuple
            resulst[i] = parameters[-1]
            parameters_2 = biased_std(*dataset)
            results2[i] = parameters_2[-1]
      return resulst, results2 # Return both dictionaries

def computations(iterations): # Create dfs and return bias based on MSE from the two approaches 
      dictionary = replicating(iterations)[0]
      dictionary2 = replicating(iterations)[-1]
      df = pd.DataFrame(list(dictionary.items()), columns = ["Iterations", "Point estimate"])
      MSE_1 = (df["Point estimate"].mean() - 15000)**2 # 15,000 is the true/population std
      mean_error = np.sqrt(MSE_1)
      df_2 =pd.DataFrame(list(dictionary2.items()), columns = ["Iterations", "Point estimate"])
      MSE_2 = (df_2["Point estimate"].mean() - 15000)**2
      mean_error_2 = np.sqrt(MSE_2)
      error_component = ((MSE_1, mean_error), (MSE_2, mean_error_2))
      return df, df_2, error_component

values = computations(200) # 200 iterations
df = values[0] 
df_2 = values[1]
mean_errors = (values[1:]) 

# 4) Plotting results 
plt.plot(df["Iterations"],df["Point estimate"], label = "With Bessel's Correction") # Bessel's Correction plot
plt.plot(df_2["Iterations"],df_2["Point estimate"], label = "Without Bessel's Correction") # No Bessel's Correction plot

plt.text(0.875, 0.8, f"Bessel Average Bias: {mean_errors[1][0][1]:.2f}",  # Adding as text the biases of each approach
         ha="left", va="center", transform=plt.gca().transAxes, fontsize=9, 
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=10))
plt.text(0.855, 0.70, f"No Bessel Average Bias: {mean_errors[1][1][1]:.2f}", 
         ha="left", va="center", transform=plt.gca().transAxes, fontsize=9, 
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=10))

plt.ylabel("Variance point estimate")
plt.xlabel("Nº of iterations")
plt.title("Variance Esimation, Bessel's Correction")

plt.grid(True)
plt.legend()

plt.show()

# 5) Conclusion: Bessel's Correction is necessary to avoid bias in the point estimate of the population variance. For this dataset Bessel's Correction has a bias 
# 190,46 units lower than the one without it.