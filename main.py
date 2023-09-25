import OneR
import pandas

def main ():
    filename = "../datasets/golf-dataset-categorical.csv"  # Raiz del archivo
    porcentaje_entranimento = .7 
    clase = 'Play'

    dataset = pandas.read_csv(filename)

    muestra_entrenamiento = dataset.sample(frac=porcentaje_entranimento)
    y_train = muestra_entrenamiento[clase]
    x_train = muestra_entrenamiento.drop(y_train)

    muestra_test = dataset.drop(x_train.index)
    y_test = muestra_test[clase]
    x_test = muestra_test.drop(y_test)