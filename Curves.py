from typing import Dict
from datetime import date
from scipy.interpolate import CubicSpline
import numpy as np


class Curve:
    def __init__(self, curve_date: date, rates: Dict[date, float]) -> None:
        self.curve_date = curve_date
        # Sort rates by date to ensure correct order for interpolation
        sorted_dates = sorted(rates)
        self.dates = sorted_dates
        self.rates = [rates[dt] for dt in sorted_dates]

        # Prepare x (days since curve date) and y (rates) for CubicSpline
        self.x = [(dt - curve_date).days for dt in sorted_dates]
        self.y = self.rates
        self.spline = CubicSpline(self.x, self.y)

    def get_rate(self, target_date: date) -> float:
        # Convert target_date to days since curve_date for interpolation
        target_x = (target_date - self.curve_date).days

        # Use spline to interpolate/extrapolate the rate
        return self.spline(target_x)


class SOFRCurve(Curve):
    def __init__(self, curve_date: date, rates: Dict[date, float]) -> None:
        super().__init__(curve_date, rates)
        # Additional attributes or methods specific to SOFR curve


class OISCurve(Curve):
    def __init__(self, curve_date: date, rates: Dict[date, float]) -> None:
        super().__init__(curve_date, rates)
        # Additional attributes or methods specific to OIS curve
