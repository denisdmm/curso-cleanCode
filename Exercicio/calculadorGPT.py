import os


class Calculator:
    """Classe responsável por operações matemáticas básicas."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float):
        if a == 0 and b == 0:
            return "Indeterminação (0/0)"
        if b == 0:
            return "Erro: divisão por zero não permitida!"
        return a / b


def clear_screen():
    """Limpa a tela do terminal (Windows, Linux, Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu() -> None:
    """Exibe o menu de opções da calculadora."""
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")


def get_number(prompt: str) -> float:
    """Lê um número do usuário com tratamento de erro."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def execute_operation(option: str, calculator: Calculator) -> None:
    """Executa a operação escolhida pelo usuário."""
    a = get_number("Digite o primeiro número: ")
    b = get_number("Digite o segundo número: ")

    operations = {
        "1": ("Soma", calculator.add),
        "2": ("Subtração", calculator.subtract),
        "3": ("Multiplicação", calculator.multiply),
        "4": ("Divisão", calculator.divide),
    }

    operation_name, operation_func = operations[option]
    result = operation_func(a, b)

    print(f"Resultado da {operation_name}: {result}")


def main():
    calculator = Calculator()

    while True:
        clear_screen()
        show_menu()
        option = input("Escolha uma operação (1-4): ").strip()

        if option not in {"1", "2", "3", "4"}:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
            continue

        execute_operation(option, calculator)

        choice = input("\nDigite 'sair' para encerrar ou pressione Enter para continuar: ").strip().lower()
        if choice == "sair":
            print("Encerrando a calculadora... Até logo!")
            break


if __name__ == "__main__":
    main()
