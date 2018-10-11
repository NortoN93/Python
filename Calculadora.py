print("Calculadora")

opção = " "
resultado = " "
operação = " "

def soma(num1,num2):
    resultado = num1 + num2
    return resultado

def subtração(num1,num2):
    resultado = num1 - num2
    return resultado

def multiplicação(num1,num2):
    resultado = num1 * num2
    return resultado

def divisão(num1,num2):
    resultado = num1 / num2
    return resultado


while opção != 'N':
    num1 = float(input("Digite um número:\n"))
    while operação not in ['+','-','*','/']:
        operação = (input("Digite uma operação matemática:\n"
                        "+ p/ soma\n"
                        "- p/ subtração\n"
                        "x p/ multiplicação\n"
                        "/ p/ divisão\n"))

    num2 = float(input("Digite um número:\n"))

    if operação == '+':
        resultado = soma(num1,num2)
    elif operação == '-':
        resultado = subtração(num1,num2)
    elif operação == '*':
        resultado = multiplicação(num1,num2)
    elif operação == '/':
        resultado = divisão(num1,num2)


    print(resultado)

    while opção not in ['S','N']:
        opção = input("Deseja fazer outra conta ?\n"
                  "s p/ sim\n"
                  "n p/ não\n")
        opção = opção.upper()
        print(opção)

    operação = " "
    opção = " "

