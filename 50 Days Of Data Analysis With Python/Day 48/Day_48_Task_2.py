# 2 Import the flowers_dataset , which is a CSV file.


# Create a copy of the DataFrame. In supervised machine learning, the target variable is the variable that will be
# predicted using the other variables in the dataset.
# This target variable must be converted into a numeric data type before fitting a model.
# Convert this target variable (flower_type) into a numeric data type and separate the target column from the other variables.
# Write code to create two variables, x and y. X is the variable that will predict the target variable, y.
# Use Sklearn train_test_split() function to split the data into training and test sets. Make the test size 20% of the dataset.
# Set the random_state parameter to 42. Check the shapes of the training and test sets.
# What is the purpose of the random_state parameter in the train_test_split() function?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Import the dataset
df = pd.read_csv('flowers_dataset.csv')

# Create a copy of the DataFrame
flowers = df.copy()

# Convert the target variable (flower_type) to numeric
encoder = LabelEncoder()
flowers['flower_type'] = encoder.fit_transform(flowers['flower_type'])

# Create X (features) and y (target)
X = flowers.drop('flower_type', axis=1)
y = flowers['flower_type']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Check the shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

print()
print("The random_state parameter ensures the data is split in the same way every time the code is run.\nThis makes the results reproducible and allows for consistent model evaluation.")