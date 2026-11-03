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
    ingresso = 15
    print("Bem vindo idoso!")
    print("Seu ingresso promocional vale R$ 15,00!")
    print(f"Seu troco:  {dinheiro - ingresso}")
 elif idade >= 12 and idade <= 64 and estudante:
    ingresso = 20
    print("Bem vindo jovem gafanhoto!")
    print("Você paga somente a meia-entrada de R$ 20,00! Aproveite bastante.")
    print(f"Seu troco {dinheiro - ingresso}")
 elif idade >= 12 and idade <= 64:
    ingresso = 40
    print("Bem vindo!")
    print("O ingresso custa R$ 40,00. Aproveite bastante.")
    print(f"Seu troco {dinheiro - ingresso}")
 else:
     print("Nenhuma opção encontrada ou sistema fora do ar!")

  
