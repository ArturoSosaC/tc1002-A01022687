import pandas as pd
from os import system

def readPandas(filepath, name):
    df = pd.read_csv(filepath, names=name)
    return df

def describeDataFrame(df):
    #Analize dataframe recieved
    dfFiltered_sepal_length = df['sepal length'].describe()
    dfFiltered_sepal_width = df['sepal width'].describe()
    dfFiltered_petal_length = df['petal length'].describe()
    dfFiltered_petal_width = df['petal width'].describe()

    # Print results
    print("\nSepal Length")
    print(dfFiltered_sepal_length)
    print("\nSepal Width")
    print(dfFiltered_sepal_width)
    print("\nPetaal Length")
    print(dfFiltered_petal_length)
    print("\nPetal Width")
    print(dfFiltered_petal_width)
    pressEnter()

def pressEnter():
    print("Press Enter to continue")
    while(input()!="\n"):
        break
    system('clear')
    system('clear')

if __name__ == '__main__':
    # Clear console
    system('clear')
    system('clear')

    # Create dataframe (df)
    filepath = './data/iris.data'
    names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
    df = readPandas(filepath, names)

    # Print df's head
    print(("\t"*4)+"Header\n")
    print(df.head())
    pressEnter()

    # Filter plants with sepal length lower than 4.9
    irisSetosa = df[df['sepal length']<4.9]
    print("Sepal length lower than 4.9 Analisis:")
    describeDataFrame(irisSetosa)
    # print(irisSetosa) # option to print all Iris Setosa dataframe

    # Filter plants with Sepal width between 3 and 3.5
    dfFiltered = df[df['sepal width']>3]
    dfFiltered = dfFiltered[dfFiltered['sepal width']<3.5]
    print("Sepal Width between 3 and 3.5 Analisis:")
    describeDataFrame(dfFiltered)


    # Filter plants with Petal Length lower than 1.5
    dfFilteredPeatalLength = df[df['petal length']<1.5]
    print("Petal Length lower than 1.5 Analisis:")
    describeDataFrame(dfFilteredPeatalLength)
