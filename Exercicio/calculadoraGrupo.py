class Calculadora():
    """
        Essa é uma classe para calcular dois números
    """
    
    def somar(self, num_1, num_2):
        return num_1 + num_2

    def subtrair(self, num_1, num_2):
        return num_1 - num_2

    def multiplicar(self, num_1, num_2):
        return num_1 * num_2

    def dividir(self, num_1, num_2):
        if num_2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return num_1 / num_2

if __name__ == "__main__":

    calc = Calculadora()
    num1 = int(input("Selecione numeros entre 0 e 9: "))
    num2 = int(input("Selecione numeros entre 1 e 9: "))
 
    print("Soma: ", calc.somar(num1, num2))
    print("Subtrai: ", calc.subtrair(num1, num2))
    print("Multiplica: ", calc.multiplicar(num1, num2))
    print("Divide: ", calc.dividir(num1, num2))