1.  #Addition (+)
# This is to Prompt the user to enter two numbers and store them as num1 and num2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
Answer = num1 + num2
print(f"The sum of {num1} and {num2} is: {Answer}")

#2. Subtraction (-)
#This will subtract num2 from num1 to get the difference
Answer = num1 - num2
print(f"The difference of {num1} and {num2} is: {Answer}")

#3. Multiplication (*)
#This will multiply num1 and num2 to get the product
Answer = num1 * num2    
print(f"The product of {num1} and {num2} is: {Answer}") 

#4. Division (/)
# Check if either number is zero before performing division to avoid division by zero error
if num1 == 0 or num2 == 0:
  print("Error: You cannot divide by zero.")
# If both numbers are non-zero, perform the division
else:
  #This will divide num1 by num2 to get the quotient
  Answer = num1 / num2
  print(f"The quotient of {num1} and {num2} is: {Answer}")   
