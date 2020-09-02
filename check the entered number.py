while True:
    usernumber = input('Please enter a number between 0-4000: ')
    if not usernumber.isdigit():
        print('please enter a correct type of number:')
    elif 0 < int(usernumber) < 4000:
        print('Please enter a number between 0-4000:')