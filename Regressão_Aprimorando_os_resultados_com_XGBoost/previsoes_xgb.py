import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

# Função que converte colunas do tipo 'object' para 'category'
def converte_object_para_category(X):
    object_columns = X.select_dtypes(include='object').columns
    X[object_columns] = X[object_columns].astype('category')
    return X

# Transformador para a função
converte_para_category = FunctionTransformer(converte_object_para_category)

# Pipeline com o XGBoost e a conversão de tipo
pipeline = Pipeline([
    ('converte_category', converte_para_category),
    ('xgboost', xgb.XGBRegressor(enable_categorical=True))
])