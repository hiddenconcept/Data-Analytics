import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
rng = np.random.default_rng(seed=0)

# Generate 1000 random numbers from standard normal distribution
arr = rng.normal(loc=0, scale=1, size=1000)

# Calculate statistics
mean = np.mean(arr)
variance = np.var(arr)
std_dev = np.std(arr)

print("=" * 50)
print("STATISTICS:")
print("=" * 50)
print(f"Mean = {mean:.4f}")
print(f"Variance = {variance:.4f}")
print(f"Standard Deviation = {std_dev:.4f}")
print(f"Min Value = {np.min(arr):.4f}")
print(f"Max Value = {np.max(arr):.4f}")
print("=" * 50)

# Create figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Basic Histogram
axes[0, 0].hist(arr, bins=72, edgecolor='black', color='skyblue')
axes[0, 0].set_title("Histogram of Random Numbers")
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].grid(axis='y', alpha=0.3)

# 2. Histogram with normal curve overlay
axes[0, 1].hist(arr, bins=30, density=True, edgecolor='black', color='lightgreen', alpha=0.7)
# Overlay theoretical normal distribution
x = np.linspace(arr.min(), arr.max(), 100)
axes[0, 1].plot(x, 1/(np.sqrt(2*np.pi)) * np.exp(-0.5*x**2), 'r-', linewidth=2, label='Theoretical Normal')
axes[0, 1].set_title("Histogram with Normal Distribution Curve")
axes[0, 1].set_xlabel('Value')
axes[0, 1].set_ylabel('Density')
axes[0, 1].legend()
axes[0, 1].grid(alpha=0.3)

# 3. Box Plot
axes[1, 0].boxplot(arr, vert=True)
axes[1, 0].set_title("Box Plot")
axes[1, 0].set_ylabel('Value')
axes[1, 0].grid(axis='y', alpha=0.3)

# 4. Q-Q Plot (Quantile-Quantile)
from scipy import stats
stats.probplot(arr, dist="norm", plot=axes[1, 1])
axes[1, 1].set_title("Q-Q Plot (Normality Check)")
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()