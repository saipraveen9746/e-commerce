"""2.To check a number is palindrome or not"""

num = int(input("enter the number"))
rev = 0
temp = num
while num>0:
    reminder = num%10
    rev = (rev*10)+reminder
    num = num//10
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")