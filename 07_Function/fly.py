from typing import Final

MAX_FLYING_WEIGHT: Final[float] = 15


def calc_weight(weight: float) -> float:
    """
    Calculates Mohan Weight
    ------------------------

    Look how the function just transforms data, from float to float.
    """
    return (weight + 32) / 8


def can_fly(weight: float) -> bool:
    """
    Returns if you can fly
    ----------------------

    This function is a nice example for data transformation, we convert
    float values to boolean values!! Nice isn't it!
    """
    return weight <= MAX_FLYING_WEIGHT


def flying_friends(friends: dict[str, float]) -> None:
    """
    Displays flying and non-flying friends

    Note:
    -----
    No data transformation here.
    We are printing the output to console, the function doesn't return anything.
    """
    for name, earth_weight in friends.items():
        zortan_weight = calc_weight(earth_weight)
        if can_fly(zortan_weight):
            print(f"{name}: {zortan_weight} kgs can fly on Zortan!")
        else:
            print(f"{name}: {zortan_weight} kgs can only walk on Zortan.")


def main():
    friends: dict[str, float] = {
        "Mohan": 54,
        "Sohan": 88,
        "Moni": 50,
        "Ruki": 102,
        "Soni": 90,
    }
    flying_friends(friends)


main()
