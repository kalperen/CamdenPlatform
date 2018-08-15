import os

import pandas as pd

cols = ['position', 'noseX', 'noseY', 'neckX', 'neckY', 'neckZ', 'noseZ', 'neckX', 'neckY', 'neckZ', 'rshoulderX',
        'rshoulderY', 'rshoulderZ', 'relbowX', 'relbowY', 'relbowZ', 'rwristX', 'rwristY', 'rwristZ', 'lshoulderX',
        'lshoulderY', 'lshoulderZ', 'lelbowX', 'lelbowY', 'lelbowZ', 'lwristX', 'lwristY', 'lwristZ', 'midhipX',
        'midhipY', 'midhipZ', 'rhipX', 'rhipY', 'rhipZ', 'rkneeX', 'rkneeY', 'rkneeZ', 'rankleX', 'rankleY', 'rankleZ',
        'lhipX', 'lhipY', 'lhipZ', 'lkneeX', 'lkneeY', 'lkneeZ', 'lankleX', 'lankleY', 'lankleZ', 'leyeX', 'leyeY',
        'leyeZ']

#csv_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "/featureExtraction/tf-pose-estimation/validation.csv"
csv_dir = '/Users/shahrozahmed/Desktop/openpose_trainingv1.csv'


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
             data_dir=csv_dir):
    train_data = pd.read_csv(data_dir, usecols=columns, engine="python")

    if ("position" in columns):
        # # encode position - train data
        encode_var(train_data, "position")

    if "noseX" in columns and "noseY" in columns and "noseZ" in columns:
        # encode nose - train data
        train_data.noseX = clean_up_data(train_data.noseX)
        train_data.noseY = clean_up_data(train_data.noseY)
        train_data.noseZ = clean_up_data(train_data.noseZ)

    if "neckX" in columns and "neckY" in columns and "neckZ" in columns:
        # encode neck - train data
        train_data.neckX = clean_up_data(train_data.neckX)
        train_data.neckY = clean_up_data(train_data.neckY)
        train_data.neckZ = clean_up_data(train_data.neckZ)

    if "rshoulderX" in columns and "rshoulderY" in columns and "rshoulderZ" in columns:
        # encode rshoulder - train data
        train_data.rshoulderX = clean_up_data(train_data.rshoulderX)
        train_data.rshoulderY = clean_up_data(train_data.rshoulderY)
        train_data.rshoulderZ = clean_up_data(train_data.rshoulderZ)

    if "relbowX" in columns and "relbowY" in columns and "relbowZ" in columns:
        # encode relbow - train data
        train_data.relbowX = clean_up_data(train_data.relbowX)
        train_data.relbowY = clean_up_data(train_data.relbowY)
        train_data.relbowZ = clean_up_data(train_data.relbowZ)

    if "rwristX" in columns and "rwristY" in columns and "rwristZ" in columns:
        # encode rwrist - train data
        train_data.rwristX = clean_up_data(train_data.rwristX)
        train_data.rwristY = clean_up_data(train_data.rwristY)
        train_data.rwristZ = clean_up_data(train_data.rwristZ)

    if "lshoulderX" in columns and "lshoulderY" in columns and "lshoulderZ" in columns:
        # encode lshoulder - train data
        train_data.lshoulderX = clean_up_data(train_data.lshoulderX)
        train_data.lshoulderY = clean_up_data(train_data.lshoulderY)
        train_data.lshoulderZ = clean_up_data(train_data.lshoulderZ)

    if "lelbowX" in columns and "lelbowY" in columns and "lelbowZ" in columns:
        # encode lelbow - train data
        train_data.lelbowX = clean_up_data(train_data.lelbowX)
        train_data.lelbowY = clean_up_data(train_data.lelbowY)
        train_data.lelbowZ = clean_up_data(train_data.lelbowZ)

    if "lwristX" in columns and "lwristY" in columns and "lwristZ" in columns:
        # encode lwrist - train data
        train_data.lwristX = clean_up_data(train_data.lwristX)
        train_data.lwristY = clean_up_data(train_data.lwristY)
        train_data.lwristZ = clean_up_data(train_data.lwristZ)

    if "midhipX" in columns and "midhipY" in columns and "midhipZ" in columns:
        # encode midhip - train data
        train_data.midhipX = clean_up_data(train_data.midhipX)
        train_data.midhipY = clean_up_data(train_data.midhipY)
        train_data.midhipZ = clean_up_data(train_data.midhipZ)

    if "rhipX" in columns and "rhipY" in columns and "rhipZ" in columns:
        # encode rhip - train data
        train_data.rhipX = clean_up_data(train_data.rhipX)
        train_data.rhipY = clean_up_data(train_data.rhipY)
        train_data.rhipZ = clean_up_data(train_data.rhipZ)

    if "rkneeX" in columns and "rkneeY" in columns and "rkneeY" in columns:
        # encode rknee - train data
        train_data.rkneeX = clean_up_data(train_data.rkneeX)
        train_data.rkneeY = clean_up_data(train_data.rkneeY)
        train_data.rkneeZ = clean_up_data(train_data.rkneeZ)

    if "rankleX" in columns and "rankleY" in columns and "rankleZ" in columns:
        # encode rankle - train data
        train_data.rankleX = clean_up_data(train_data.rankleX)
        train_data.rankleY = clean_up_data(train_data.rankleY)
        train_data.rankleZ = clean_up_data(train_data.rankleZ)

    if "lhipX" in columns and "lhipY" in columns and "lhipZ" in columns:
        # encode lhip - train data
        train_data.lhipX = clean_up_data(train_data.lhipX)
        train_data.lhipY = clean_up_data(train_data.lhipY)
        train_data.lhipZ = clean_up_data(train_data.lhipZ)

    if "lkneeX" in columns and "lkneeY" in columns and "lkneeZ" in columns:
        # encode lknee - train data
        train_data.lkneeX = clean_up_data(train_data.lkneeX)
        train_data.lkneeY = clean_up_data(train_data.lkneeY)
        train_data.lkneeZ = clean_up_data(train_data.lkneeZ)

    if "lankleX" in columns and "lankleY" in columns and "lankleZ" in columns:
        # encode lankle - train data
        train_data.lankleX = clean_up_data(train_data.lankleX)
        train_data.lankleY = clean_up_data(train_data.lankleY)
        train_data.lankleZ = clean_up_data(train_data.lankleZ)

    if "reyeX" in columns and "reyeY" in columns and "reyeZ" in columns:
        # encode reye - train data
        train_data.reyeX = clean_up_data(train_data.reyeX)
        train_data.reyeY = clean_up_data(train_data.reyeY)
        train_data.reyeZ = clean_up_data(train_data.reyeZ)

    if "leyeX" in columns and "leyeY" in columns and "leyeZ" in columns:
        # encode leye - train data
        train_data.leyeX = clean_up_data(train_data.leyeX)
        train_data.leyeY = clean_up_data(train_data.leyeY)
        train_data.leyeZ = clean_up_data(train_data.leyeZ)

    # determine data rows
    data = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    labels = train_data.iloc[:, 0].values  # predict position

    return data, labels
