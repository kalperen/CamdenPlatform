import pandas as pd

columns = ['position', 'noseX', 'noseY', 'neckX', 'neckY', 'rshoulderX','rshoulderY', 'relbowX', 'relbowY', 'rwristX',
           'rwristY', 'lshoulderX','lshoulderY', 'lelbowX', 'lelbowY', 'lwristX','lwristY', 'midhipX','midhipY',
           'rhipX','rhipY', 'rkneeX','rkneeY', 'rankleX', 'rankleY', 'lhipX','lhipY', 'lkneeX','lkneeY', 'lankleX',
           'lankleY', 'reyeX', 'reyeY', 'leyeX','leyeY']


def encode_var(dataset, variable):
    series = pd.Series(dataset[variable])
    encoded_domains = pd.get_dummies(series)
    dataset = dataset.drop(variable, axis=1)
    dataset = dataset.join(encoded_domains)
    return dataset


def clean_up_data(dataset):
    dataset = (dataset.fillna('0.0'))
    dataset = dataset.astype(float).astype('float64')
    dataset = dataset.astype(float).fillna(0.0)
    return dataset


def array_cleaning(dataset):
    dataset = (dataset.fillna('0.0,0.0'))
    sp = []
    for item in dataset:
        xy = item.split(',')
        joint_list.append(xy)
    nparray = np.array(joint_list)
    np_float = nparray.astype(np.float)
    dataset = np_float.tolist()
    return dataset


def get_data(columns=columns):

    train_data = pd.read_csv('/Users/alperen/Desktop/CamdenPlatform/ImageRecognition/featureExtraction/train.csv', usecols=columns)
    validation_data = pd.read_csv('/Users/alperen/Desktop/CamdenPlatform/ImageRecognition/featureExtraction/validation.csv', usecols=columns)

    # # encode position - train data
    encode_var(train_data, "position")
    # # encode position - validation data
    encode_var(validation_data, "position")

    # encode nose - train data
    clean_up_data(train_data.noseX)
    clean_up_data(train_data.noseY)
    # encode nose - validation data
    clean_up_data(validation_data.noseX)
    clean_up_data(validation_data.noseY)

    # encode neck - train data
    clean_up_data(train_data.neckX)
    clean_up_data(train_data.neckY)
    # encode neck - validation data
    clean_up_data(validation_data.neckX)
    clean_up_data(validation_data.neckY)

    # encode rshoulder - train data
    clean_up_data(train_data.rshoulderX)
    clean_up_data(train_data.rshoulderY)
    # encode rshoulder - validation data
    clean_up_data(validation_data.rshoulderX)
    clean_up_data(validation_data.rshoulderY)

    # encode relbow - train data
    clean_up_data(train_data.relbowX)
    clean_up_data(train_data.relbowY)
    # encode relbow - validation data
    clean_up_data(validation_data.relbowX)
    clean_up_data(validation_data.relbowY)

    # encode rwrist - train data
    clean_up_data(train_data.rwristX)
    clean_up_data(train_data.rwristY)
    # encode rwrist - validation data
    clean_up_data(validation_data.rwristX)
    clean_up_data(validation_data.rwristY)

    # encode lshoulder - train data
    clean_up_data(train_data.lshoulderX)
    clean_up_data(train_data.lshoulderY)
    # encode lshoulder - validation data
    clean_up_data(validation_data.lshoulderX)
    clean_up_data(validation_data.lshoulderY)

    # encode lelbow - train data
    clean_up_data(train_data.lelbowX)
    clean_up_data(train_data.lelbowY)
    # encode lelbow - validation data
    clean_up_data(validation_data.lelbowX)
    clean_up_data(validation_data.lelbowY)

    # encode lwrist - train data
    clean_up_data(train_data.lwristX)
    clean_up_data(train_data.lwristY)
    # encode lwrist - validation data
    clean_up_data(validation_data.lwristX)
    clean_up_data(validation_data.lwristY)

    # encode midhip - train data
    clean_up_data(train_data.midhipX)
    clean_up_data(train_data.midhipY)
    # encode midhip - validation data
    clean_up_data(validation_data.midhipX)
    clean_up_data(validation_data.midhipY)

    # encode rhip - train data
    clean_up_data(train_data.rhipX)
    clean_up_data(train_data.rhipY)
    # encode rhip - validation data
    clean_up_data(validation_data.rhipX)
    clean_up_data(validation_data.rhipY)

    # encode rknee - train data
    clean_up_data(train_data.rkneeX)
    clean_up_data(train_data.rkneeY)
    # encode rknee - validation data
    clean_up_data(validation_data.rkneeX)
    clean_up_data(validation_data.rkneeY)

    # encode rankle - train data
    clean_up_data(train_data.rankleX)
    clean_up_data(train_data.rankleY)
    # encode rankle - validation data
    clean_up_data(validation_data.rankleX)
    clean_up_data(validation_data.rankleY)

    # encode lhip - train data
    clean_up_data(train_data.lhipX)
    clean_up_data(train_data.lhipY)
    # encode lhip - validation data
    clean_up_data(validation_data.lhipX)
    clean_up_data(validation_data.lhipY)

    # encode lknee - train data
    clean_up_data(train_data.lkneeX)
    clean_up_data(train_data.lkneeY)
    # encode lknee - validation data
    clean_up_data(validation_data.lkneeX)
    clean_up_data(validation_data.lkneeY)

    # encode lankle - train data
    clean_up_data(train_data.lankleX)
    clean_up_data(train_data.lankleY)
    # encode lankle - validation data
    clean_up_data(validation_data.lankleX)
    clean_up_data(validation_data.lankleY)

    # encode reye - train data
    clean_up_data(train_data.reyeX)
    clean_up_data(train_data.reyeY)
    # encode reye - validation data
    clean_up_data(validation_data.reyeX)
    clean_up_data(validation_data.reyeY)

    # encode leye - train data
    clean_up_data(train_data.leyeX)
    clean_up_data(train_data.leyeY)
    # encode leye - validation data
    clean_up_data(validation_data.leyeX)
    clean_up_data(validation_data.leyeY)

# determine data rows
    X_train = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_train = train_data.iloc[:, 0].values  # predict position

    X_valid = validation_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_valid = validation_data.iloc[:, 0].values  # predict position

    return X_train, y_train, X_valid, y_valid, train_data, validation_data
