import sys

class Calculadora:

    """
    Essa é uma classe para calcular dois números

    """

    # Soma dois números
    def somar(self: float, primeiro_numero: float, segundo_numero: float) -> float:
        return primeiro_numero + segundo_numero

    # Subtrai dois números
    def subtrair(self: float, primeiro_numero: float, segundo_numero: float) -> float:
        return primeiro_numero - segundo_numero

    # Multiplica dois números
    def multiplicar(self: float, primeiro_numero: float, segundo_numero: float) -> float:
        return primeiro_numero * segundo_numero

    # Divide dois números
    def dividir(self: float, primeiro_numero: float, segundo_numero: float) -> float:
        try:
            return primeiro_numero / segundo_numero
        except ZeroDivisionError:
            raise ValueError("Divisão por zero não é permitida.")
    
if __name__ == "__main__":
    calc = Calculadora()

    primeiro_numero = int(input('Digite o primeiro número: '))

    print("Escolha uma operação: ")
    print("+ (Soma)")
    print("- (Subtração)")
    print("* (Multiplicação)")
    print("/ (Divisão)")

    operacao = str(input("Digite o número da operação desejada: "))

    segundo_numero = int(input('Digite o segundo número: '))

    switcher = {
        '+': calc.somar(primeiro_numero, segundo_numero),
        '-': calc.subtrair(primeiro_numero, segundo_numero),
        '*': calc.multiplicar(primeiro_numero, segundo_numero),
        '/': calc.dividir(primeiro_numero, segundo_numero)
    }

    if operacao in switcher:
        print("O resultado é: ", switcher[operacao])    
    else:
        print("Operação inválida")
