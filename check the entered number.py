# while True:
#     usernumber = input('Please enter a number between 0-4000: ')
#     if not usernumber.isdigit():
#         print('please enter a correct type of number:')
#     elif 0 < int(usernumber) < 4000:
#         print('Please enter a number between 0-4000:')


num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

usernumber = input('Enter a number: ')
int_usernumber = int(usernumber)


if type(usernumber) == Str:
    print('please enter a correct type of number:')


def num2roman(num):

    roman = ''

    while 4000 > num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman




print(num2roman(int_usernumber))
print(type(usernumber))