
def exibir_titulo():
    print("=" * 40)
    print("        VERIFICADOR DE PALÍNDROMO        ")
    print("=" * 40)

def solicitar_entrada():
    while True:
        texto = input("\nDigite uma palavra ou frase: ").strip()
        if texto == "":
            print("Entrada vazia! Por favor, digite algo.")
        else:
            return texto

def limpar_texto(texto):
    texto = texto.lower()
    caracteres_validos = []

    for letra in texto:
        if letra.isalnum(): 
            caracteres_validos.append(letra)

    texto_limpo = ''.join(caracteres_validos)
    return texto_limpo
def inverter_texto(texto):
    invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        invertido += texto[i]
    return invertido

def verificar_palindromo(texto_original):
    texto_formatado = limpar_texto(texto_original)
    texto_invertido = inverter_texto(texto_formatado)

    print(f"\nTexto formatado: {texto_formatado}")
    print(f"Texto invertido : {texto_invertido}")

    if texto_formatado == texto_invertido:
        return True
    else:
        return False

def programa_palindromo():
    exibir_titulo()
    entrada = solicitar_entrada()

    resultado = verificar_palindromo(entrada)

    print("\nResultado:")
    if resultado:
        print("✅ É palíndromo!")
    else:
        print("❌ Não é palíndromo.")

    print("\nObrigado por usar o verificador!")

programa_palindromo()
