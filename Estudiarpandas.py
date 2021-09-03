import pandas as pd
datos={
     'temperaturas':[10, 20, 22, 12, 26, 31, 42],
     'Poblacion':[20000, 15000, 9000, 11000, 25000, 20000, 9000]
}
df=pd.DataFrame(datos, index=['Tunja', 'Puerto inrida', 'Caqueta', 'Villavicencio', 'Bogota', 'Cali', 'total promedio'])
print(df)