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

    from typing import List, Tuple
    from datetime import date

    def find_future_cashflows(
        start_date: date, end_date: date, pay_frequency: str, day_count_convention: str
    ) -> List[Tuple[date, float]]:
        """
        Calculate all future cashflows of a swap given the start date, end date, payment frequency, and day count convention.

        Args:
        - start_date (date): The start date of the swap.
        - end_date (date): The end date of the swap.
        - pay_frequency (str): The frequency of payments (e.g., 'monthly', 'quarterly', 'semi-annually', 'annually').
        - day_count_convention (str): The day count convention for interest calculation (e.g., '30/360', 'actual/360', 'actual/365').

        Returns:
        - List[Tuple[date, float]]: A list of tuples where each tuple contains a payment date and the corresponding cashflow amount.
        """
        from dateutil.relativedelta import relativedelta

        # Define payment frequency in terms of months
        frequency_mapping = {
            "monthly": 1,
            "quarterly": 3,
            "semi-annually": 6,
            "annually": 12,
        }

        # Calculate the number of days in a year based on the day count convention
        days_in_year = {"30/360": 360, "actual/360": 360, "actual/365": 365}

        payment_interval = frequency_mapping[pay_frequency]
        cashflows = []
        current_date = start_date

        while current_date < end_date:
            # Calculate next payment date
            next_payment_date = current_date + relativedelta(months=+payment_interval)
            if next_payment_date > end_date:
                next_payment_date = end_date

            # Placeholder for cashflow amount calculation
            # In a real scenario, this would involve calculating the interest based on the notional amount, rate, and day count convention
            cashflow_amount = 0.0  # This is a placeholder

            cashflows.append((next_payment_date, cashflow_amount))

            current_date = next_payment_date

        return cashflows
