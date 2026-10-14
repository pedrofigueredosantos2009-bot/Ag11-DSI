from colorama import Fore, Style, init

init(autoreset=True)



niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE


for i in range(len(niveis)):
    cor = definir_cor(i + 1)
    mensagem = niveis[i]
    print(cor + f"Nível {i + 1}: {mensagem}" + Style.RESET_ALL)
