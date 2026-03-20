import pandas as pd

def load_data():
    return pd.read_csv("outputs/cleaned_flights.csv")

def monthly_travel_insights(df):
    monthly = df.groupby("month_name")["ArrDelay"].mean().sort_values()

    print("\nBest Months to Travel (Lower Delays -> Likely Lower Demand / Better Prices):")
    print(monthly.head(5))

    print("\nWorst Months to Travel (Higher Delays -> Likely Higher Demand / Higher Prices):")
    print(monthly.tail(5))

def airline_travel_insights(df):
    airline = df.groupby("Reporting_Airline")["ArrDelay"].mean().sort_values()

    print("\nMost Reliable Airlines (Likely More Cost-Efficient Choices):")
    print(airline.head(5))

    print("\nLeast Reliable Airlines (Likely Busier / Less Cost-Efficient Choices):")
    print(airline.tail(5))

def main():
    df = load_data()
    monthly_travel_insights(df)
    airline_travel_insights(df)

if __name__ == "__main__":
    main()