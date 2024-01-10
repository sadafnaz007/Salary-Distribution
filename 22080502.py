import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Styling for plots
sns.set(style="whitegrid")

# Load the dataset
dataset = pd.read_csv('data2.csv', header=None)
dataset.columns = ['Salary']

# Calculate the mean salary (W̃)
mean_salary = dataset['Salary'].mean()

# Calculate the specific value X (salary such that 5% have a salary above X)
X_value = dataset['Salary'].quantile(0.95)

# Creating a more colorful and advanced histogram
plt.figure(figsize=(10, 6))
sns.histplot(dataset['Salary'], bins=30, kde=True, color='purple', edgecolor='yellow')

# Adding a vertical line for the mean salary
plt.axvline(mean_salary, color='yellow', linestyle='dashed', linewidth=2, label=f'Mean Salary (W̃): €{mean_salary:.2f}')

# Adding a vertical line for the specific value X
plt.axvline(X_value, color='red', linestyle='dashed', linewidth=2, label=f'Value X (5% above): €{X_value:.2f}')

# Adding labels, title, and legend
plt.xlabel('Salary (€)')
plt.ylabel('Density')
plt.title('Colorful Salary Distribution with Mean and Specific Value X')
plt.legend()

# Display the histogram
plt.show()
