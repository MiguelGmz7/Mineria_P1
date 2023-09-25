import OneR
import pandas as pd
import os

def main ():
    file_path = '../datasets/golf-dataset-categorical.csv'
    data = pd.read_csv(file_path)
    train_sample_size = .7

    # Nombre de la columna de la clase
    clase_column = 'Play'


    train_data = data.sample(frac=train_sample_size) # agarramos el 80 porciento de toda nuestra tabla (atributos y clases)

    test_data = data.drop(train_data.index) # Los datos que nos faltan osea el 20%, en este caso 3 instancias
    test_data
    
    one_r_rules, most_frequent_class = OneR.frequencie_table(train_data, clase_column, test_data)

    OneR.app_OneR(one_r_rules, test_data, most_frequent_class, clase_column) 


if __name__ == '__main__':
    main()