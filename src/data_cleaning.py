import pandas as pd
import os

def clean_flight_data(input_path, output_path):
    print("Loading dataset...")
    df = pd.read_csv(input_path)

    print("Original shape:", df.shape)

    df["FlightDate"] = pd.to_datetime(df["FlightDate"], errors="coerce")

    df["month_name"] = df["FlightDate"].dt.month_name()
    df["day_name"] = df["FlightDate"].dt.day_name()

    if "ArrDelay" in df.columns:
        df["ArrDelay"] = df["ArrDelay"].fillna(0)

    cols = [
        "FlightDate", "Reporting_Airline",
        "Origin", "Dest",
        "DepDelay", "ArrDelay",
        "Distance", "Cancelled",
        "month_name", "day_name"
    ]

    df = df[[c for c in cols if c in df.columns]]

    df = df.dropna()

    os.makedirs("outputs", exist_ok=True)

    df.to_csv(output_path, index=False)

    print("Cleaned shape:", df.shape)
    print("Saved to:", output_path)


if __name__ == "__main__":
    clean_flight_data("data/flights.csv", "outputs/cleaned_flights.csv")