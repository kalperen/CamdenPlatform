import pandas as pd

cols = ['position', 'noseX', 'noseY', 'neckX', 'neckY', 'rshoulderX', 'rshoulderY', 'relbowX', 'relbowY', 'rwristX',
           'rwristY', 'lshoulderX', 'lshoulderY', 'lelbowX', 'lelbowY', 'lwristX', 'lwristY', 'midhipX', 'midhipY',
           'rhipX', 'rhipY', 'rkneeX', 'rkneeY', 'rankleX', 'rankleY', 'lhipX', 'lhipY', 'lkneeX', 'lkneeY', 'lankleX',
           'lankleY', 'reyeX', 'reyeY']


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


def get_data(columns=cols,
             train_dir="/Users/shahrozahmed/Desktop/IR_data/train.csv",
             valid_dir="/Users/shahrozahmed/Desktop/IR_data/validation.csv"):
    train_data = pd.read_csv(train_dir, usecols=columns)
    validation_data = pd.read_csv(valid_dir, usecols=columns)

    if ("position" in columns):
        # # encode position - train data
        encode_var(train_data, "position")
        # # encode position - validation data
        encode_var(validation_data, "position")

    if "noseX" in columns and "noseY" in columns:
        # encode nose - train data
        train_data.noseX = clean_up_data(train_data.noseX)
        train_data.noseY = clean_up_data(train_data.noseY)
        # encode nose - validation data
        validation_data.noseX = clean_up_data(validation_data.noseX)
        validation_data.noseY = clean_up_data(validation_data.noseY)

    if "neckX" in columns and "neckY" in columns:
        # encode neck - train data
        train_data.neckX = clean_up_data(train_data.neckX)
        train_data.neckY = clean_up_data(train_data.neckY)
        # encode neck - validation data
        validation_data.neckX = clean_up_data(validation_data.neckX)
        validation_data.neckY = clean_up_data(validation_data.neckY)

    if "rshoulderX" in columns and "rshoulderY" in columns:
        # encode rshoulder - train data
        train_data.rshoulderX = clean_up_data(train_data.rshoulderX)
        train_data.rshoulderY = clean_up_data(train_data.rshoulderY)
        # encode rshoulder - validation data
        validation_data.rshoulderX = clean_up_data(validation_data.rshoulderX)
        validation_data.rshoulderY = clean_up_data(validation_data.rshoulderY)

    if "relbowX" in columns and "relbowY" in columns:
        # encode relbow - train data
        train_data.relbowX = clean_up_data(train_data.relbowX)
        train_data.relbowY = clean_up_data(train_data.relbowY)
        # encode relbow - validation data
        validation_data.relbowX = clean_up_data(validation_data.relbowX)
        validation_data.relbowY = clean_up_data(validation_data.relbowY)

    if "rwristX" in columns and "rwristY" in columns:
        # encode rwrist - train data
        train_data.rwristX = clean_up_data(train_data.rwristX)
        train_data.rwristY = clean_up_data(train_data.rwristY)
        # encode rwrist - validation data
        validation_data.rwristX = clean_up_data(validation_data.rwristX)
        validation_data.rwristY = clean_up_data(validation_data.rwristY)

    if "lshoulderX" in columns and "lshoulderY" in columns:
        # encode lshoulder - train data
        train_data.lshoulderX = clean_up_data(train_data.lshoulderX)
        train_data.lshoulderY = clean_up_data(train_data.lshoulderY)
        # encode lshoulder - validation data
        validation_data.lshoulderX = clean_up_data(validation_data.lshoulderX)
        validation_data.lshoulderY = clean_up_data(validation_data.lshoulderY)

    if "lelbowX" in columns and "lelbowY" in columns:
        # encode lelbow - train data
        train_data.lelbowX = clean_up_data(train_data.lelbowX)
        train_data.lelbowY = clean_up_data(train_data.lelbowY)
        # encode lelbow - validation data
        validation_data.lelbowX = clean_up_data(validation_data.lelbowX)
        validation_data.lelbowY = clean_up_data(validation_data.lelbowY)

    if "lwristX" in columns and "lwristY" in columns:
        # encode lwrist - train data
        train_data.lwristX = clean_up_data(train_data.lwristX)
        train_data.lwristY = clean_up_data(train_data.lwristY)
        # encode lwrist - validation data
        validation_data.lwristX = clean_up_data(validation_data.lwristX)
        validation_data.lwristY = clean_up_data(validation_data.lwristY)

    if "midhipX" in columns and "midhipY" in columns:
        # encode midhip - train data
        train_data.midhipX = clean_up_data(train_data.midhipX)
        train_data.midhipY = clean_up_data(train_data.midhipY)
        # encode midhip - validation data
        validation_data.midhipX = clean_up_data(validation_data.midhipX)
        validation_data.midhipY = clean_up_data(validation_data.midhipY)

    if "rhipX" in columns and "rhipY" in columns:
        # encode rhip - train data
        train_data.rhipX = clean_up_data(train_data.rhipX)
        train_data.rhipY = clean_up_data(train_data.rhipY)
        # encode rhip - validation data
        validation_data.rhipX = clean_up_data(validation_data.rhipX)
        validation_data.rhipY = clean_up_data(validation_data.rhipY)

    if "rkneeX" in columns and "rkneeY" in columns:
        # encode rknee - train data
        train_data.rkneeX = clean_up_data(train_data.rkneeX)
        train_data.rkneeY = clean_up_data(train_data.rkneeY)
        # encode rknee - validation data
        validation_data.rkneeX = clean_up_data(validation_data.rkneeX)
        validation_data.rkneeY = clean_up_data(validation_data.rkneeY)

    if "rankleX" in columns and "rankleY" in columns:
        # encode rankle - train data
        train_data.rankleX = clean_up_data(train_data.rankleX)
        train_data.rankleY = clean_up_data(train_data.rankleY)
        # encode rankle - validation data
        validation_data.rankleX = clean_up_data(validation_data.rankleX)
        validation_data.rankleY = clean_up_data(validation_data.rankleY)

    if "lhipX" in columns and "lhipY" in columns:
        # encode lhip - train data
        train_data.lhipX = clean_up_data(train_data.lhipX)
        train_data.lhipY = clean_up_data(train_data.lhipY)
        # encode lhip - validation data
        validation_data.lhipX = clean_up_data(validation_data.lhipX)
        validation_data.lhipY = clean_up_data(validation_data.lhipY)

    if "lkneeX" in columns and "lkneeY" in columns:
        # encode lknee - train data
        train_data.lkneeX = clean_up_data(train_data.lkneeX)
        train_data.lkneeY = clean_up_data(train_data.lkneeY)
        # encode lknee - validation data
        validation_data.lkneeX = clean_up_data(validation_data.lkneeX)
        validation_data.lkneeY = clean_up_data(validation_data.lkneeY)

    if "lankleX" in columns and "lankleY" in columns:
        # encode lankle - train data
        train_data.lankleX = clean_up_data(train_data.lankleX)
        train_data.lankleY = clean_up_data(train_data.lankleY)
        # encode lankle - validation data
        validation_data.lankleX = clean_up_data(validation_data.lankleX)
        validation_data.lankleY = clean_up_data(validation_data.lankleY)

    if "reyeX" in columns and "reyeY" in columns:
        # encode reye - train data
        train_data.reyeX = clean_up_data(train_data.reyeX)
        train_data.reyeY = clean_up_data(train_data.reyeY)
        # encode reye - validation data
        validation_data.reyeX = clean_up_data(validation_data.reyeX)
        validation_data.reyeY = clean_up_data(validation_data.reyeY)

    if "leyeX" in columns and "leyeY" in columns:
        # encode leye - train data
        train_data.leyeX = clean_up_data(train_data.leyeX)
        train_data.leyeY = clean_up_data(train_data.leyeY)
        # encode leye - validation data
        validation_data.leyeX = clean_up_data(validation_data.leyeX)
        validation_data.leyeY = clean_up_data(validation_data.leyeY)

    # determine data rows
    X_train = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_train = train_data.iloc[:, 0].values  # predict position

    X_valid = validation_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_valid = validation_data.iloc[:, 0].values  # predict position

    return X_train, y_train, X_valid, y_valid, train_data, validation_data
