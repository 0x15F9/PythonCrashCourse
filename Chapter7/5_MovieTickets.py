def get_fee(age):
    """Function which returns the fee based on the age"""
    if age < 3 :
        fee = 0
    elif age > 3 and age < 12:
        fee = 10
    else:
        fee = 15
    
    return(fee)

age = 0
while age != -1:
    age = int(input("How old are you?\n"))
    print(get_fee(age))