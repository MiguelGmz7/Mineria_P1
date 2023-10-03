import pandas as pd
def split(data):
    frequency = {}
    index = 0

    for column_name in data.columns:
        frequency[column_name] = {}
        for value in data[column_name]:
            index += 1
            if data[column_name].dtypes == 'object':
                if value not in frequency[column_name]:
                    frequency[column_name][value] = 1
                else:
                    frequency[column_name][value] += 1
            else:
                frequency[column_name][index] = value
        index = 0
        #-----
        #if data[column_name].dtypes == 'float64':

    return frequency

def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    #train_sample_size = .7
    #print(df)
    #print(df.columns)
    #print(df.dtypes)
    #print(df.describe())
    #print(df.head())
    # como uso el metodo split de la clase Bayes
    frecuency = split(df)
    print(frecuency)

if __name__ == '__main__':
    main()