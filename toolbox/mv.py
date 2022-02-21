import numpy as np
from sklearn.impute import SimpleImputer

def overview(data):
    duplicate_count = data.duplicated().sum()
    return f'there are {duplicate_count} duplicates'

def drop_duplicates(data):
    data = data.drop_duplicates()
    print(overview(data))
    return data

def check_percentage(data):
    a = data.isnull().sum().sort_values(ascending=False)
    b = data.isnull().sum().sort_values(ascending=False)/len(data)
    print('greater than 30%: drop; less than 30%: impute')
    return a,b

def missing_data(data, column_name, mode, strategy="median"):
    '''
    Option 1: replace
    Option 2: impute
    Option 3: drop
    '''
    if mode=='replace':
        data.column_name.replace(np.nan,column_name, inplace=False)
    elif mode=='impute':
        imputer = SimpleImputer(strategy=strategy)
        imputer.fit(data[[str(column_name)]])
        data[str(column_name)] = imputer.transform(data[[column_name]])
    elif mode=='drop':
        data.drop(columns=column_name, inplace=False)
    else:
        print('choose from replace, impute and drop')
    return data
