# ----- MÓDULOS -----
import sys

# ----- ENTRADA DE DADOS -----
def entrada():
    print('---   SISTEMA DE CONVERSÃO NUMÉRICA   ---')
    print('-' * 40)
    print('''ESCOLHA O MÉTODO DE CONVERSÃO ABAIXO
[ 1 ] Binário p/ decimal
[ 2 ] Decimal p/ binário
[ 0 ] Encerrar o programa''')
    sistema = input('Método de conversão: ')
    while sistema != '1' and sistema != '2' and sistema != '0':
        print('\033[31m' + 'ERRO! Opção inválida.' + '\033[0;0m')
        sistema = input('Método de conversão: ')
    if sistema == '1':
        num = input('Digite o número binário que será convertido para decimal: ')
    if sistema == '2':
        num = input('Digite o número decimal que será convertido para binário: ')
    if sistema == '0':
        print('\033[31m' + 'PROGRAMA ENCERRADO!' + '\033[0;0m')
        sys.exit()    
    return num, sistema
    
# ----- VERIFICAÇÃO -----
num, sistema = entrada()
while not ((sistema == '2' and num.isdigit()) or \
           (sistema == '1' and all(n in '01' for n in num))):
    print('\033[31m' + 'ERRO! Incorreção nos valores digitados.' + '\033[0;0m')
    num, sistema = entrada()

# ----- CONVERSORES -----

# BINÁRIO -> DECIMAL
def bin_para_dec(num_bin):
    num_dec = 0
    for digit in range(0, len(num_bin)):
        num_dec += int(num_bin[digit]) * 2 ** (len(num_bin) - 1 - digit)
    return num_dec

# DECIMAL -> BINÁRIO
def dec_para_bin(num_dec):
    num_dec = int(num_dec)
    num_bin = ''
    if num_dec == 0:
        return 0
    else:
        while num_dec != 0:
            num_bin = str(num_dec % 2) + num_bin
            num_dec //= 2
    return num_bin

# ----- SAÍDA DE DADOS -----
if sistema == '1':
    saida = str(bin_para_dec(num))
    print(f'O decimal correspondente ao binário {num} é {saida}.')
else:
    saida = dec_para_bin(int(num))
    print(f'O binário correspondente ao decimal {num} é {saida}.')
