#TO DO: PASS a dictionary of card numbers to this function to calculate and validate

def validate_creditCard_check_digit(): 
# get the card number as an input
    cardNumber=input('add your card number to validate: ')
# pass the number to a list to split the digits
    temp = [int(x) for x in str(cardNumber)] 
    print(temp) 
    number_len=len(temp)
    print(number_len)
# from right get every second digit
    result=0
    total=0
    checkDigit= temp[-1]
    validate_on_list=sorted(temp[-2::-2] , reverse= True)
    print(validate_on_list)
    for item in validate_on_list:
        result=item*2
        print(result)
        if result>9:
            result-=9
        else:
            total+=result
    print(total)
    validator=(checkDigit+total)%10
    print(validator)
    if validator==0:
        print ('Valid CardNamber')
    else:    
        print ('invalid card Namber')

# if digit*2 = result > 9 => x = x[0]+x[1] or result-=9 , these are products
# sum up all products together = total
# (checkDigit+ total)%10==0
# if last digit is == checkDigit 
#then return true 
def calculate_gcreditCard_check_digit():
#get the card number as in input
    cardNumber= input('add your card number to calculate the check digit: ')
#create a list and pass the card number to the list , splits each digit to a cell in the list
    temp=[int(x) for x in cardNumber]
#keep the last digit as actual check digit or remove it
    number_len=len(temp)
    calculate_on_list=temp[:number_len]
# clculate the check digit
    total=0
    # sum up all the digits in the list 
    for item in calculate_on_list:
        total+=item
    # (sum *9)%10= check digit
    print((total*9)%10)
#return the check digit    


validate_creditCard_check_digit()
calculate_gcreditCard_check_digit()
