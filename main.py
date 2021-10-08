


# title
print('\nCalorie calculator :)\n')

# base data
height = int(input('Please provide your height in centimeters: '))
weight = int(input('Please provide your weight in kilograms: '))
age = int(input('Please provide your age: '))


# Basal Metabolic Rate calculation
def BMRW():
    BMRW = 10 * weight + 6.25 * height - 5 * age - 161  # for women
    return BMRW


def BMRM():
    BMRM = 10 * weight + 6.25 * height - 5 * age + 5  # for men
    return BMRM


# BMI calculation
BMI = (weight/((height/100)**2))
print('\nYour Body Mass Index (BMI) is: ', round(BMI, 2), "and you are "  .format(BMI), end="")

# BMI description
if BMI < 18:
    print(" underweight.")
elif 18.5 <= BMI < 25:
    print(" healthy.")
elif 25 >= BMI < 30:
    print(" overweight.")
elif BMI >= 30:
    print(" obese.")

print(f"Your daily calories intake: {BMRW()}")
print(f"Your daily calories intake: {BMRM()}")

# opcja trybu zycia do obliczenia zapotrzebowania kalorycznego
print('\nActivity level: ')
print('1.2: Sedentary: little or no exercise')
print('1.4: Exercise 1-3 times/week')
print('1.6: Exercise 4-5 times/week')
print('1.8: Daily exercise or intense exercise 3-4 times/week, total of 7hrs a day')
print('2.0: Intense exercise 6-7 times/week')

tryb = input('\nChoose your activity level: ')

# obliczanie zapotrzebowania kalorycznego dla mezczyzny i kobiety
zapotrzebowanieK = ((BMRW())*float(tryb))
zapotrzebowanieM = ((BMRM())*float(tryb))
print("\nDziennie zapotrzebowanie kaloryczne dla kobiety:", zapotrzebowanieK, 'kalorii.')
print("\nDziennie zapotrzebowanie kaloryczne dla mezczyzny:", zapotrzebowanieM, 'kalorii.')

