# Project 2 - Data Classification Using AI

# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

# Display results
print("========== AI Classification Project ==========")
print("Dataset Loaded Successfully")
print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))
print("-----------------------------------------------")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("-----------------------------------------------")

# Predict a new flower
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("Prediction for sample", sample)

print("Flower Name:", iris.target_names[prediction][0])