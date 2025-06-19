#faça um algoritmo que leia cada pessoa, quantos paes de queijo cada pessoa pediu
#e quanto cada pessoa deve pagar

pao = int(input('digite a quantidade de pao de queijo :'))
pessoas = int(input('digite a quantidade de pessoas :'))
valortotal = float(input('digite o valor total :'))
valorpc = valortotal/pao
valorpago = valortotal/pessoas

print('a quantidade que cada um deve pagar e de {}'.format(valorpago))

comeumenos = int(input('caso alguem tenha comido menos pao de queijo, quantos paes ele comeu ?'))
pessoacomeumenos = comeumenos*valorpc
print('entao ele/ela deve pagar o valor de{}'.format(pessoacomeumenos))


input('pressione enter para sair')