# res: str = '0Guilherme Balduino Lopes'
#
# if res[0] == '1':
#     res = res[1:24]
# else:
#     res = res[0:23]
#
# print(f'{res}')
def float_bin(number, places=3):
    try:
        wholenumber, decimalnumber = str(number).split(".")

        wholenumber = int(wholenumber)
        decimalnumber = int(decimalnumber)

        res = bin(wholenumber).lstrip("0b") + "."
        print(f'res: {res}')
        print('')
        for x in range(places):
            wholenumber, decimalnumber = str((decimal_converter(decimalnumber)) * 2).split(".")
            decimalnumber = int(decimalnumber)
            res = str(res + wholenumber)
        print(f'res: {res}')
        if res[0] == '1':
            res = res[1:24]
        else:
            res = res[0:23]
        # #expo = len(str(res)) - 1
        # expo = 8
        # expo += 127
        # expo = bin(expo)
        return res

    except Exception as e:
        print('\033[31mERRO: ', e.args, '\033[m')


def decimal_converter(num):
    try:
        while num > 1:
            num /= 10
        return num
    except Exception as e:
        print('\033[31mERRO: ', e.args, '\033[m')


while True:
    resp = str(input('Deseja converter um valor? [S/N]: ')).upper()[0]
    if resp != 'N':
        n = input('Digite um número float: ')
        p = int(input('Número de casas decimais: '))
        print(float_bin(n, places=p))

    else:
        print('Programa finalizado..')
        break
