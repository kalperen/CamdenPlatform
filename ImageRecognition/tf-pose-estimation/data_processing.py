import pandas as pd

columns = ['position', 'nose', 'neck', 'rshoulder', 'relbow', 'rwrist', 'lshoulder', 'lelbow',
        'lwrist', 'midhip', 'rhip', 'rknee', 'rankle', 'lhip', 'lknee', 'lankle', 'reye', 'leye', 'rear']

def encode_var(dataset, variable):
    series = pd.Series(dataset[variable])
    encoded_domains = pd.get_dummies(series)
    dataset = dataset.drop(variable, axis=1)
    dataset = dataset.join(encoded_domains)
    return dataset

def encode_coord(dataset, var):
    #dataset[var] = dataset[var].astype('float64')
    return dataset

def encode_coord2(dataset, var):
    series = dataset[var]
    encoded = pd.get_dummies(series, var)
    dataset = dataset.drop(var, axis=1)
    dataset = dataset.join(encoded)
    return dataset

def encode_coord3(dataset, var):
    newColumns = dataset[var].str.get_dummies(sep=',')
    dataset = dataset.drop(var, axis=1)
    dataset = dataset.join(newColumns)
    return dataset

def get_data(columns=columns):
    # importing the dataset

    train_data = pd.read_csv('/Users/shahrozahmed/Desktop/IR_data/TrainingDat.csv', usecols=columns)
    validation_data = pd.read_csv('/Users/shahrozahmed/Desktop/IR_data/validationDat.csv', usecols=columns)

    #
    #
    # X_train = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    # y_train = train_data.iloc[:, 0].values  # predict position
    #
    # X_valid = validation_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    # y_valid = validation_data.iloc[:, 0].values  # predict position
    #
    # return X_train, y_train, X_valid, y_valid, train_data, validation_data

    # # encode position - train data
    encode_var(train_data, "position")
    # # encode position - validation data
    encode_var(validation_data, "position")

    print("0")

    # encode nose - train data

    train_data.nose = train_data.nose.astype(float).astype('float64')
    train_data.nose =\
        train_data.nose.astype(float).fillna(0.0)
    encode_coord(train_data, "nose")
    # encode nose - validation data
    validation_data.nose = validation_data.nose.astype(float).fillna(0.0)
    encode_coord(validation_data, "nose")

    print("1")
    # encode neck - train data
    train_data.neck = train_data.neck.astype(float).fillna(0.0)
    encode_coord(train_data, "neck")
    # encode neck - validation data
    validation_data.neck = validation_data.neck.astype(float).fillna(0.0)
    encode_coord(validation_data, "neck")

    print("2")
    # encode rshoulder - train data
    train_data.rshoulder = train_data.rshoulder.astype(float).fillna(0.0)
    encode_coord(train_data, "rshoulder")
    # encode rshoulder - validation data
    validation_data.rshoulder = validation_data.rshoulder.astype(float).fillna(0.0)
    encode_coord(validation_data, "rshoulder")

    print("2.5")
    # encode relbow - train data
    train_data.relbow = train_data.relbow.astype(float).fillna(0.0)
    encode_coord(train_data, "relbow")
    # encode relbow - validation data
    validation_data.relbow = validation_data.relbow.astype(float).fillna(0.0)
    encode_coord(validation_data, "relbow")

    print("3")
    # encode rwrist - train data
    train_data.rwrist = train_data.rwrist.astype(float).fillna(0.0)
    encode_coord(train_data, "rwrist")
    # encode rwrist - validation data
    validation_data.rwrist = validation_data.rwrist.astype(float).fillna(0.0)
    encode_coord(validation_data, "rwrist")

    print("4")
    # encode lshoulder - train data
    train_data.lshoulder = train_data.lshoulder.astype(float).fillna(0.0)
    encode_coord(train_data, "lshoulder")
    # encode lshoulder - validation data
    validation_data.lshoulder = validation_data.lshoulder.astype(float).fillna(0.0)
    encode_coord(validation_data, "lshoulder")

    # encode lelbow - train data
    train_data.lelbow = train_data.lelbow.astype(float).fillna(0.0)
    encode_coord(train_data, "lelbow")
    # encode lelbow - validation data
    validation_data.lelbow = validation_data.lelbow.astype(float).fillna(0.0)
    encode_coord(validation_data, "lelbow")

    # encode lwrist - train data
    train_data.lwrist = train_data.lwrist.astype(float).fillna(0.0)
    encode_coord(train_data, "lwrist")
    # encode lwrist - validation data
    validation_data.lwrist = validation_data.lwrist.astype(float).fillna(0.0)
    encode_coord(validation_data, "lwrist")

    # encode midhip - train data
    train_data.midhip = train_data.midhip.astype(float).fillna(0.0)
    encode_coord(train_data, "midhip")
    # encode midhip - validation data
    validation_data.midhip = validation_data.midhip.astype(float).fillna(0.0)
    encode_coord(validation_data, "midhip")

    # encode rhip - train data
    train_data.rhip = train_data.rhip.astype(float).fillna(0.0)
    encode_coord(train_data, "rhip")
    # encode rhip - validation data
    validation_data.rhip = validation_data.rhip.astype(float).fillna(0.0)
    encode_coord(validation_data, "rhip")

    # encode rknee - train data
    train_data.rknee = train_data.rknee.astype(float).fillna(0.0)
    encode_coord(train_data, "rknee")
    # encode rknee - validation data
    validation_data.rknee = validation_data.rknee.astype(float).fillna(0.0)
    encode_coord(validation_data, "rknee")

    # encode rankle - train data
    train_data.rankle = train_data.rankle.astype(float).fillna(0.0)
    encode_coord(train_data, "rankle")
    # encode rankle - validation data
    validation_data.rankle = validation_data.rankle.astype(float).fillna(0.0)
    encode_coord(validation_data, "rankle")

    # encode lhip - train data
    train_data.lhip = train_data.lhip.astype(float).fillna(0.0)
    encode_coord(train_data, "lhip")
    # encode lhip - validation data
    validation_data.lhip = validation_data.lhip.astype(float).fillna(0.0)
    encode_coord(validation_data, "lhip")

    # encode lknee - train data
    train_data.lknee = train_data.lknee.astype(float).fillna(0.0)
    encode_coord(train_data, "lknee")
    # encode lknee - validation data
    validation_data.lknee = validation_data.lknee.astype(float).fillna(0.0)
    encode_coord(validation_data, "lknee")

    # encode lankle - train data
    train_data.lankle = train_data.lankle.astype(float).fillna(0.0)
    encode_coord(train_data, "lankle")
    # encode lankle - validation data
    validation_data.lankle = validation_data.lankle.astype(float).fillna(0.0)
    encode_coord(validation_data, "lankle")

    # encode reye - train data
    train_data.reye = train_data.reye.astype(float).fillna(0.0)
    encode_coord(train_data, "reye")
    # encode reye - validation data
    validation_data.reye = validation_data.reye.astype(float).fillna(0.0)
    encode_coord(validation_data, "reye")

    # encode leye - train data
    train_data.leye = train_data.leye.astype(float).fillna(0.0)
    encode_coord(train_data, "leye")
    # encode leye - validation data
    validation_data.leye = validation_data.leye.astype(float).fillna(0.0)
    encode_coord(validation_data, "leye")

    # encode rear - train data
    train_data.rear = train_data.rear.astype(float).fillna(0.0)
    encode_coord(train_data, "rear")
    # encode rear - validation data
    validation_data.rear = validation_data.rear.astype(float).fillna(0.0)
    encode_coord(validation_data, "rear")

# determine data rows
    X_train = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_train = train_data.iloc[:, 0].values  # predict position

    X_valid = validation_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_valid = validation_data.iloc[:, 0].values  # predict position

    return X_train, y_train, X_valid, y_valid, train_data, validation_data


