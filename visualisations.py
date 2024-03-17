import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict
from datetime import date


def plot_rate_curve(rate_curve: Dict[date, float]) -> None:
    # Convert the rate curve dictionary into lists for plotting
    dates = list(rate_curve.keys())
    rates = list(rate_curve.values())

    # Set the seaborn style for better aesthetics
    sns.set(style="whitegrid")

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker="o", linestyle="-", color="b")

    # Set plot title and labels
    plt.title("Rate Curve")
    plt.xlabel("Date")
    plt.ylabel("Rate")

    # Rotate date labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()
