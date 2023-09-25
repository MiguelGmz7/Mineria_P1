import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Inicializar un diccionario para almacenar las reglas de One-R
def frequencie_table(train_data, clase_column, test_data):
    one_r_rules = {}
    class_frequencies = train_data[clase_column].value_counts()
    most_frequent_class = class_frequencies.idxmax()

    # Iterar a través de las columnas de atributos (excluyendo la columna de clase)
    for column in train_data.columns:
        if column != clase_column:
            attribute_frequencies = train_data.groupby([column, clase_column]).size().unstack(fill_value=0)
            attribute_errors = attribute_frequencies.sub(attribute_frequencies.max(axis=1), axis=0)
            best_rule = attribute_errors.idxmin()
            one_r_rules[column] = (best_rule, most_frequent_class)
            print(f"Regla de One-R para {column}: {best_rule}")
            print(f"Tabla de frecuencia para {column}:\n{attribute_frequencies}")
            input("\n Preciona enter para continuar...")
            os.system("cls")

    app_OneR(one_r_rules, test_data, most_frequent_class, clase_column)

# Aplicar las reglas de One-R al conjunto de prueba y calcular la tasa de error

def app_OneR(one_r_rules, test_data, most_frequent_class, clase_column):

    correct_predictions = 0  # Inicializar el contador de predicciones correctas

    for _, instance in test_data.iterrows():
        predicted_class = None

        for column, (best_rule, _) in one_r_rules.items():
            if (instance[column] == best_rule).any():
                predicted_class = most_frequent_class

        actual_class = instance[clase_column]

        if predicted_class == actual_class:  # Comprobar si la predicción es correcta
            correct_predictions += 1

    accuracy = correct_predictions / len(test_data)  # Calcular la tasa de acierto
    print(f"Aciertos: {correct_predictions} ")
    print("Total: ",len(test_data))
    print(f"Tasa de acierto en el conjunto de prueba: {accuracy}")
