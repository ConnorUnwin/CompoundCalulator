import math
import sys as system


def truncate(number, digits) -> float:
    stepper = pow(10.00, digits)
    return math.trunc(stepper * number) / stepper

def compound():
    base_amount = float(system.argv[1])
    duration = int(system.argv[2])
    annaul_interest = float(int(system.argv[3]) / 100)
    year = 0

    while year < duration:
        year += 1
        compound_amount = base_amount * annaul_interest
        base_amount += compound_amount
        print("Year {} £{}".format(year, truncate(base_amount, 2)))

compound()