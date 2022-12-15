import statistics as sts

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as srn

# importar dados
dataset = pd.read_csv("tempo.csv", sep=";")

# visualizando dados no terminal
print('*** ARQUIVO COMPLETO ***\n')
# print(dataset)


# verificando se existem dados NAs
dados_Nas = dataset.isnull().sum()
print('\n\n*** Dados Nas ***\n')
# print(dados_Nas)


# Visualizando Coluna Aparencia
agrupado = dataset.groupby(['Aparencia']).size()
print('\n\n*** RESUMO Aparencia ***\n')
# print(agrupado)

# exibe o gráfico acima em uma nova janela
# agrupado.plot.bar(color = 'gray')
# plt.show()

# Tratando Aparencia
dataset.loc[dataset['Aparencia'] == 'menos', 'Aparencia'] = 'sol'

# Visualizando Novamente Coluna Aparencia
agrupado = dataset.groupby(['Aparencia']).size()
print('\n\n*** RESUMO Repetido Aparencia ***\n')
# print(agrupado)


# Visualizando Coluna Temperatura (regra de negócio -> Entre -130 e 130F)
print('\n\n*** RESUMO Temperatura ***\n')
# print(dataset['Temperatura'].describe())

# visualizando dados acim através de um boxplot
# srn.boxplot(x=dataset['Temperatura']).set_title('Temperatura')
# plt.show()

# visualizando dados acima através de um distplot
# srn.distplot(dataset['Temperatura']).set_title('Temperatura')
# plt.show()

# verificando se existem temperatura com valores anormais
print('\n\n *** Verificando valores outliers ***')
# print(dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)])

# calculando a mediana
mediana = sts.median(dataset['Temperatura'])
print('\n\n *** Exibindo a Mediana de Temperatura ***')
# print(mediana)

# substituir valor anormal pela mediana
dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)] = mediana

# veriricando novamente
print('\n\n *** Verificando novamente valores outliers ***')
# print(dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)])


# Umidade

# visualizando descricao
print('\n\n*** RESUMO Umidade ***\n')
# print(dataset['Umidade'].describe())

# calculando a mediana
mediana = sts.median(dataset['Umidade'])

# substituindo valores NAs pela mediana
dataset['Umidade'].fillna(mediana, inplace=True)

# verificando se ainda existem NAs em 
print('\n\n*** Valores NAs Umidade ***\n')
# print(dataset['Umidade'].isnull().sum())

# verificando se existem valores anormais
print('\n\n*** Valores anormais Umidade ***\n')
# print(dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)])

# substituindo valores anormais pela mediana
dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)] = mediana

# verificando novamente se existem valores anormais
# print(dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)])

# Vento

# agrupando
agrupado = dataset.groupby(['Vento']).size()
print('\n\n*** RESUMO Vento ***\n')
print(agrupado)

# tratando dados de vento

# substituindo valores anormais poer FALSO e VERDADEIRO
dataset.loc[dataset['Vento'] == 73.5, 'Vento'] = "VERDADEIRO"
dataset.loc[dataset['Vento'] == 82.5, 'Vento'] = "FALSO"

# agrupando novamente
agrupado = dataset.groupby(['Vento']).size()
print('\n\n*** RESUMO repetido Vento ***\n')
# print(agrupado)

# Jogar

# agrupando
agrupado = dataset.groupby(['Jogar']).size()
print('\n\n*** RESUMO Jogar ***\n')
print(agrupado)