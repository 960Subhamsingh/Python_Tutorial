"""
Weight = (Earth Weight + 32) / 8
"""


def calc_weight(weight: float) -> float:
    return (weight + 32) / 8


print(f"You weigh {calc_weight(60):.2f} kgs on Zortan.")
