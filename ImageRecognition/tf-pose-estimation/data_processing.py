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
    series = dataset[var]
    encoded = pd.get_dummies(series, var)
    dataset = dataset.drop(var, axis=1)
    dataset = dataset.join(encoded)
    return dataset

def get_data(columns=columns):
    # importing the dataset

    train_data = pd.read_csv('/Users/shahrozahmed/Desktop/TrainingDat.csv', usecols=columns)
    validation_data = pd.read_csv('/Users/shahrozahmed/Desktop/validationDat.csv', usecols=columns)

    # encode position - train data
    encode_coord(train_data, "position")
    # encode position - validation data
    encode_coord(validation_data, "position")

    # encode nose - train data
    encode_coord(train_data, "nose")
    # encode nose - validation data
    encode_coord(validation_data, "nose")

    # encode neck - train data
    encode_coord(train_data, "neck")
    # encode neck - validation data
    encode_coord(validation_data, "neck")

    # encode rshoulder - train data
    encode_coord(train_data, "rshoulder")
    # encode rshoulder - validation data
    encode_coord(validation_data, "rshoulder")

    # encode relbow - train data
    encode_coord(train_data, "relbow")
    # encode relbow - validation data
    encode_coord(validation_data, "relbow")

    # encode rwrist - train data
    encode_coord(train_data, "rwrist")
    # encode rwrist - validation data
    encode_coord(validation_data, "rwrist")

    # encode lshoulder - train data
    encode_coord(train_data, "lshoulder")
    # encode lshoulder - validation data
    encode_coord(validation_data, "lshoulder")

    # encode lelbow - train data
    encode_coord(train_data, "lelbow")
    # encode lelbow - validation data
    encode_coord(validation_data, "lelbow")

    # encode lwrist - train data
    encode_coord(train_data, "lwrist")
    # encode lwrist - validation data
    encode_coord(validation_data, "lwrist")

    # encode midhip - train data
    encode_coord(train_data, "midhip")
    # encode midhip - validation data
    encode_coord(validation_data, "midhip")

    # encode rhip - train data
    encode_coord(train_data, "rhip")
    # encode rhip - validation data
    encode_coord(validation_data, "rhip")

    # encode rknee - train data
    encode_coord(train_data, "rknee")
    # encode rknee - validation data
    encode_coord(validation_data, "rknee")

    # encode rankle - train data
    encode_coord(train_data, "rankle")
    # encode rankle - validation data
    encode_coord(validation_data, "rankle")

    # encode lhip - train data
    encode_coord(train_data, "lhip")
    # encode lhip - validation data
    encode_coord(validation_data, "lhip")

    # encode lknee - train data
    encode_coord(train_data, "lknee")
    # encode lknee - validation data
    encode_coord(validation_data, "lknee")

    # encode lankle - train data
    encode_coord(train_data, "lankle")
    # encode lankle - validation data
    encode_coord(validation_data, "lankle")

    # encode reye - train data
    encode_coord(train_data, "reye")
    # encode reye - validation data
    encode_coord(validation_data, "reye")

    # encode leye - train data
    encode_coord(train_data, "leye")
    # encode leye - validation data
    encode_coord(validation_data, "leye")

    # encode rear - train data
    encode_coord(train_data, "rear")
    # encode rear - validation data
    encode_coord(validation_data, "rear")

# determine data rows
    X_train = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_train = train_data.iloc[:, 0].values  # predict position

    X_valid = validation_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_valid = validation_data.iloc[:, 0].values  # predict position

    return X_train, y_train, X_valid, y_valid, train_data, validation_data
