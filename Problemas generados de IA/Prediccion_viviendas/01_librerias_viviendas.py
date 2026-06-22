# ============================================
# PASO 2 — Importación de librerías
# ============================================

# Manipulación de datos

import pandas as pd
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ============================================
# PASO 3 — Cargar dataset y renombrar columnas
# ============================================

df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")

# El dataset viene TODO en minúsculas → renombramos 'medv' a 'price'
df = df.rename(columns={"medv": "price"})

print("\nColumnas del DataFrame:")
print(df.columns)

print("\nPrimeras filas:")
print(df.head())



# ============================================
# PASO 4 — Exploración de Datos (EDA)
# ============================================

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

plt.figure(figsize=(8,5))
sns.histplot(df["price"], kde=True)
plt.title("Distribución del precio")
plt.show()

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()


# ============================================
# PASO 5 — Limpieza de datos
# ============================================

print("\nValores nulos:")
print(df.isnull().sum())

print("\nTipos de datos:")
print(df.dtypes)

plt.figure(figsize=(8,5))
sns.boxplot(x=df["price"])
plt.title("Outliers en price")
plt.show()

print("\nDuplicados:", df.duplicated().sum())




# ============================================
# PASO 6 — Feature Engineering
# ============================================

# Densidad (indus * nox)
df["density"] = df["indus"] * df["nox"]

# Índice de calidad (rm / ptratio)
df["quality_index"] = df["rm"] / df["ptratio"]

# Log de criminalidad
df["crim_log"] = np.log1p(df["crim"])

# Categorías de precio
df["price_cat"] = pd.qcut(df["price"], q=3, labels=["low", "medium", "high"])

print("\nColumnas finales:")
print(df.columns)


# ============================================
# PASO 7 — División Train/Test
# ============================================

X = df.drop(["price", "price_cat"], axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTamaños:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)


# ============================================
# PASO 8 — Entrenamiento del modelo
# ============================================

modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("\nModelo entrenado.")


# ============================================
# PASO 9 — Predicciones
# ============================================

y_pred = modelo.predict(X_test)

print("\nPrimeras predicciones:")
print(y_pred[:5])


# ============================================
# PASO 10 — Evaluación del modelo
# ============================================

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nResultados:")
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

