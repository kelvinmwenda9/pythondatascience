def simple_interest():
    principle = 4500
    rate = 89
    time = 24
    answer = principle * rate * time
    print('Your interest is ', answer)


# create a function to check the largest number from 3 variables
def bmi():
    h = 1.74
    w = 65.5
    BMI = w / h * h
    print(BMI)


def largest_Variable():
    x = int(input("Enter value of x"))
    y = int(input("Enter value of y"))
    z = int(input("Enter value of z"))
    if x > y and x > z:
        print("x is the largest")
    elif y > x and y > z:
        print("y is the largest")
    elif z > x and z > y:
        print("z is the largest")
    else:
        print("All are equal")


def multi(x, y):
    multiple = x * y
    print(multiple)


# use your function/ call your function/ invoke a function
# simple_interest()  - functions are being used externally
# largest_Variable()
# bmi()

def bmi(height, weight):
    bMI = weight / (height * height)
    print(bMI)
    if bMI < 18.5:
        print('You are underweight')
    elif bMI >= 18.5 and bMI <= 24.5:
        print('you are normal')

    elif bMI > 24.5 and bMI <= 28:
        print('You are overweight')
    else:
        print('You are obese')


