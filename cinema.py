print("——————————————————————")
print("Bem vindo ao cinema Freddy Fazbear Enterprise")
print("——————————————————————")
print("Vamos começar perguntando sua idade!")
loop = " "
while loop: # sistema de repetição, a partir de idade, entra em loop
 idade = int(input("Digite sua idade: "))
 print("Agora, iremos registrar no sistema seu saldo,digite abaixo seu o saldo disponível")
 dinheiro = int(input("Digite seu saldo: "))
 estudante = input("Você é estudante? (s/n): ") == "s"
 ingresso = 10
 if idade <= 12:
    ingresso = 10
    print("Bem vinda criança!")
    print("Seu ingresso com preço fixo vale R$ 10,00!")
    print(f"Seu troco:  {dinheiro - ingresso}")
 elif (dinheiro < ingresso):
  print("Seu saldo é insuficiente!")
 elif idade >= 65:
    total = 0
    ingresso = 15
    quantidade = int(input("Quantos ingressos você quer? "))
    print("Bem vindo idoso!")
    print("Seu ingresso promocional vale R$ 15,00!")
    for compra in range (quantidade):
     total = ingresso * quantidade
    print(f"Seu troco: {dinheiro - total}")
 elif idade >= 12 and idade <= 64 and estudante:
    total = 0
    ingresso = 20
    quantidade = int(input("Quantos ingressos você quer? "))
    print("Bem vindo jovem gafanhoto!")
    print("Você paga somente a meia-entrada de R$ 20,00! Aproveite bastante.")
    for compra in range (quantidade):
     total = ingresso * quantidade
    print(f"Seu troco: {dinheiro - total}")
 elif idade >= 12 and idade <= 64:
    total = 0
    ingresso = 40
    quantidade = int(input("Quantos ingressos você quer? "))
    print("Bem vindo!")
    print("O ingresso custa R$ 40,00. Aproveite bastante.")
    for compra in range (quantidade):
     total = ingresso * quantidade
    print(f"Seu troco: {dinheiro - total}")
 else:
     print("Nenhuma opção encontrada ou sistema fora do ar!")
  
