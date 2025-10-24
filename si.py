# simple_interest.py

# Input principal, rate, and time
P = float(input("Enter Principal amount (₹): "))
R = float(input("Enter Rate of Interest (%): "))
T = float(input("Enter Time (years): "))

# Calculate Simple Interest
SI = (P * R * T) / 100

# Display result
print(f"Simple Interest: ₹{SI}")
# Calculate Compound Interest
CI = P * (1 + R/100) ** T - P

# Display result
print(f"Compound Interest: ₹{CI:.2f}")
