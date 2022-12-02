from time import sleep
from math import sqrt
def startup():
    print('Cal-cue-lator')
    for i in range(3):
        sleep(0.75) 
        print('...')
    print('Welcome to Cal-cue-lator')

def add():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    total = a + b
    print('The total is: ', total)
    ask = input('\nWould you like to do more? [y/n]: ')
    print('\n')
    if ask == 'y' or ask == 'Y':
        add()
    elif ask == 'n' or ask == 'N':
        main()

def sub():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    total = a - b
    print('The total is: ', total)
    ask = input('\nWould you like to do more? [y/n]: ')
    print('\n')
    if ask == 'y' or ask == 'Y':
        sub()
    elif ask == 'n' or ask == 'N':
        main()

def mult():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    total = a * b
    print('The total is: ', total)
    ask = input('\nWould you like to do more? [y/n]: ')
    print('\n')
    if ask == 'y' or ask == 'Y':
        mult()
    elif ask == 'n' or ask == 'N':
        main()

def div():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    total = a / b
    print('The total is: ', total)
    ask = input('\nWould you like to do more? [y/n]: ')
    print('\n')
    if ask == 'y' or ask == 'Y':
        div()
    elif ask == 'n' or ask == 'N':
        main()

def sqre():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    total = a ** b
    print('The total is: ', total)
    ask = input('\nWould you like to do more? [y/n]: ')
    print('\n')
    if ask == 'y' or ask == 'Y':
        sqre()
    elif ask == 'n' or ask == 'N':
        main()

def squirt():
    a = int(input('Enter number: '))
    total = sqrt(a) 
    print('The total is: ', total)
    ask = input('\nWould you like to do more? [y/n]: ')
    print('\n')
    if ask == 'y' or ask == 'Y':
        squirt()
    elif ask == 'n' or ask == 'N':
        main()

def menu():
    print('--------------------------------------------------\n')
    sleep(0.75)
    print('Menu Options:')
    print('------------\n')
    print(' 1. Addition\n',
            '2. Subtraction\n',
            '3. Mutiplication\n',
            '4. Divistion\n',
            '5. Square\n',
            '6. Square Root\n',
            '7. Close program\n')

    try:
        menu_option = int(input('Please choose a menu option for your math function: '))
        
        if menu_option == 1:
            return add()
        elif menu_option == 2:
            return sub()
        elif menu_option == 3:
            return mult
        elif menu_option == 4:
            return div()
        elif menu_option == 5:
            return sqre()
        elif menu_option == 6:
            return squirt()
        elif menu_option == 7:
            print('Thank you for using Cal-cue-lator')
        else:
            print('Sorry, that is not a menu option. Please choose a menu option.')
            return menu()
    except:
        print('Sorry, that is not a menu option. Please choose a menu option.')
        return menu()



def main():

    startup()
    menu()

main()