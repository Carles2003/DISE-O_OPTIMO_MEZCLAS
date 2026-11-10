import pandas as pd

#cargar datos 
ruta = "https://raw.githubusercontent.com/Carles2003/DISE-O_OPTIMO_MEZCLAS/refs/heads/main/datos_concreto.csv"
df = pd.read_csv(ruta)

print("="*50)
print(df.head())
print("="*50)

print("="*50)
print(df.info())
print("="*50)

print("="*50)
print(df.describe())
print("="*50)

print("="*50)
print(df.columns)
print("="*50)

print("="*50)
print(df.isnull().sum())
print("="*50)

print("="*50)
print(df.shape) #filas columnas
print("="*50)

print("="*50)
print(df["Resistencia a la compresión (MPa)"])
print("="*50)

print("="*50)
print(df[["Cemento (kg/m³)","Resistencia a la compresión (MPa)"]])
print("="*50)

print("="*50)
print(df[df["Edad (días)"]==28])
print("="*50)