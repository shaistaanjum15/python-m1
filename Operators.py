

# result = 3 + 4   # + is the operator
#                  # 3 and 4 are the operands
# print(result)    # Output: 7

# #Average
# total    = 120 + 85 + 150 + 95 + 110  # addition
# earnings = total * 15                  # multiplication
# average  = total / 5                   # division (float)
# print(total, earnings, average)
# # Output: 560  8400  112.0

# #division and modulus
# total    = 10       # total harvest in kg
# bag_size = 3        # each bag holds 25 kg

# bags     = total // bag_size  #10/3 = 3 full bags
# leftover = total % bag_size   # 10 % 3  = 1 kg left over

# print("Full bags:", bags)      # Output: 3
# print("Leftover:", leftover)   # Output: 1

# #comparison 
# total     = 560
# last_year = 500

# print(total > last_year)   # True  — 560 is greater than 500
# print(total == last_year)  # False — 560 is not equal to 500
# print(total >= last_year)  # True  — 560 is at least as good
# print(total < 400)         # False — 560 is not less than 400

# total = 560        # = stores 560 into total
# total += 30        # same as: total = total + 30
# print(total)       # Output: 590
# total -= 15        # same as: total = total - 15
# print(total)       # Output: 575
# #double slashes // only gives the round value without decimal 
# bags = total // 25 # recalculate bags after update
# print(bags)        # Output: 23


#percentage
marks=45
total =50
percentage = (marks/total)*100
print(percentage)

#Square root 
import math 
number = 25
answer = math.sqrt(number)
print(answer)


# ============================================================
# Farm Harvest Calculator
# ============================================================

# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest
total   = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest      :", total, "kg")
print("Average per field  :", average, "kg")

# Price per kg is 15 rupees — calculate total earnings
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings     : Rs.", earnings)

# --- Floor Division (//) and Modulus (%) ---
# Pack the harvest into bags of 25 kg each
bags     = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover grain     :", leftover, "kg")

# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop   :", total, "kg")

# Subtract 15 kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed  :", bags)


#odd and even 

num = int(input("Enter a number to check if its even or odd : "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")

