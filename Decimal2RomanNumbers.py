

usernumber = input('Please enter a number: ')
str_usernumber = str(usernumber)
int_usernumber = int(usernumber)
list_usernumber = list(str_usernumber)
list_romannumber =[] 
# len_usernumber = len(usernumber)
digit1 = list_usernumber[-1]



def def1digit(digit1):
    if digit1 == '1':
        list_romannumber.append('I')
    elif digit1 == '2':
        list_romannumber.append('II')
    elif digit1 == '3':
        list_romannumber.append('III')
    elif digit1 == '4':
        list_romannumber.append('IV')
    elif digit1 == '5':
        list_romannumber.append('V')
    elif digit1 == '6':
        list_romannumber.append('VI')
    elif digit1 == '7':
        list_romannumber.append('VII')
    elif digit1 == '8':
        list_romannumber.append('VIII')
    elif digit1 == '9':
        list_romannumber.append('IX')
    else:
        print('1 d Hata Mesajı')



def def10digit(digit10):
    digit10 = list_usernumber[-2]
    if digit10 == '1':
        list_romannumber.append('X')
    elif digit10 == '2':
        list_romannumber.append('XX')
    elif digit10 == '3':
        list_romannumber.append('XXX')
    elif digit10 == '4':
        list_romannumber.append('XL')
    elif digit10 == '5':
        list_romannumber.append('L')
    elif digit10 == '6':
        list_romannumber.append('LX')
    elif digit10 == '7':
        list_romannumber.append('LXX')    
    elif digit10 == '8':
        list_romannumber.append('LXXX')
    elif digit10 == '9':
        list_romannumber.append('XC')

    else:
        print('Hata 10d Mesajı')
    def1digit(digit1)    



def def100digit(digit100):
    digit10 = list_usernumber[-2]
    digit100 = list_usernumber[-3]
    if digit100 == '1':
        list_romannumber.append('C')
    elif digit100 == '2':
        list_romannumber.append('CC')
    elif digit100 == '3':
        list_romannumber.append('CCC')
    elif digit100 == '4':
        list_romannumber.append('CD')
    elif digit100 == '5':
        list_romannumber.append('D')
    elif digit100 == '6':
        list_romannumber.append('DC')
    elif digit100 == '7':
        list_romannumber.append('DCC')    
    elif digit100 == '8':
        list_romannumber.append('DCCC')
    elif digit100 == '9':
        list_romannumber.append('CM')

    else:
        print('Hata 100 Mesajı')    
    def10digit(digit10)
    





def def1000digit(digit1000):
    digit10 = list_usernumber[-2]
    digit100 = list_usernumber[-3]
    digit1000 = list_usernumber[-4]
    if digit1000 == '1':
        list_romannumber.append('M')
    elif digit1000 == '2':
        list_romannumber.append('MM')
    elif digit1000 == '3':
        list_romannumber.append('MMM')
    else:
        print('Hata 1000 mesajı')
    def100digit(digit100)



if 0 < int_usernumber < 4000: 
    if len(usernumber) == 1:
        def1digit(usernumber)
    elif len(usernumber) == 2:
        def10digit(usernumber)
    elif len(usernumber) == 3:
        def100digit(usernumber)
    elif len(usernumber) == 4:
        def1000digit(usernumber)
else:
    print('Hata fff kodu')


romannumber = ''.join(list_romannumber)

print('The number', str_usernumber, 'is: ', romannumber)
