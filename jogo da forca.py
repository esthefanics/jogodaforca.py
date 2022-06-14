import random

palavras = ["computador", "cachorro", "mulher", "brasil", "parede", "bala", "pote", "celular", "relógio", "espelho",
            "cadeira", "mesa", "sofá"]

palavra = random.choice(palavras)

print (palavra)


tentativas = 0

chances = 4

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)

print ("\033[1;34mBem vindo ao jogo da forca\033[m")
print ("\033[1;34mSeu objetivo é tentar acertar a palavra secreta\033[m")
print ("\033[1;34mVocê terá que tentar uma letra por vez\033[m")
print ("\033[1;34mCaso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar\033[m")
print ("\033[1;34mCaso você erre, você percerá uma chance, você tem no máximo", chances, "tentativas\033[m")

while tentativas < chances and ''.join(estado_atual) != palavra:

	letra = input("\n\n\033[1;33mQual letra você quer tentar? \033[m")

	while letra in letras_escolhidas:
		print ("\033[1;31mVocê escolheu uma letra que já tinha tentado, escolha outra\033[m")
		letra = input("\n\033[1;31mQual letra você quer tentar? \033[m")

	letras_escolhidas.append(letra)

	if letra in palavra:
		print ("\033[1;32mParabéns, você acertou a letra!\033[m")
		for i in range(len(palavra)):
			if letra == palavra[i]:
				estado_atual[i] = letra
	else:
		print ("\033[1;31mQue pena, você errou!\033[m")
		tentativas = tentativas + 1

	# quantas tentativas ele tem
	print ("\033[1;31mVocê já fez", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas\033[m" )

	# qual o estado atual da palavra
	print ("Esse é o estado atual:")
	print (estado_atual)

	# quais as letras ele já tentou
	print ("As letras que você já tentou são:")
	for item in letras_escolhidas:
		print (item, end=" ")

# fazer um final pro jogo
if tentativas == chances:
	print ("\n\nVocê perdeu")
	print ("Acabaram suas tentativas")
else:
	print ("\n\n\033[1;32mVocê ganhou, parabéns\033[m")

print ("\033[1;32mA palavra era\033[m", palavra)