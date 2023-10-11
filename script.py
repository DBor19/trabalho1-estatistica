import pandas as pd

df = pd.read_csv('Dados.csv')

media_altura = df['Altura'].mean()
media_peso = df['Peso'].mean()
media_idade = df['Idade'].mean()
media_IMC = df['Imc'].mean()

mediana_altura = df['Altura'].median()
mediana_peso = df['Peso'].median()
mediana_idade = df['Idade'].median()
mediana_IMC = df['Imc'].median()

moda_altura = df['Altura'].mode()
moda_peso = df['Peso'].mode()
moda_idade = df['Idade'].mode()
moda_IMC = df['Imc'].mode()

variacao_altura = df['Altura'].var()
variacao_peso = df['Peso'].var()
variacao_idade = df['Idade'].var()
variacao_IMC = df['Imc'].var()

desvio_padrao_altura = df['Altura'].std()
desvio_padrao_peso = df['Peso'].std()
desvio_padrao_idade = df['Idade'].std()
desvio_padrao_IMC = df['Imc'].std()

coeficiente_variacao_altura = desvio_padrao_altura / media_altura * 100
coeficiente_variacao_peso = desvio_padrao_peso / media_peso * 100
coeficiente_variacao_idade = desvio_padrao_idade / media_idade * 100
coeficiente_variacao_IMC = desvio_padrao_IMC / media_IMC * 100

print('Média da altura: ', media_altura)
print('Média do peso: ', media_peso)
print('Média da idade: ', media_idade)
print('Média do IMC: ', media_IMC)

print('Mediana da altura: ', mediana_altura)
print('Mediana do peso: ', mediana_peso)
print('Mediana da idade: ', mediana_idade)
print('Mediana do IMC: ', mediana_IMC)

print('Moda da altura: ', moda_altura)
print('Moda do peso: ', moda_peso)
print('Moda da idade: ', moda_idade)
print('Moda do IMC: ', moda_IMC)

print('Variância da altura: ', variacao_altura)
print('Variância do peso: ', variacao_peso)
print('Variância da idade: ', variacao_idade)
print('Variância do IMC: ', variacao_IMC)

print('Desvio padrão da altura: ', desvio_padrao_altura)
print('Desvio padrão do peso: ', desvio_padrao_peso)
print('Desvio padrão da idade: ', desvio_padrao_idade)
print('Desvio padrão do IMC: ', desvio_padrao_IMC)

print('Coeficiente de variação da altura: ', coeficiente_variacao_altura)
print('Coeficiente de variação do peso: ', coeficiente_variacao_peso)
print('Coeficiente de variação da idade: ', coeficiente_variacao_idade)
print('Coeficiente de variação do IMC: ', coeficiente_variacao_IMC)


# Técnica de Amostragem Utilizada (Amostragem Aleatória Simples) (10% da População):
amostra = df.sample(frac=0.10)

print(amostra)

media_amostra_altura = amostra['Altura'].mean()
media_amostra_peso = amostra['Peso'].mean()
media_amostra_idade = amostra['Idade'].mean()
media_amostra_IMC = amostra['Imc'].mean()


moda_amostra_altura = amostra['Altura'].mode()
moda_amostra_peso = amostra['Peso'].mode()
moda_amostra_idade = amostra['Idade'].mode()
moda_amostra_IMC = amostra['Imc'].mode()

mediana_amostra_altura = amostra['Altura'].median()
mediana_amostra_peso = amostra['Peso'].median()
mediana_amostra_idade = amostra['Idade'].median()
mediana_amostra_IMC = amostra['Imc'].median()

variacao_amostra_altura = amostra['Altura'].var()
variacao_amostra_peso = amostra['Peso'].var()
variacao_amostra_idade = amostra['Idade'].var()
variacao_amostra_IMC = amostra['Imc'].var()

desvio_padrao_amostra_altura = amostra['Altura'].std()
desvio_padrao_amostra_peso = amostra['Peso'].std()
desvio_padrao_amostra_idade = amostra['Idade'].std()
desvio_padrao_amostra_IMC = amostra['Imc'].std()

coeficiente_variacao_amostra_altura = (
    desvio_padrao_amostra_altura / media_amostra_altura) * 100
coeficiente_variacao_amostra_peso = (
    desvio_padrao_amostra_peso / media_amostra_peso) * 100
coeficiente_variacao_amostra_idade = (
    desvio_padrao_amostra_idade / media_amostra_idade) * 100
coeficiente_variacao_amostra_IMC = (
    desvio_padrao_amostra_IMC / media_amostra_IMC) * 100

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


# Comparação dos Índices
print()
print()
print()
print()
print()
print()
print(
    f'ALTURA: Média População: {media_altura:.2f}, Média Amostra {media_amostra_altura:.2f}')
print(
    f'ALTURA: Moda População: {moda_altura}, Moda Amostra {moda_amostra_altura}')
print(
    f'ALTURA: Mediana População: {mediana_altura:.2f}, Mediana Amostra {mediana_amostra_altura:.2f}')
print(
    f'ALTURA: Variância População: {variacao_altura:.2f}, Variância Amostra {variacao_amostra_altura:.2f}')
print(
    f'ALTURA: Desvio Padrão População: {desvio_padrao_altura:.2f}, Desvio Padrão Amostra {desvio_padrao_amostra_altura:.2f}')
print(
    f'ALTURA: Coeficiente de Variação População: {coeficiente_variacao_altura:.2f}, Coeficiente de Variação Amostra {coeficiente_variacao_amostra_altura:.2f}')

print(
    f'PESO: Média População: {media_peso:.2f}, Média Amostra {media_amostra_peso:.2f}')
print(
    f'PESO: Moda População: {moda_peso}, Moda Amostra {moda_amostra_peso}')
print(
    f'PESO: Mediana População: {mediana_peso:.2f}, Mediana Amostra {mediana_amostra_peso:.2f}')
print(
    f'PESO: Variância População: {variacao_peso:.2f}, Variância Amostra {variacao_amostra_peso:.2f}')
print(
    f'PESO: Desvio Padrão População: {desvio_padrao_peso:.2f}, Desvio Padrão Amostra {desvio_padrao_amostra_peso:.2f}')
print(
    f'PESO: Coeficiente de Variação População: {coeficiente_variacao_peso:.2f}, Coeficiente de Variação Amostra {coeficiente_variacao_amostra_peso:.2f}')


print(
    f'IDADE: Média População: {media_idade:.2f}, Média Amostra {media_amostra_idade:.2f}')
print(
    f'IDADE: Moda População: {moda_idade}, Moda Amostra {moda_amostra_idade}')
print(
    f'IDADE: Mediana População: {mediana_idade:.2f}, Mediana Amostra {mediana_amostra_idade:.2f}')
print(
    f'IDADE: Variância População: {variacao_idade:.2f}, Variância Amostra {variacao_amostra_idade:.2f}')
print(
    f'IDADE: Desvio Padrão População: {desvio_padrao_idade:.2f}, Desvio Padrão Amostra {desvio_padrao_amostra_idade:.2f}')
print(
    f'IDADE: Coeficiente de Variação População: {coeficiente_variacao_idade:.2f}, Coeficiente de Variação Amostra {coeficiente_variacao_amostra_idade:.2f}')


print(
    f'IMC: Média População: {media_IMC:.2f}, Média Amostra {media_amostra_IMC:.2f}')
print(
    f'IMC: Moda População: {moda_IMC}, Moda Amostra {moda_amostra_IMC}')
print(
    f'IMC: Mediana População: {mediana_IMC:.2f}, Mediana Amostra {mediana_amostra_IMC:.2f}')
print(
    f'IMC: Variância População: {variacao_IMC:.2f}, Variância Amostra {variacao_amostra_IMC:.2f}')
print(
    f'IMC: Desvio Padrão População: {desvio_padrao_IMC:.2f}, Desvio Padrão Amostra {desvio_padrao_amostra_IMC:.2f}')
print(
    f'IMC: Coeficiente de Variação População: {coeficiente_variacao_IMC:.2f}, Coeficiente de Variação Amostra {coeficiente_variacao_amostra_IMC:.2f}')
