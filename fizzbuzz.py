def calculate(number):
    if not number % 15:
        print('fizzbuzz')
    elif not number % 5 :
        print('buzz')
    elif not number % 3:
        print('fizz')
    else:
        print(number)

for output in [number for number in range(1,101)]:
    calculate(output)
