import pandas as pd

def load_data():
    return pd.read_csv("outputs/cleaned_flights.csv")

def airline_delays(df):
    print("\nAverage Delay by Airline:")
    print(df.groupby("Reporting_Airline")["ArrDelay"].mean().sort_values(ascending=False))

def airport_delays(df):
    print("\nTop 10 Worst Airports:")
    print(df.groupby("Origin")["ArrDelay"].mean().sort_values(ascending=False).head(10))

def monthly_trends(df):
    print("\nAverage Delay by Month:")
    print(df.groupby("month_name")["ArrDelay"].mean())

def main():
    df = load_data()

    airline_delays(df)
    airport_delays(df)
    monthly_trends(df)

if __name__ == "__main__":
    main()