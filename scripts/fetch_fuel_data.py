import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


flight_path = os.path.join(BASE_DIR, "data", "flight_price.csv")
fuel_path = os.path.join(BASE_DIR, "data", "processed", "fuel_data.csv")

print("Flight Path:", flight_path)
print("Fuel Path:", fuel_path)

flight_df = pd.read_csv(flight_path)
fuel_df = pd.read_csv(fuel_path)

if "Unnamed: 0" in flight_df.columns:
    flight_df = flight_df.drop(columns=["Unnamed: 0"])

latest_fuel_price = fuel_df["fuel_price"].iloc[-1]

print(f"Latest Fuel Price: {latest_fuel_price}")


flight_df["fuel_price"] = latest_fuel_price

processed_dir = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(processed_dir, exist_ok=True)

# Output file path
output_path = os.path.join(
    processed_dir,
    "final_flight_fuel.csv"
)

try:
    if os.path.exists(output_path):
        os.remove(output_path)
except PermissionError:
    print(
        "\nERROR: final_flight_fuel.csv is currently open."
        "\nPlease close the CSV file (Excel, VS Code, etc.) and run again."
    )
    exit()

flight_df.to_csv(output_path, index=False)

print("\nMerged dataset saved successfully")
print("Output File:", output_path)

print("\nDataset Information")
print("-------------------")
print("Rows:", len(flight_df))
print("Columns:", len(flight_df.columns))

print("\nColumns:")
print(flight_df.columns.tolist())

print("\nSample Data:")
print(flight_df.head())