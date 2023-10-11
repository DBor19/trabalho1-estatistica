import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('Dados.csv')
# print(df.head(n=10))
# print(df.info())

print(df["Modulo"].value_counts())

# Divide os dados em treinamento e teste estratificados
x_train, x_test, y_train, y_test = train_test_split(df.drop('Modulo', 
                                                            axis=1), 
                                                            df['Modulo'], 
                                                            test_size=0.90, 
                                                            random_state=1, 
                                                            stratify=df['Modulo'])

# Cria um novo DataFrame com base nos dados de treinamento
amostra_estratificada = pd.concat([x_train, y_train], axis=1)

# Exibe as contagens de módulo na amostra estratificada
print(amostra_estratificada['Modulo'].value_counts())


desc_populacao = df[['Idade', 'Peso', 'Altura']].describe()

