import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Dados.csv')

dataModulo1 = df[df["Modulo"] == 1]
dataModulo2 = df[df["Modulo"] == 2]
dataModulo3 = df[df["Modulo"] == 3]
dataModulo4 = df[df["Modulo"] == 4]
dataModulo5 = df[df["Modulo"] == 5]

# Proporção das Estratificações:
fator_modulo1 = len(dataModulo1)/len(df)
proporcao_modulo1 = fator_modulo1 * len(df)*0.1

fator_modulo2 = len(dataModulo2)/len(df)
proporcao_modulo2 = fator_modulo2 * len(df)*0.1

fator_modulo3 = len(dataModulo3)/len(df)
proporcao_modulo3 = fator_modulo3 * len(df)*0.1

fator_modulo4 = len(dataModulo4)/len(df)
proporcao_modulo4 = fator_modulo4 * len(df)*0.1

fator_modulo5 = len(dataModulo5)/len(df)
proporcao_modulo5 = fator_modulo5 * len(df)*0.1

amostraM1 = dataModulo1.sample(round(proporcao_modulo1))
print(amostraM1)
print()
amostraM2 = dataModulo2.sample(round(proporcao_modulo2))
print("Módulo2", amostraM2)
print()
amostraM3 = dataModulo3.sample(round(proporcao_modulo3))
print("Módulo3", amostraM3)
print()
amostraM4 = dataModulo4.sample(round(proporcao_modulo4))
print("Módulo4", amostraM4)
print()
amostraM5 = dataModulo5.sample(round(proporcao_modulo5))
print("Módulo5", amostraM5)


# Dataframe das Amostras
amostras = [amostraM1, amostraM2, amostraM3, amostraM4, amostraM5]
amostra_unificada = pd.concat(amostras)

print(amostra_unificada)


# Medidas da Amostra
media_amostra_altura = amostra_unificada['Altura'].mean()
media_amostra_peso = amostra_unificada['Peso'].mean()
media_amostra_idade = amostra_unificada['Idade'].mean()
media_amostra_imc = amostra_unificada['Imc'].mean()

moda_amostra_altura = amostra_unificada['Altura'].mode()
moda_amostra_peso = amostra_unificada['Peso'].mode()
moda_amostra_idade = amostra_unificada['Idade'].mode()
moda_amostra_imc = amostra_unificada['Imc'].mode()

mediana_amostra_altura = amostra_unificada['Altura'].median()
mediana_amostra_peso = amostra_unificada['Peso'].median()
mediana_amostra_idade = amostra_unificada['Idade'].median()
mediana_amostra_imc = amostra_unificada['Imc'].median()

variacao_amostra_altura = amostra_unificada['Altura'].var()
variacao_amostra_peso = amostra_unificada['Peso'].var()
variacao_amostra_idade = amostra_unificada['Idade'].var()
variacao_amostra_imc = amostra_unificada['Imc'].var()

desvio_padrao_amostra_altura = amostra_unificada['Altura'].std()
desvio_padrao_amostra_peso = amostra_unificada['Peso'].std()
desvio_padrao_amostra_idade = amostra_unificada['Idade'].std()
desvio_padrao_amostra_imc = amostra_unificada['Imc'].std()

coeficiente_variacao_amostra_altura = (
    desvio_padrao_amostra_altura / media_amostra_altura) * 100
coeficiente_variacao_amostra_peso = (
    desvio_padrao_amostra_peso / media_amostra_peso) * 100
coeficiente_variacao_amostra_idade = (
    desvio_padrao_amostra_idade / media_amostra_idade) * 100
coeficiente_variacao_amostra_imc = (
                                           desvio_padrao_amostra_imc / media_amostra_imc) * 100

print(f'Média da altura: {media_amostra_altura:.2f}')
print(f'Média do peso: {media_amostra_peso:.2f}')
print(f'Média da idade: {media_amostra_idade:.2f}')
print(f'Média do IMC: {media_amostra_imc:.2f}')

print(f'Mediana da altura:  {mediana_amostra_altura}')
print(f'Mediana do peso: {mediana_amostra_peso}')
print(f'Mediana da idade:  {mediana_amostra_idade}')
print(f'Mediana do IMC:  {mediana_amostra_imc}')

# print(f'Moda da altura: {moda_altura::.2f}')
# print(f'Moda do peso: {moda_peso:.2f}')
# print(f'Moda da idade: ', moda_idade)
# print(f'Moda do IMC: ', moda_imc)

# Moda vem como um Series no pandas(pois pode ter mais de uma moda). Tem que passar para list
print(f'Moda da altura: {moda_amostra_altura.tolist()}')
print(f'Moda da peso: {moda_amostra_peso.tolist()}')
print(f'Moda da idade: {moda_amostra_idade.tolist()}')
print(f'Moda da IMC: {moda_amostra_imc.tolist()}')

print(f'Variância da altura: {variacao_amostra_altura:.4f}')
print(f'Variância do peso: {variacao_amostra_peso:.4f}')
print(f'Variância da idade: {variacao_amostra_idade:.4f}')
print(f'Variância do IMC: {variacao_amostra_imc:.4f}')


print(f'Desvio padrão da altura: {desvio_padrao_amostra_altura:.4f}')
print(f'Desvio padrão do peso: {desvio_padrao_amostra_peso:.4f}')
print(f'Desvio padrão da idade: {desvio_padrao_amostra_idade:.4f}')
print(f'Desvio padrão do IMC: {desvio_padrao_amostra_imc:.4f}')

print(f'Coeficiente de variação da altura: {coeficiente_variacao_amostra_altura:.4f}' )
print(f'Coeficiente de variação do peso: {coeficiente_variacao_amostra_peso:.4f}' )
print(f'Coeficiente de variação da idade: {coeficiente_variacao_amostra_idade:.4f}' )
print(f'Coeficiente de variação do IMC: {coeficiente_variacao_amostra_imc:.4f}')

plt.figure(1)
boxplot1 = amostra_unificada.boxplot(column=['Altura'])
plt.title("Box plot Amostra")

plt.figure(2)
boxplot2 = amostra_unificada.boxplot(column=['Peso'])
plt.title("Box plot Amostra")

plt.figure(3)
boxplot3 = amostra_unificada.boxplot(column=['Idade'])
plt.title("Box plot Amostra")

plt.figure(4)
boxplot4 = amostra_unificada.boxplot(column=['Imc'])
plt.title("Box plot Amostra")

plt.show()