#

notas= {"Alice": 8.5,
        "Bruno": 7.0,
        "Carla": 9.0,
        "Daniel": 5.7,
}
notas.keys()
notas.values()
# 2. Calcule a média das notas e exiba o resultado
media = (notas["Alice"] + notas["Bruno"] + 
         notas["Carla"] + notas["Daniel"]) / 4


# Exercicio 6:
produtos = {"caneta": 10,
            "mochila": 70,
            "caderno": 45,
            "notebook": 3000
            }

#Looser
for produto, preco in produtos.items():
    if preco >= 50:
        print(produtos,"=" ,preco )

#Campeao 
filtro = {}
for produto, preco in produtos.items():
    if preco >= 50:
        filtro[produto] = preco
print(filtro)

# Exercicio 7:
tradutor = {
    "door": "porta",
    "cat": "gato",
    "drink": "bebida"
}
palavra = input("digite a palavra em inglês")
if palavra in tradutor:
    print(f"traducao: {tradutor[palavra]}")
else:
    print("palavra nao encontrada")

# Exercicio 8:
compras = {}


# Exercicio 10 
funcionario = {}

while True:
    escolha = input("escolha o que voce deseja:")
    if escolha == '1':
        nome = input("digite o produto")
        cargo = input("digite a quantidade")
        salario = float(input("digite a quantidade"))
        funcionario["nome"] = nome
        funcionario["cargo"] = cargo
        funcionario["salario"] = salario
    elif escolha=='2':
        nome = input("digite o nome a ser consultado")
        if nome in funcionario["nome"]:
            print(funcionario[nome])
    else:
        print("programa encerrado")
        break