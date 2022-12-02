import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
nums = '1234567890'
spec_char = '!@#$%^&*()?<>-_'

string = lower + upper + nums + spec_char
pass_len = 15

while True:
    try:
        ask = int(input('How many passwords would you like?: '))
        print('-----------------------------------\n')
        if ask == 0:
            print('INVALID INPUT!!\n')
        
        else:
            with open('Generated Passwords.txt', 'a+') as file:
                file.write('Generated Password(s) for this session:\n')

                for line in range(ask):
                    password = ''.join(random.sample(string, pass_len))
                    print(password, file = file)
                
                file.write('\n')
                
                print('Password(s) have been stored in file successfully!!\nSee text file for password(s)')
            file.close()
            break

    except:
        print('INVALID INPUT!!\n')