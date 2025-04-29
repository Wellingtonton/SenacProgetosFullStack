def obter_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Valor inválido! Por favor, insira um número inteiro.")

def e_par(numero):
    return numero % 2 == 0 
def soma_pares_no_intervalo(inicio, fim):
    soma = 0
    
    for numero in range(inicio, fim + 1):
        if e_par(numero):  
            soma += numero 
    return soma

def programa_soma_pares():
    print("Bem-vindo ao programa de soma de números pares!")

    inicio = obter_numero("Digite o início do intervalo: ")
    fim = obter_numero("Digite o fim do intervalo: ")

    if inicio > fim:
        print("O início do intervalo não pode ser maior que o fim. Tentando novamente.")
        return

    soma = soma_pares_no_intervalo(inicio, fim)

    print(f"\nA soma dos números pares entre {inicio} e {fim} é: {soma}")

programa_soma_pares()
