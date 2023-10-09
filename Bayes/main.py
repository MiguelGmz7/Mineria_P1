import pandas as pd
import numpy as np
from bayes import Bayes

def split_data(data, train_ratio):
    # Obtén el número de filas para entrenamiento y prueba
    train_size = int(len(data) * train_ratio)
    train_data = data.sample(n=train_size, random_state=42)
    test_data = data.drop(train_data.index)
    
    # Restablecer los índices para el conjunto de prueba
    test_data.reset_index(drop=True, inplace=True)
    
    return train_data, test_data

def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    
    # Entrenamiento con el 100% de los datos
    bayes = Bayes()
    bayes.compute_frequency(df)
    bayes.print_tables("Tabla de Frequencia")
    bayes.compute_verisimilitude()
    bayes.print_tables("Tabla de verisimilitud")
    
    # Dividir los datos en entrenamiento (70%) y prueba (30%)
    train_data, test_data = split_data(df, train_ratio=0.7)
    
    # Practicar con el 100% de los datos
    bayes.dataframe(df)
    
    # Practicar con el 30% de los datos de prueba
    bayes.dataframe(test_data)

if __name__ == '__main__':
    main()