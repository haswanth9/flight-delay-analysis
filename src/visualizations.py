import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data():
    return pd.read_csv("outputs/cleaned_flights.csv")

def save_plot(name):
    os.makedirs("outputs/charts", exist_ok=True)
    plt.savefig(f"outputs/charts/{name}.png", bbox_inches='tight')
    plt.close()

def airline_plot(df):
    data = df.groupby("Reporting_Airline")["ArrDelay"].mean().sort_values()

    plt.figure()
    data.plot(kind='bar')
    plt.title("Average Delay by Airline")
    plt.ylabel("Delay (minutes)")
    save_plot("airline_delays")

def airport_plot(df):
    data = df.groupby("Origin")["ArrDelay"].mean().sort_values(ascending=False).head(10)

    plt.figure()
    data.plot(kind='bar')
    plt.title("Top 10 Airports by Delay")
    save_plot("airport_delays")

def monthly_plot(df):
    data = df.groupby("month_name")["ArrDelay"].mean()

    plt.figure()
    data.plot(kind='bar')
    plt.title("Average Delay by Month")
    save_plot("monthly_delays")

def main():
    df = load_data()

    airline_plot(df)
    airport_plot(df)
    monthly_plot(df)

    print("Charts saved in outputs/charts/")

if __name__ == "__main__":
    main()