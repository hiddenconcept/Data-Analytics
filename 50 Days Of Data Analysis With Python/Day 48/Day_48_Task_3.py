#3 Why is it important to standardize the data before fitting?
#Use Sklearn StandardScaler to standardize the features in the dataset (training and test sets).
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('flowers_dataset.csv')

# Make a copy
flowers = df.copy()

# Convert the target variable to numeric
encoder = LabelEncoder()
flowers['flower_type'] = encoder.fit_transform(flowers['flower_type'])

# Create features (X) and target (y)
X = flowers.drop('flower_type', axis=1)
y = flowers['flower_type']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Standardize the data
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Check the shapes
print(X_train_scaled.shape)
print(X_test_scaled.shape)

print("Standardizing the data puts all features on the same scale so that no feature dominates the model because of its larger values.\n"
      " It also improves the performance and convergence of many machine learning algorithms.\n"
      " The scaler is fit on the training data and then applied to the test data to avoid data leakage.")