try:
    num1 = int(raw_input("First Number : "))
    num2 = int(raw_input("Second Number: "))
    add = num1+num2
    print('The sum of {} and {} is {}'.format(num1, num2, add)) 
except ValueError as v:
    print("Invalid input! Only numbers are accepted.")
