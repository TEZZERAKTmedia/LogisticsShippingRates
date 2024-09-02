# Shipping cost calculator
## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms:"))
rate = float(input("Enter the shipping rate in kilograms"))

#calculate shipping cost
shipping_cost = weight * rate

#Display result
print(f"Shipping cost {shipping_cost} USD")

