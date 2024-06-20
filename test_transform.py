import pandas as pd
test = pd.read_csv('test.csv')

def count_dash(test):
    return (test == '–').sum()

dash_counts =count_dash(test)

cols_with_dash = dash_counts[dash_counts > 0].index
test[cols_with_dash] = test[cols_with_dash].replace('–', np.nan)

test['fuel_type'] = test['fuel_type'].fillna(test['fuel_type'].mode()[0])
test['accident'] = test['accident'].fillna(test['accident'].mode()[0])

accident_map = {'At least 1 accident or damage reported': 1, 'None reported': 0}
test['accident'] =test['accident'].apply(lambda x : accident_map[x])

test['clean_title'] = test['clean_title'].fillna('No')

test['transmission'].fillna(test['transmission'].mode()[0], inplace=True)
test['engine'].fillna(test['engine'].mode()[0], inplace=True)
test['ext_col'].fillna(test['ext_col'].mode()[0], inplace=True)
test['int_col'].fillna(test['int_col'].mode()[0], inplace=True)

clean_title_map = {'Yes': 1, 'No': 0}
test['clean_title'] = test['clean_title'].apply(lambda x : clean_title_map[x])


test['transmission_type'] = test['transmission'].apply(lambda x: 'Automatic' if 'a/t' in x.lower() or 'automatic' in x.lower() else 'Manual')

def extract_litre_eng(engine_desc):
    match = re.search(r'(\d+(\.\d+)?)\s*[Ll](?:iter)?', engine_desc)
    return float(match.group(1)) if match else None

test['engine_litre'] = test['engine'].apply(extract_litre_eng)
test['engine_litre'].fillna(test['engine_litre'].mode()[0], inplace=True)

def extract_hp(engine_desc):
    match  = re.search(r'(\d+(\.\d+)?)HP', engine_desc)
    return float(match.group(1)) if match else None

test['hp'] = test['engine'].apply(extract_hp)
test['hp'].fillna(test['hp'].mode()[0], inplace=True)

def extract_cylinders(engine_desc):
    match = re.search(r'\b([VvIi]\d+)\b', engine_desc)
    if match:
        config = match.group(1)
        return int(config[1:])  

    match = re.search(r'(\d+(\.\d+)?)\s*L', engine_desc)
    if match:
        displacement = float(match.group(1))
        if displacement <= 2.5:
            return 4  
        elif displacement <= 3.8:
            return 6  
        else:
            return 8  
    return None


test['cylinders'] = test['engine'].apply(extract_cylinders)
test['cylinders'].fillna(test['cylinders'].mode()[0], inplace=True)


def extract_speed(transmission_desc):
    match = re.search(r'(\d+)[- ]?(Speed|Spd)', transmission_desc, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None
    

test['transmission_speed'] = test['transmission'].apply(extract_speed)

test['transmission_speed'].fillna('5', inplace= True)

cols_drop = ['id', 'engine','transmission', 'model' ]
test.drop(columns=cols_drop,axis=1, inplace=True)


cols_encode = ['brand', 'fuel_type', 'transmission_type', 'ext_col', 'int_col', 'model_year']
cols_scale = ['milage' , 'hp', 'cylinders', 'transmission_speed', 'engine_litre']


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
test[cols_encode] = test[cols_encode].apply(le.fit_transform)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
test[cols_scale] = sc.fit_transform(test[cols_scale])

