precoProduto1 = float(input('Informe o preço do 1º produto: '))
precoProduto2 = float(input('Informe o preço do 2º produto: '))
precoProduto3 = float(input('Informe o preço do 3º produto: '))

if (precoProduto1 < precoProduto2 and precoProduto1 < precoProduto3):
    print('O produto com menor preço é o primeiro e custa R$ {:.2f}'.format(
        precoProduto1))
elif (precoProduto2 < precoProduto3):
    print('O produto com menor preço é o segundo e custa R$ {:.2f}'.format(
        precoProduto2))
else:
    print('O produto com menor preço é o terceiro e custa R$ {:.2f}'.format(
        precoProduto3))
