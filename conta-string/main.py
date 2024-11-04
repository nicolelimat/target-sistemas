def contar_a(texto):
    contador = texto.lower().count("a")
    return contador


texto = input("Informe uma string: ")
quantidade_a = contar_a(texto)
print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
