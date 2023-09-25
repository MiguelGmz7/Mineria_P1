import OneR
import pandas as pd


def main ():
    # filename = "../datasets/golf-dataset-categorical.csv"  # Dataset filename
    # train_sample_size = .7  # Training percentage
    # class_column_name = 'Play'

    # dataset = pandas.read_csv(filename)

    # x_train = dataset.sample(frac=train_sample_size) # agarramos el 80 porciento de toda nuestra tabla (atributos y clases)
    # y_train = x_train[class_column_name] # copiamos en una variables las puras clases
    # x_train = x_train.drop(columns=class_column_name) # eliminamos las clases de nuestro datos, (nos quedamos con los puros atributos)

    # x_test = dataset.drop(x_train.index) # Los datos que nos faltan osea el 20%, en este caso 3 instancias
    # y_test = x_test[class_column_name] #las puras clases
    # x_test = x_test.drop(columns=[class_column_name]) #los puros atributos

    file_path = '../datasets/golf-dataset-categorical.csv'
    data = pd.read_csv(file_path)
    train_sample_size = .7
    # Nombre de la columna de la clase
    clase_column = 'Play'

# Dividir el conjunto de datos en entrenamiento (70%) y prueba (30%)
# train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
    train_data = data.sample(frac=train_sample_size) # agarramos el 80 porciento de toda nuestra tabla (atributos y clases)
    y_train = train_data[clase_column] # copiamos en una variables las puras clases
    x_train = train_data.drop(columns=clase_column) # eliminamos las clases de nuestro datos, (nos quedamos con los puros atributos)

    test_data = data.drop(x_train.index) # Los datos que nos faltan osea el 20%, en este caso 3 instancias
    y_test = test_data[clase_column] #las puras clases

    OneR.frequencie_table(train_data, clase_column, test_data)
    


    

if __name__ == '__main__':
    main()