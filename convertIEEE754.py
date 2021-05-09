def convert_to_IEEE():
    var = float(input("Digite um número real: "))
    var = str(var)
    binary = ''
    binary_no = ''
    point = ''
    sign = var.find('-') + 1

    try:
        point = float('0.' + (var.split('.'))[1])

        ''' find binary of the values after the decimal'''
        while (float((str(point).split('.'))[1]) != 0):
            point = point * 2
            binary = binary + (str(point).split('.'))[0]
            point = float('0.' + (str(point).split('.'))[1])
        binary_no = bin(int(var.split('.')[0]))[3:] + binary
        data = int(bin(int(var.split('.')[0]))[2:])

        '''find the value of exponent'''
        expo = len(str(data)) - 1

        '''converting exponant to excess/bias notation'''
        expo = expo + 127

        '''adding additional 0's to the output binary'''
        binary_no = binary_no + '0' * (23 - len(binary_no))

        print('Output:', sign, '|', bin(expo)[2:], '|', binary_no)

    except Exception as e:
        print('\033[31mERRO: ', e.args, '\033[m')


def float_bin(number, places=24):
    try:
        wholenumber, decimalnumber = str(number).split(".")

        wholenumber = int(wholenumber)
        decimalnumber = int(decimalnumber)

        res = bin(wholenumber).lstrip("0b")
        print(f'decimalnumber: {decimalnumber}')
        print(f'wholenumber: {wholenumber}')
        print(f'res: {res}')
        print('')
        for x in range(places):
            wholenumber, decimalnumber = str((decimal_converter(decimalnumber)) * 2).split(".")
            decimalnumber = int(decimalnumber)
            res = str(res + wholenumber)
            print(decimalnumber, end='')
        print('')
        print(f'decimalnumber: {decimalnumber}')
        print(f'wholenumber: {wholenumber}')
        print(f'res: {res}')

        if res[0] == '1':
            res = res[1:24]
        else:
            res = res[0:23]
        # #expo = len(str(res)) - 1
        expo = 8
        expo += 127
        expo = bin(expo).lstrip("0b")
        print(f'res: {res}')
        ieee = str(f'{sign}{expo}{res}')
        return ieee

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
        n = float(input('Digite um número float: '))
        if n < 0:
            sign = '1'
        else:
            sign = '0'
        print(f'\nValor {n} convertido para IEEE754: {float_bin(n)}')

    else:
        print('\n\033[32mPrograma finalizado..\033[m')
        break
