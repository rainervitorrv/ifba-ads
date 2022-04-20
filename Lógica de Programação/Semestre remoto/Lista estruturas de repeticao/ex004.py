HABITANTES_POPULACAO_A = 80000
TAXA_ANUAL_CRESCIMENTO_DA_POPULACAO_A = 0.03
HABITANTES_POPULACAO_B = 200000
TAXA_ANUAL_CRESCIMENTO_DA_POPULACAO_B = 0.015

totalAnos = 0

while HABITANTES_POPULACAO_A < HABITANTES_POPULACAO_B:
    totalAnos = totalAnos + 1
    HABITANTES_POPULACAO_A += int(HABITANTES_POPULACAO_A *
                                  TAXA_ANUAL_CRESCIMENTO_DA_POPULACAO_A)

    HABITANTES_POPULACAO_B += int(HABITANTES_POPULACAO_A *
                                  TAXA_ANUAL_CRESCIMENTO_DA_POPULACAO_B)

if (HABITANTES_POPULACAO_A == HABITANTES_POPULACAO_B):
    print('Em ', totalAnos, ' anos a população A será igual a população B')
else:
    print('Em ', totalAnos, ' anos a população A será maior que a população B')
