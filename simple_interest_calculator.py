"""
Simple Interest Calculator
---------------------------
This program calculates the simple interest and the total amount
based on the principal, rate of interest, and time period entered
by the user.

Formula used:
    Simple Interest (SI) = (P * R * T) / 100
    Total Amount (A)     = P + SI

Where:
    P = Principal amount
    R = Annual interest rate (in percentage)
    T = Time period (in years)
"""


def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest and total amount.

    Parameters:
        principal (float): The initial amount of money (P)
        rate (float): The annual interest rate in percent (R)
        time (float): The time period in years (T)

    Returns:
        tuple: (simple_interest, total_amount)
    """
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    return simple_interest, total_amount


def get_positive_number(prompt):
    """
    Prompts the user for a number and validates that it is positive.
    Keeps asking until a valid positive number is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=" * 40)
    print("      SIMPLE INTEREST CALCULATOR")
    print("=" * 40)

    principal = get_positive_number("Enter the principal amount: ")
    rate = get_positive_number("Enter the annual interest rate (%): ")
    time = get_positive_number("Enter the time period (years): ")

    simple_interest, total_amount = calculate_simple_interest(principal, rate, time)

    print("\n--- Results ---")
    print(f"Principal Amount   : {principal:.2f}")
    print(f"Interest Rate      : {rate:.2f}%")
    print(f"Time Period        : {time:.2f} years")
    print(f"Simple Interest    : {simple_interest:.2f}")
    print(f"Total Amount       : {total_amount:.2f}")


if __name__ == "__main__":
    main()
