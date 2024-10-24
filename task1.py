import pandas as pd
import numpy as np

data = {
    'Neighborhood': ['Rohini', 'Pitampura', 'Haryana', 'South', 'Prashant Vihar'],
    'Housetype': ['1bhk', '2bhk', '2bhk', '1bhk', '1bhk'],
    'Condition': ['Good', 'Fair', 'Good', 'Excellent', 'Poor']
}

df = pd.DataFrame(data)

print("Original Data:", df)

def ordinal_encode(dataframe, column, ordering):

    dataframe[column + '_Ordinal'] = dataframe[column].apply(lambda x: ordering.index(x))
    return dataframe

condition_ordering = ['Poor', 'Fair', 'Good', 'Excellent']
df2 = ordinal_encode(df, 'Condition', condition_ordering)

print("\nAfter Ordinal Encoding:")
print(df2)

#ONE HOT ENCODING....
def one_hot_encode(dataframe, column):
    one_hot = pd.get_dummies(dataframe[column], prefix=column)
    dataframe = pd.concat([dataframe, one_hot], axis=1)
    dataframe.drop(column, axis=1, inplace=True)
    return dataframe

df3 = one_hot_encode(df, 'Neighborhood')
df3 = one_hot_encode(df, 'HouseType')

print("\nAfter One-Hot Encoding:")
print(df3)
