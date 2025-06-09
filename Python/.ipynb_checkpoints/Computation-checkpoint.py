import numpy as np
import matplotlib.pyplot as plt

def basic_probability(n_val):
  # if n_val < 0:
  #   return 0.0
  # k = n_val // 3
  # if n_val % 3 == 0:
  #   return 1.0 / (2.0 * (6.0 ** k))
  # elif n_val % 3 == 1 or n_val % 3 == 2:
  #   return 1.0 / (6.0 ** (k + 1))
  # else:
  #   return 0.0
  if n_val == 1 or n_val == 2 or n_val == 3:
    return 1.0 / 6.0
  elif n_val == 0:
    return 1.0 / 2.0
  else:
    return 0.0

def n_throws_basic_probability(n_val,j):
  if j == 0:
    return basic_probability(n_val)
  prob = 0
  for x in range(0, n_val+1):
    prob += basic_probability(x) * n_throws_basic_probability(n_val, j-1)
  return prob

# --- 1. Configuration for the plot ---
# Set the font for better aesthetics
plt.rcParams['font.family'] = 'Inter'


# --- 2. Generate data points for plotting ---
# Determine a range for n.
# We'll plot from n=0 up to n=25 to clearly see multiple cycles of k.
# The probabilities decrease rapidly, so higher n values might be too small to visualize.
n_values = np.arange(0, 26)

# Calculate the probability f(n) for each n in the range
probabilities = [n_throws_basic_probability(n,6) for n in n_values]

# Convert to numpy array for easier calculations/plotting if needed
probabilities = np.array(probabilities)

# --- 3. Plotting using Matplotlib ---
plt.figure(figsize=(12, 7)) # Set the figure size for better readability

# Use a stem plot to visualize discrete probabilities
# `markerfmt='o'` sets the marker style to circles.
# `linefmt='red'` sets the color of the vertical lines.
# `basefmt=" "` removes the horizontal line at the bottom.
# plt.stem(n_values, probabilities2, basefmt=" ",
#          markerfmt='o', linefmt='blue',
#          label='Custom Discrete Function $f(n)$')
plt.stem(n_values, probabilities,
  basefmt=" ",
  markerfmt='o',
  linefmt='blue',
  label='Custom Discrete Function $f(n)$')

# Add title and labels for clarity
plt.title('Plot of Custom Discrete Probability Function $f(n)$', fontsize=18)
plt.xlabel('Integer Value ($n$)', fontsize=14)
plt.ylabel('Probability $f(n)$', fontsize=14)

# Set x-axis ticks to be integers
plt.xticks(n_values)

# Limit y-axis if necessary for better visualization of smaller probabilities,
# but ensure it starts from 0.
plt.ylim(bottom=0)

# Add a grid for easier reading of values
plt.grid(True, linestyle='--', alpha=0.7)

# Add a legend to identify the plotted function
plt.legend(fontsize=12)

# Customize tick parameters
plt.tick_params(axis='both', which='major', labelsize=12)

# Apply aesthetic touches to the plot borders (conceptual for raster output)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(0.5)
plt.gca().spines['bottom'].set_linewidth(0.5)

# Ensure tight layout to prevent labels from being cut off
plt.tight_layout()

# Display the plot
# This command opens a window showing the plot.
plt.show()

print("Custom discrete probability function plot generated successfully.")