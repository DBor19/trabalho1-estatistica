import pandas as pd

df = pd.read_csv('Dados.csv')


dataModulo1 = df[df["Modulo"] == 1]
dataModulo2 = df[df["Modulo"] == 2]
dataModulo3 = df[df["Modulo"] == 3]
dataModulo4 = df[df["Modulo"] == 4]
dataModulo5 = df[df["Modulo"] == 5]
dataSample = df.sample(round(len(df)*0.1))

print(dataModulo1)

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
media_amostra_IMC = amostra_unificada['Imc'].mean()

moda_amostra_altura = amostra_unificada['Altura'].mode()
moda_amostra_peso = amostra_unificada['Peso'].mode()
moda_amostra_idade = amostra_unificada['Idade'].mode()
moda_amostra_IMC = amostra_unificada['Imc'].mode()

mediana_amostra_altura = amostra_unificada['Altura'].median()
mediana_amostra_peso = amostra_unificada['Peso'].median()
mediana_amostra_idade = amostra_unificada['Idade'].median()
mediana_amostra_IMC = amostra_unificada['Imc'].median()

variacao_amostra_altura = amostra_unificada['Altura'].var()
variacao_amostra_peso = amostra_unificada['Peso'].var()
variacao_amostra_idade = amostra_unificada['Idade'].var()
variacao_amostra_IMC = amostra_unificada['Imc'].var()

desvio_padrao_amostra_altura = amostra_unificada['Altura'].std()
desvio_padrao_amostra_peso = amostra_unificada['Peso'].std()
desvio_padrao_amostra_idade = amostra_unificada['Idade'].std()
desvio_padrao_amostra_IMC = amostra_unificada['Imc'].std()

coeficiente_variacao_amostra_altura = (
    desvio_padrao_amostra_altura / media_amostra_altura) * 100
coeficiente_variacao_amostra_peso = (
    desvio_padrao_amostra_peso / media_amostra_peso) * 100
coeficiente_variacao_amostra_idade = (
    desvio_padrao_amostra_idade / media_amostra_idade) * 100
coeficiente_variacao_amostra_IMC = (
    desvio_padrao_amostra_IMC / media_amostra_IMC) * 100

print('------AMOSTRA------')
print('Média da altura: ', media_amostra_altura)
print('Média do peso: ', media_amostra_peso)
print('Média da idade: ', media_amostra_idade)
print('Média do IMC: ', media_amostra_IMC)

print('Moda da altura: ', moda_amostra_altura)
print('Moda do peso: ', moda_amostra_peso)
print('Moda da idade: ', moda_amostra_idade)
print('Moda do IMC: ', moda_amostra_IMC)

print('Mediana da altura: ', mediana_amostra_altura)
print('Mediana do peso: ', mediana_amostra_peso)
print('Mediana da idade: ', mediana_amostra_idade)
print('Mediana do IMC: ', mediana_amostra_IMC)

print('Variância da altura: ', variacao_amostra_altura)
print('Variância do peso: ', variacao_amostra_peso)
print('Variância da idade: ', variacao_amostra_idade)
print('Variância do IMC: ', variacao_amostra_IMC)

print('Desvio padrão da altura: ', desvio_padrao_amostra_altura)
print('Desvio padrão do peso: ', desvio_padrao_amostra_peso)
print('Desvio padrão da idade: ', desvio_padrao_amostra_idade)
print('Desvio padrão do IMC: ', desvio_padrao_amostra_IMC)

print('Coeficiente de variação da altura: ',
      coeficiente_variacao_amostra_altura)
print('Coeficiente de variação do peso: ', coeficiente_variacao_amostra_peso)
print('Coeficiente de variação da idade: ', coeficiente_variacao_amostra_idade)
print('Coeficiente de variação do IMC: ', coeficiente_variacao_amostra_IMC)