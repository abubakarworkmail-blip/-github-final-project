#!/bin/bash

# ============================================
# Simple Interest Calculator (Bash Script)
# --------------------------------------------
# Formula:
#   Simple Interest (SI) = (P * R * T) / 100
#   Total Amount (A)     = P + SI
#
# Where:
#   P = Principal amount
#   R = Annual interest rate (in percentage)
#   T = Time period (in years)
# ============================================

echo "========================================"
echo "      SIMPLE INTEREST CALCULATOR"
echo "========================================"

# Function to validate that input is a positive number
validate_number() {
    local value=$1
    if ! [[ $value =~ ^[0-9]+([.][0-9]+)?$ ]]; then
        echo "Invalid input. Please enter a positive numeric value."
        return 1
    fi
    return 0
}

# Get Principal amount
while true; do
    read -p "Enter the principal amount: " principal
    validate_number "$principal" && break
done

# Get Rate of interest
while true; do
    read -p "Enter the annual interest rate (%): " rate
    validate_number "$rate" && break
done

# Get Time period
while true; do
    read -p "Enter the time period (years): " time
    validate_number "$time" && break
done

# Calculate Simple Interest and Total Amount using bc for floating point math
simple_interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
total_amount=$(echo "scale=2; $principal + $simple_interest" | bc)

# Display results
echo ""
echo "--- Results ---"
printf "Principal Amount   : %.2f\n" "$principal"
printf "Interest Rate      : %.2f%%\n" "$rate"
printf "Time Period        : %.2f years\n" "$time"
printf "Simple Interest    : %.2f\n" "$simple_interest"
printf "Total Amount       : %.2f\n" "$total_amount"
