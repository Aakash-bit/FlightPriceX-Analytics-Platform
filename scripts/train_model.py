import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_flight_fuel.csv"
)

print("Loading dataset from:")
print(file_path)

df = pd.read_csv(file_path)

categorical_cols = [
    "airline",
    "source_city",
    "destination_city",
    "class",
    "departure_time",
    "arrival_time",
    "stops"
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])


drop_cols = ["price"]

if "flight" in df.columns:
    drop_cols.append("flight")

X = df.drop(columns=drop_cols)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

print("Training model...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n===== MODEL RESULTS =====")
print(f"MAE: {mae:.2f}")
print(f"R² Score: {r2:.4f}")
print(f"Approx Accuracy: {r2 * 100:.2f}%")