from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb
import joblib


# Fetch dataset
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

# Criando coluna doenca ~ 0 = não e 1 = sim
dados['doenca'] = (heart_disease.data.targets > 0) * 1

X = dados.drop(columns='doenca')
y = dados['doenca']

# separando os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432, stratify=y)

# Criando o modelo
modelo = xgb.XGBClassifier(objective='binary:logistic')

# Treinando o modelo
modelo.fit(X_train, y_train)

# fazendo predições com o modelo
preds = modelo.predict(X_test)

# Verificando acuracia do modelo
acuracia = accuracy_score(y_test, preds)

print(f'A acurácia do modelo é: {acuracia:.2%}')

# salvando o modelo
joblib.dump(modelo, 'modelo_xgboost.pkl')
