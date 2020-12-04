a = 0
while a == 0:
    x = input ()
    b = x.isnumeric()
    if b == True:
        x = int(x)
        if (x >= 1) and (x <4000):
            print(int_to_Roman(x))
        else:
            print ("Not Valid Input!!! Please enter valid input (1-3999) :")
            print("To exit the program, please type 'exit'")
            print("Please enter a number between 1 and 3999, inclusively :")
    elif b == False :
        x = str(x)
        x = x.title()
        if x == "Exit":
            print("Exiting the program... Good Bye")
            a = 1
            break
        else:
            print ("Not Valid Input!!! Please enter valid input (1-3999) :")
            print("To exit the program, please type 'exit'")
            print("Please enter a number between 1 and 3999, inclusively :")

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def int_to_Roman():

    roman = ''

    while 4000 > num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman




print(int_to_Roman(x))