nome=input("Olá, qual seu nome?")
valor=float(input("Qual o valor que você tem guardado para a viagem?"))
dias=float(input("Quantos dias vai durar a viagem?"))
total=valor/dias
print("Olá" , nome,",você tem R$", total, "para gastar por dia na viagem.".format(nome))

