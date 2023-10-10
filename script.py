import pandas as pd

df = pd.read_csv('Dados.csv')

media_altura = df['Altura'].mean()
media_peso = df['Peso'].mean()
media_idade = df['Idade'].mean()
media_imc = df['IMC'].mean()

mediana_altura = df['Altura'].median()
mediana_peso = df['Peso'].median()
mediana_idade = df['Idade'].median()
mediana_imc = df['IMC'].median()

moda_altura = df['Altura'].mode()
moda_peso = df['Peso'].mode()
moda_idade = df['Idade'].mode()
moda_imc = df['IMC'].mode()

variacao_altura = df['Altura'].var()
variacao_peso = df['Peso'].var()
variacao_idade = df['Idade'].var()
variacao_imc = df['IMC'].var()

desvio_padrao_altura = df['Altura'].std()
desvio_padrao_peso = df['Peso'].std()
desvio_padrao_idade = df['Idade'].std()
desvio_padrao_imc = df['IMC'].std()

coeficiente_variacao_altura = desvio_padrao_altura / media_altura
coeficiente_variacao_peso = desvio_padrao_peso / media_peso
coeficiente_variacao_idade = desvio_padrao_idade / media_idade
coeficiente_variacao_imc = desvio_padrao_imc / media_imc

print('Média da altura: ', media_altura)
print('Média do peso: ', media_peso)
print('Média da idade: ', media_idade)
print('Média do IMC: ', media_imc)

print('Mediana da altura: ', mediana_altura)
print('Mediana do peso: ', mediana_peso)
print('Mediana da idade: ', mediana_idade)
print('Mediana do IMC: ', mediana_imc)

print('Moda da altura: ', moda_altura)
print('Moda do peso: ', moda_peso)
print('Moda da idade: ', moda_idade)
print('Moda do IMC: ', moda_imc)

print('Variância da altura: ', variacao_altura)
print('Variância do peso: ', variacao_peso)
print('Variância da idade: ', variacao_idade)
print('Variância do IMC: ', variacao_imc)

print('Desvio padrão da altura: ', desvio_padrao_altura)
print('Desvio padrão do peso: ', desvio_padrao_peso)
print('Desvio padrão da idade: ', desvio_padrao_idade)
print('Desvio padrão do IMC: ', desvio_padrao_imc)

print('Coeficiente de variação da altura: ', coeficiente_variacao_altura)
print('Coeficiente de variação do peso: ', coeficiente_variacao_peso)
print('Coeficiente de variação da idade: ', coeficiente_variacao_idade)
print('Coeficiente de variação do IMC: ', coeficiente_variacao_imc)
