import OneR
import pandas as pd


def main ():
    file_path = '../datasets/golf-dataset-categorical.csv'
    data = pd.read_csv(file_path)
    train_sample_size = .7

    # Nombre de la columna de la clase
    clase_column = 'Play'


    train_data = data.sample(frac=train_sample_size) # agarramos el 80 porciento de toda nuestra tabla (atributos y clases)
    y_train = train_data[clase_column] # copiamos en una variables las puras clases
    x_train = train_data.drop(columns=clase_column) # eliminamos las clases de nuestro datos, (nos quedamos con los puros atributos)

    test_data = data.drop(x_train.index) # Los datos que nos faltan osea el 20%, en este caso 3 instancias
    y_test = test_data[clase_column] #las puras clases

    OneR.frequencie_table(train_data, clase_column, test_data)
    

if __name__ == '__main__':
    main()