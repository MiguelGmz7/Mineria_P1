import pandas as pd
def split(data):
    frequency = {} # creamos un diccionario para la tabla de frecuencia 
    for column_name in data.columns: # va a iterar en cada columna 
        frequency[column_name] = {} # Cada elemento del diccionario sera otro diccionario {'sepal-width':{'1':21, '2':34}}
        index = 0 # indice de en que lugar estamos de las instancias (se usa en las numericas)
        count = 0 # sumatoria de cada valor de las numericas (Se usa en el promedio)
        for value in data[column_name]: #vamos a iterar por cada valor de cada columna
            index += 1 # nuestro indice al principio valdra 1
            if data[column_name].dtypes == 'object': # si la columna es de tipo objeto, va a pasar: 
                if value not in frequency[column_name]: # si el que tenemos de 'data' aun no esta en el diccionario de frec, se pone 1
                    frequency[column_name][value] = 1 # {'petal-length(column_name)': {'<0.8(value)': 1}}
                else: # si ya existe en nuestro diccionario se le suma un valor
                    frequency[column_name][value] += 1# {'petal-length(column_name)': {'<0.8(value)': 2}}
            else: # si la columna no es de tipo objeto
                count += value # el contador va a ser 0 + el valor numerico
                frequency[column_name][index] = value #{'sepal-length': {'1': 4.7, '2': 7.2}}
        #-----
        if data[column_name].dtypes == 'float64': #si nos encontramos en una columna numerica al final
            media = count / index # se calcula el promedio
            frequency[column_name]['media'] = media #agregamos otra key al diccionario al final {'sepal-length': {..., '14': 6,'15':6.3, 'media': 6.3333}}
    return frequency
                
                            
# crea una funcion que reciba un dataframe y retorne un diccionario con la tabla de frecuencia segun su iris
def frequency(data):
    frequency = {}
    for column_name in data:
        frequency[column_name] = {}
        frequency[column_name]['Iris-setosa'] = {}
        frequency[column_name]['Iris-virginica'] = {}
        frequency[column_name]['Iris-versicolor'] = {}
        x = 0
        y = 0
        z = 0
        
        for index, row in data.iterrows():

            if data.iloc[index]['iris'] == 'Iris-setosa':
                x += 1
                if column_name == 'sepal-length':
                    frequency[column_name]['Iris-setosa'][x] = data.iloc[index]['sepal-length']
                if column_name == 'sepal-width':
                    value = data.iloc[index]['sepal-width']
                    if value not in frequency[column_name]['Iris-setosa']:
                        frequency[column_name]['Iris-setosa'][value] = 1
                    else:
                        frequency[column_name]['Iris-setosa'][value] += 1
                    
            if data.iloc[index]['iris'] == 'Iris-virginica':
                y += 1
                if column_name == 'sepal-length':
                    frequency[column_name]['Iris-virginica'][y] = data.iloc[index]['sepal-length']
            
            if data.iloc[index]['iris'] == 'Iris-versicolor':
                z += 1
                if column_name == 'sepal-length':
                    frequency[column_name]['Iris-versicolor'][z] = data.iloc[index]['sepal-length']
    return frequency


def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    #train_sample_size = .7
    #print(df)
    #print(df)
    #print(df.dtypes)
    #print(df.describe())
    #print(df.head())
    # como uso el metodo split de la clase Bayes
    #frecuency = split(df)
    #print(frecuency)
    # como pasar por cada una de las instancias del dataframe
    print(frequency(df))
if __name__ == '__main__':
    main()