# O programa recebe o tamanho em metros quadrados(valor inteiro) da área a ser pintada
# e informa ao usuário as quantidades de tinta a serem compradas e os respectivos preços 
# O melhor preço com 10% de folga 
# Disponível em github.com/rainervitorrv

tamanhoAreaSerPintada = int(input('Informe o tamanho da área a ser pintada: '))

qtdLitrosTintaNecessario = tamanhoAreaSerPintada / 6
qtdLatasTintaNecessario = qtdLitrosTintaNecessario / 18
qtdLatasTintaNecessario = 1 if qtdLitrosTintaNecessario <= 18 else qtdLatasTintaNecessario
qtdGaloesTintaNecessario = qtdLitrosTintaNecessario / 3.6
qtdGaloesTintaNecessario = 1 if qtdLitrosTintaNecessario <= 3.6 else qtdGaloesTintaNecessario

precoTotalEmLatas = qtdLatasTintaNecessario * 80
precoTotalEmGaloes = qtdGaloesTintaNecessario * 25

qtdLitrosNecessario = qtdLitrosTintaNecessario + (qtdLitrosTintaNecessario * 0.1)


qtdLataMisto = 0
qtdGalaoMisto = 0

while qtdLitrosNecessario > 0 :
    if qtdLitrosNecessario >= 18:
        qtdLataMisto += 1
        qtdLitrosNecessario -= 18
    elif qtdLitrosNecessario > 3.6:
        if (qtdLitrosNecessario * )
        qtdGalaoMisto += 1
        qtdLitrosNecessario -= 3.6


precoTotalMisturado = qtdGalaoMisto * 25 + qtdLataMisto * 80

print('-------------------------------------------------')
print('TAMANHO DA ARÉA A SER PINTADA: {:.0f}m²'.format(tamanhoAreaSerPintada))
print('QUANTIDADE DE LITROS DE TINTA GASTO: {:.0f} l'.format(qtdLitrosTintaNecessario))
print('SE VOCÊ COMPRAR APENAS LATAS DE 18 l PRECISARÁ DE {:.0f} LATA(S)'.format(qtdLatasTintaNecessario))
print('E DEVERÁ GASTAR O VALOR TOTAL DE R$ {:.2f}'.format(precoTotalEmLatas))
print('SE VOCÊ COMPRAR APENAS GALÕES DE 3,6 l PRECISARÁ DE {:.0f} GALÕES'.format(qtdGaloesTintaNecessario))
print('E DEVERÁ GASTAR O VALOR TOTAL DE R$ {:.2f}'.format(precoTotalEmGaloes))
print('SE VOCÊ COMPRAR MISTURADO PRECISARÁ DE {:.0f} GALÕES E {:.0f} LATA(S)'.format(qtdGalaoMisto, qtdLataMisto))
print('E DEVERÁ GASTAR O VALOR TOTAL DE R$ {:.2f}'.format(precoTotalMisturado))
print('-------------------------------------------------')
