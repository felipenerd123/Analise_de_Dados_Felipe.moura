#1. par ou impar
# leia um número inteiro e informe se 
num1 = 11
if num1 % 2 == 0: 
    print("o numero é par")
else:
    print("o numero é impar")

#2. Aprovado ou Reprovado
#Leia a nota final de um aluno e diga se ele está:
#- Aprovado, se a nota for maior ou igual a 7.
#- Reprovado, se a nota for menor que 7.
ap1 = float(input("digite o primeiro numero"))
ap2 = float(input("digite o Segundo numero"))
ac = float(input("digite o Terceiro numero"))
media_ponderada = ((ap1*0.4) + (ap2*0.4) + (ac*0.2), 2)
print(f"a sua media é: {media_ponderada}")
if media_ponderada >= 7:
    print("Aprovado")
else:
    print("You're COOKED")


#3. Cálculo de Desconto
#Leia o valor de uma compra.
#- Se o valor for maior que 100, aplicar 10% de desconto.
#- Caso contrário, não aplicar desconto.
#- Mostrar o valor final.
valor = float(input("digite o valor do produto"))
if valor > 100:
    desconto = valor * 0.1
    Preço_final = valor - desconto
    print(f"Valor Original: {valor} \nDesconto: {desconto}\n----------------\nValor final: {Preço_final}")
else:
    preço_final = valor
    print(f"valor Final: {preço_final}")


#4. Conversão de Temperatura
#Leia a temperatura em Celsius e converta para Fahrenheit usando a fórmula: F = (C x 9/5) + 32.
celsius = float(input("digite a temperatura"))
fahrenhet = (celsius * 9/5) + 32
print(f"Temperatura em Celsius {fahrenhet}")



#5. Maior Número (Dois Valores)
#Leia dois números inteiros e informe:
#- Qual deles é o maior.
#- Ou se são iguais.
num1 = float(input("Digite o primeiro número"))
num2 = float(input("Digite o Segundo número"))
if num1 > num2:
    print("Primeiro é maior")
elif num2 > num1:
    print("Segundo é maior")
elif num1 == num2:
    print("Os dois são iguais")



#6. Maior Número (Três Valores)
#Escreva um programa que leia três números inteiros e determine qual deles é o maior.
#Entrada: Três números inteiros.
#Saída: O maior número.
num1 = float(input("Digite o primeiro número"))
num2 = float(input("Digite o Segundo número"))
num2 = float(input("Digite o terceiro número"))


#7. Calculadora Simples
#Crie uma calculadora simples que permita ao usuário realizar operações básicas: soma (+), subtração (-), multiplicação (*) e divisão (/).
#Entrada: Dois números e a operação desejada.
#Saída: O resultado da operação.
n1 = float(input("Digite o Número Digitado"))
n2 = float(input("Digite o Número Digitado"))
operaçao = (input("selecione o tipo de operação:"))
if operaçao == "+":
    resultado = n1+n2
elif operaçao == "-":
    resultado = n1-n2
elif operaçao == "*":
    resultado = n1*n2
elif operaçao == "/":
    if n2!= 0:
        resultado=n1/n2
    else:
        print("divisão por zero")
else:
    print("operação invalida")
print(f"{n1}\n{operaçao}\n{n2}\n-----------\n={resultado}")

#8. Contagem de Números
#Leia uma sequência de números inteiros e conte quantos são positivos, negativos e zeros.
#Entrada: Lista de números inteiros (o usuário decide quantos números serão inseridos).
#Saída: Quantidade de números positivos, negativos e zeros.


#9. Ano Bissexto
#Leia um número inteiro representando um ano e verifique se ele é bissexto ou não.
#Entrada: Um ano (número inteiro).
#Saída: "Bissexto" ou "Não é bissexto".
#Exemplo:
#Entrada: 2024
#Saída: Bissexto
ano = int(input("Digite o ano:"))
if ano % 4 == 0:
    print("Ano Bissexto")
else:
    print("Ano não bissexto")

#10. Intervalo de Idade
#Leia a idade de uma pessoa e informe se ela está na faixa etária permitida (18 a 65 anos).
#- Se a idade estiver entre 18 e 65 (inclusive), mostrar: "Dentro da faixa permitida".
#- Caso contrário, mostrar: "Fora da faixa permitida".
#(Use >= e <= com and).

Idade = int(input("Digite sua idade"))
if Idade >= 18 and Idade <= 65:
    print("Dentro Da Faixa Permitida")
else:
    print("Fora Da Faixa Permitida")

#11. Acesso ao Sistema
#Leia o usuário e a senha digitados.
#- Se usuário == "admin" e senha == "1234", mostrar: "Acesso permitido".
#- Caso contrário, mostrar: "Acesso negado".
#(Use == e and).
User = input("Digite o Usuário")
Senha = input("Digite a senha")
if User == "Admin" and Senha == "1234":
    print(f"Welcome {User}")
else:
    print("Acesso Negado")

#12. Voto Obrigatório
#Leia a idade de uma pessoa.
#- Se a idade for menor que 16, mostrar "Não vota".
#- Se a idade for entre 18 e 70, mostrar "Voto obrigatório".
#- Caso contrário, mostrar "Voto facultativo".
#(Use combinações com and e or).
Idade = int(input("Digite sua Idade:"))
if Idade < 16:
    print("Não Vota")
elif Idade >= 18 and Idade <= 70:
    print("Voto Obrigatório")
else:
    print("Voto facultativo")

#13. Número Fora de Intervalo
#Leia um número inteiro e verifique:
#- Se o número não está no intervalo de 10 a 50, mostrar "Fora do intervalo".
#- Caso contrário, mostrar "Dentro do intervalo".
#(Use not com >= e <=).
num = int(input("Digite seu numero"))
if not (num <= 10) and num <= 50:
    print("sentro do intervalo")
else:
    print("Fora do intervalo")

#14. Aluno Aprovado com Recuperação
#Leia a média final de um aluno.
#- Se a média for >= 7, mostrar "Aprovado".
#- Se a média for >= 5 e < 7, mostrar "Recuperação".
#- Caso contrário, mostrar "Reprovado".
#(Use and, >=, <).
media_final = float(input("Digite a sua Media"))
if media_final >= 7:
    print("Aprovado")
elif media_final >= 5 and media_final < 7:
    print("Recuperacão")
else:
    print("Reprovado")

