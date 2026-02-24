print("hello lil white")


# 1 - crie variaveis que representem 
# sua idade
idade = 18
# sua altura
altura = 1.85
# Seu Nome
nome = 'Felipe'
# se voce é estudante 
eh_estudante = True
# para ver tipo de variável
type(eh_estudante)

# 2 - o usuário digita sua idade
# -   conversão essa entrada para número inteiro
idade = int(input("Digite a sua idade:"))
idade = int(idade) + 5
print(idade)

#3.  Soma de Números Inteiros:
#Leia dois números inteiros e exiba a soma deles. 
#Entrada: Dois números inteiros. 
#Saída: A soma dos dois números. 
#Exemplo: Entrada: 3, 5 Saída: 8
num1 = input("Digite o primeiro número")
num2 = input("Digite o segundo número")
num1 =int(num1)
num2 =int(num2)
Soma = num1 + num2
print(f"A soma é igual a: {Soma}")

#4.  Média de Três Números Inteiros Enunciado:
#Escreva um programa que leia três números inteiros e determine a média deles. 
#Entrada: Três números inteiros.
#Saída: Média dos três números.
n1 = int(input("digite o primeiro numero"))
n2 = int(input("digite o Segundo numero"))
n3 = int(input("digite o Terceiro numero"))
media = (int(n1)+int(n2)+int(n3))/3
print(f"A Media é: {media}")

#5. Média Ponderada (Padrão Ibmec):
#Escreva um programa que receba as 3 notas das avaliações dos alunos e determine a média final através da ponderação padrão do Ibmec. 
#Entrada: Três números (notas). 
#Saída: Nota Final. 
ap1 = int(input("digite o primeiro numero"))
ap2 = int(input("digite o Segundo numero"))
ac = int(input("digite o Terceiro numero"))
media_ponderada = round((ap1*0.4) + (ap2*0.4) + (ac*0.2), 2)
print(f"a sua media é: {media_ponderada}")
if media_ponderada >= 7:
    print("Aprovado")
else:
    print("You're COOKED")

#6.  Manipulação de Strings:
#Peça o nome completo do usuário.
#-   Mostre o nome em letras maiúsculas.
#-   Mostre apenas o primeiro nome.
#-   Mostre a quantidade de letras do nome (sem contar os espaços).
Nome = input("digite seu nome completo")
Nome.upper()
nome.slit()[0]
len(nome)
