# Enter the card number by User and use .strip() for unwanted spaces
card_number = list(input("Enter the card number :").strip())
# Remove the last digit i.e check digit
check_digit =(card_number.pop())
#Reverse the card_number
card_number.reverse()
# make an empty list 
future_use = []
#check for the even index and odd Index
for index,digit in enumerate (card_number) :
  if index % 2 == 0 :
     #  make an even value double 
     double_digit = int(digit) * 2
     #if double digit is greater than 9 then substract it from 9
     if double_digit > 9 :
      double_digit = double_digit - 9

     future_use.append(double_digit)    
  else :
     # odd number value remains same
   future_use.append(int(digit))

total = int(check_digit) + sum(future_use)
print(total)
 # check the number is divisible by  10 or not
if total % 10 == 0 :
   print(" The card number valid")
else :
   print("The card number invalid")