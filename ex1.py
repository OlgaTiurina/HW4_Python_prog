# Вычислить число c заданной точностью d

accur = float(input('Введите число точности округления: '))
number = float(input('Введите число, котрое будем округлять: '))
accur = str(accur)
accur = accur.split('.')
accur = len(accur[1])
print('Result: ', round(number, accur))