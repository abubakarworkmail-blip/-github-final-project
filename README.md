# Simple Interest Calculator

A simple Python command-line program that calculates **Simple Interest** and the **Total Amount** based on the principal, interest rate, and time period entered by the user.

## 📌 Description

Simple interest is a quick and easy method of calculating the interest charge on a loan or the return on an investment. This program takes three inputs — principal, rate, and time — and computes the interest and total amount using the standard simple interest formula.

## 🧮 Formula Used

```
Simple Interest (SI) = (P × R × T) / 100
Total Amount (A)     = P + SI
```

Where:
- **P** = Principal amount (initial sum of money)
- **R** = Annual interest rate (in percentage)
- **T** = Time period (in years)

## 🚀 Features

- Takes user input for principal, rate, and time
- Validates input to ensure only positive numeric values are accepted
- Calculates and displays the simple interest
- Calculates and displays the total amount (principal + interest)
- Clean, readable console output

## 🛠️ Requirements

- Python 3.x

No external libraries are required — this program only uses Python's built-in features.

## ▶️ How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the script using:

   ```bash
   python simple_interest_calculator.py
   ```

4. Enter the requested values when prompted:

   ```
   Enter the principal amount: 1000
   Enter the annual interest rate (%): 5
   Enter the time period (years): 2
   ```

5. View the output:

   ```
   --- Results ---
   Principal Amount   : 1000.00
   Interest Rate      : 5.00%
   Time Period        : 2.00 years
   Simple Interest    : 100.00
   Total Amount       : 1100.00
   ```

## 📂 Project Structure

```
├── simple_interest_calculator.py   # Main program file
└── README.md                       # Project documentation
```

## 📄 License

This project is open-source and available for personal or educational use.
Note: fixed typo in documentation.
