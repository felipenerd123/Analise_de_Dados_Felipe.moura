lista = [3, -1, 0, 7, -5]
# 1.crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja"
frutas = ["maçã", "banana", "Laranja", "uva"]

# 2. imprima o primeiro e o útimo elemento da lista
frutas[0]
frutas[-1]

# 3. adicione a fruta "manga" ao final da lista
frutas.append("manga")
frutas = frutas + ["manga"]

# 4. Remova a fruta "banana" da lista.
frutas.remove("banana")

# 5. substitua "laranja" por "abacaxi".
indice = frutas.index("laranja")
frutas[indice] = "abacaxi"

# 6. 