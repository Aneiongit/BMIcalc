


# title
print('\nCalorie calculator :)\n')

# base data
height = int(input('Please provide your height in centimeters: '))
weight = int(input('Please provide your weight in kilograms: '))
age = int(input('Please provide your age: '))


# Basal Metabolic Rate calculation
def BMRW():
    BMRW = 10 * weight + 6.25 * height - 5 * age - 161  # for women
    print(f"Your daily calories intake: {BMRW}")

def BMRM():
    BMRM = 10 * weight + 6.25 * height - 5 * age + 5  # for men
    print(f"Your daily calories intake: {BMRM}")


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

BMRW()
BMRM()

# opcja trybu zycia do obliczenia zapotrzebowania kalorycznego
print('\nAby obliczyc zapotrzebowanie, wybierz jeden z ponizszych trybow zycia: ')
print('1.2: Praca siedząca, brak dodatkowej aktywności fizycznej')
print('1.4: Praca niefizyczna, mało aktywny tryb życia')
print('1.6: Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu')
print('1.8: Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu')
print('2.0: Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu')

tryb = input('\nWybierz tryb zycia: ')

# obliczanie zapotrzebowania kalorycznego dla mezczyzny i kobiety
zapotrzebowanieK = (BMRW()*float(tryb))
zapotrzebowanieM = (BMRM()*float(tryb))
print("\nDziennie zapotrzebowanie kaloryczne dla kobiety:", zapotrzebowanieK, 'kalorii.')
print("\nDziennie zapotrzebowanie kaloryczne dla mezczyzny:", zapotrzebowanieM, 'kalorii.')

