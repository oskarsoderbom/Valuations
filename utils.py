from datetime import date, timedelta
import numpy as np
from typing import Dict
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from datetime import date, timedelta
import numpy as np


def generate_complex_mock_ois_rates(curve_date: date, years=30) -> Dict[date, float]:
    """
    Generate more complex and realistic mock OIS rates data for standard market tenors.

    Args:
    - curve_date (date): The date from which the curve starts.
    - years (int): The maximum tenor in years for which to generate rates.

    Returns:
    - Dict[date, float]: A dictionary with tenor dates as keys and mock OIS rates as values.
    """
    # Define tenors in days for common market maturities
    tenors_days = [1, 7, 30, 90, 180] + [365 * i for i in range(1, years + 1)]
    rates = {}

    # Parameters to shape the curve
    base_rate = 0.02  # Starting with a 2% base rate
    hump_midpoint = 5  # The midpoint of the hump in years
    hump_magnitude = 0.03  # The magnitude of the hump

    for tenor in tenors_days:
        tenor_date = curve_date + timedelta(days=tenor)
        tenor_years = tenor / 365

        # Generate a rate with a hump for mid-term tenors and flattening out for long-term tenors
        rate = (
            base_rate
            + hump_magnitude
            * np.exp(
                -((tenor_years - hump_midpoint) ** 2) / (2 * (hump_midpoint / 3) ** 2)
            )
            + 0.005 * tenor_years
        )  # Gradual increase to simulate long-term expectations

        # Add random noise
        rate += np.random.normal(-0.002, 0.002)

        rates[tenor_date] = rate

    return rates


if __name__ == "__main__":

    # Example usage
    curve_date = date(2023, 1, 1)  # Starting date of the curve
    mock_ois_rates = generate_complex_mock_ois_rates(curve_date)

    # Convert the dictionary to a DataFrame for plotting
    rates_df = pd.DataFrame(list(mock_ois_rates.items()), columns=["Date", "Rate"])

    # Plotting the OIS rates
    sns.lineplot(data=rates_df, x="Date", y="Rate").set_title(
        "Mock OIS Rates Over Time"
    )
    plt.show()
