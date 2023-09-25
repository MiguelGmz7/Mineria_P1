import OneR
import pandas

def main ():
    filename = "../datasets/golf-dataset-categorical.csv"  # Raiz del archivo
    porcentaje_entranimento = .7 
    clase = 'Play'

    dataset = pandas.read_csv(filename)

    muestra = dataset.sample(frac=porcentaje_entranimento)
    y_train = muestra[clase]
    x_train = muestra.drop(y_train)