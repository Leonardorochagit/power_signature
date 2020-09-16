# Pandas é usado para manipulação de dados
import pandas as pd
# Use numpy para converter em matrizes
import numpy as np
# Usando Skicit-learn para dividir dados em conjuntos de treinamento e teste de sklearn.model_selection import
from sklearn.model_selection import train_test_split
# Importe o modelo que estamos usando
from sklearn.ensemble import RandomForestRegressor
# Ferramentas de importação necessárias para visualização
from sklearn.tree import export_graphviz
import pydot

# Leia os dados e exiba as primeiras 5 linhas
features = pd.read_csv('db_elet.csv')
features.head(5)
print('The shape of our features is:', features.shape)

# Estatísticas descritivas para cada coluna
features.describe()

# Codifique os dados one-hot usando pandas get_dummies
features = pd.get_dummies(features)
# Exibe as primeiras 5 linhas das últimas 12 colunas
features.iloc[:,5:].head(5)

# Labels são os valores que queremos prever
labels = np.array(features['Label'])

# Remova os rótulos dos recursos
# eixo 1 refere-se às colunas
features= features.drop('Label', axis = 1)

# Salvar nomes de recursos para usar posteriormente
feature_list = list(features.columns)

# Converter em numpy array
features = np.array(features)

# Divida os dados em conjuntos de treinamento e teste
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.2, random_state = 60)

# print('Training Features Shape:', train_features.shape)
# print('Training Labels Shape:', train_labels.shape)
# print('Testing Features Shape:', test_features.shape)
# print('Testing Labels Shape:', test_labels.shape)

# Instancie o modelo com 1000 árvores de decisão
rf = RandomForestRegressor(n_estimators = 2000, random_state = 42)
# Treine o modelo nos dados de treinamento
rf.fit(train_features, train_labels)

# Use o método de previsão da floresta nas
predictions = rf.predict(test_features)
# Calcular os erros absolutos erros
errors = abs(predictions - test_labels)
# Imprime o erro médio absoluto (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# Calcular erro percentual absoluto médio (MAPE)
mape = 100 * (errors / test_labels)
print(mape)
# Calcular e exibir a precisão
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
