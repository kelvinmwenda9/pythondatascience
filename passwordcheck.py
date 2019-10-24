import re # search library
def passwordCheck(password):
    if len(password)==0:
        print('Password must be more than 8 characters')
    elif not re.search('[A-Z]', password):
        print('There is no capital')
    elif not re.search('[a-z]', password):
        print('there is no small')
    elif not re.search('[0-9]', password):
        print('THere is no number')
    elif not re.search('[!@#$%^&*]', password):
        print('there is no special character')
    else:
        print('Password is correct')


passwordCheck(password='128Tg38@3')
