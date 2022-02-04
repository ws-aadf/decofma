varx = 1
while varx == 1:
    try: 
        oper = input(
            '''
                Selecione qual operação a ser realizada:
                + ---> somar
                - ---> subtrair
                * --- multiplicar
                / ---> dividir
            ''')
        if oper=='*' or oper=='-' or oper=='+' or oper=='/':
            number_1 = int(input('Digite o primeiro número: '))
            number_2 = int(input('Digite o segundo número: '))

            if oper == '+':
                print('{} + {} = '.format(number_1, number_2))
                print(number_1 + number_2)

            elif oper == '-':
                print('{} - {} = '.format(number_1, number_2))
                print(number_1 - number_2)

            elif oper == '*':
                print('{} * {} = '.format(number_1, number_2))
                print(number_1 * number_2)

            elif oper == '/':
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
        else: 
            print('Selecione um operador válido e tente novamente.')

        varx = int(input('Deseja continuar? (1=s / 2=n)'))

        if varx == 2:             
            print('Fim de execução.')
            break
        elif varx == 1:
            continue
        elif varx != 2 or varx !=1: 
            print('selecionou um valor não existente, a operação continuará.')
            varx = 1
            continue
    except ValueError as e:
        print ('error type: ', type (e))