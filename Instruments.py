from typing import List
from datetime import date
from dateutil.relativedelta import relativedelta


class Derivative:
    def __init__(
        self, notional, fixed_rate, tenor, payment_frequency, start_date, end_date
    ) -> None:
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.tenor = tenor
        self.payment_frequency = payment_frequency
        self.start_date = start_date
        self.end_date = end_date
        # Additional attributes as needed


class IRSSwap(Derivative):
    def __init__(
        self, notional, fixed_rate, tenor, payment_frequency, start_date, end_date
    ) -> None:
        super().__init__(
            notional, fixed_rate, tenor, payment_frequency, start_date, end_date
        )
        # Additional attributes as needed for IRSSwap

    def calculate_fixed_leg_cash_flows(self) -> List[float]:
        # Calculate and return fixed leg cash flows
        pass

    def calculate_floating_leg_cash_flows(self, sofr_curve) -> List[float]:
        # Calculate and return floating leg cash flows using SOFR curve
        pass

    def discount_cash_flows(self, cash_flows, ois_curve) -> None:
        # Discount cash flows using OIS curve and return present value
        pass

    def value_swap(self, sofr_curve, ois_curve) -> float:
        # Main valuation logic
        # Calculate fixed and floating leg cash flows, discount them, and compute NPV
        fixed_leg_cash_flows = self.calculate_fixed_leg_cash_flows()
        floating_leg_cash_flows = self.calculate_floating_leg_cash_flows(sofr_curve)
        fixed_leg_npv = self.discount_cash_flows(fixed_leg_cash_flows, ois_curve)
        floating_leg_npv = self.discount_cash_flows(floating_leg_cash_flows, ois_curve)
        return fixed_leg_npv - floating_leg_npv
