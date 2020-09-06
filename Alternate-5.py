
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

a = 0
while a == 0:
    print('\nThis program converts decimal numbers to Roman Numerals. \nTo exit the program, please type "exit"')
    x = input ('\nPlease enter a number between 1 and 3999: ')
    b = x.isnumeric()
    if b == True:
        x = int(x)
        if (x >= 1) and (x <4000):
            roman = ''
            for i, r in num_map:
                while x >= i:
                    roman += r
                    x -= i
            print(roman)
            break
        else:
            print ("Not Valid Input!!!")
    elif b == False :
        x = str(x)
        x = x.title()
        if x == "Exit":
            print("Exiting the program... Good Bye")
            a = 1
            break
        else:
            print ("Not Valid Input!!!")



