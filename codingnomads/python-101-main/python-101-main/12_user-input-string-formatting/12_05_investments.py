# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
amount= int(input("Input the amount you wish to invest:"))
rate= int(input("Input the rate in percentage of the investment:"))
years= int(input("Input number of years to invest in:"))
print((amount*rate)//100*years)