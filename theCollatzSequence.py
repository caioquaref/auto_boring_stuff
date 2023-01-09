def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
print('\nBem vindo à sequencia de Collatz!\n\nDigite um número e quando o resultado de sua divisão por 2 for igual a 1, o programa será concluído.\n\nPesquise no google.com sobre a sequencia de Collatz!')

state = True

while state:
    try:
        choosen_number = input("Escolha um número inteiro: ")
        result = collatz(int(choosen_number))
        if result == 1:
            quit('O resultado da divisão de ' + choosen_number + ' por 2 é: ' + str(result) + '.\n\nEncerrando o programa, bye bye!.')
        else:
            print('O resultado da divisão de ' + choosen_number + ' por 2 é: ' + str(result) + '.\n\nContinue tentando!')

    except ValueError:
        print("O valor inserido precisa ser um número inteiro.")