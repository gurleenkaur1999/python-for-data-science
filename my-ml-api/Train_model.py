 
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


import joblib

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
#saving the resut of model in model.pkl file

print("✓ Model saved as 'model.pkl'")
print(f"✓ Model accuracy: {model.score(X_test, y_test):.2%}")

