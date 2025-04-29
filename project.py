def obter_nota(nota_numero):
    while True:
        try:
            nota = float(input(f"Digite a {nota_numero}ª nota: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")

def calcular_media(notas):
    soma = sum(notas)
    return soma / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def programa_notas():
    print("Bem-vindo ao sistema de avaliação!")
    
    notas = []
    for i in range(1, 5):
        nota = obter_nota(i)
        notas.append(nota)

    media = calcular_media(notas)
    
    print(f"\nA média das notas é: {media:.2f}")
    status = verificar_aprovacao(media)
    print(status)

programa_notas()
