import pandas as pd

cols = ['position', 'nose', 'neck', 'rshoulder', 'relbow', 'rwrist', 'lshoulder', 'lelbow',
        'lwrist', 'midhip', 'rhip', 'rknee', 'rankle', 'lhip', 'lknee', 'lankle', 'reye', 'leye', 'rear']


def encode_var(dataset, variable):
    series = pd.Series(dataset[variable])
    encoded_domains = pd.get_dummies(series)
    dataset = dataset.drop(variable, axis=1)
    dataset = dataset.join(encoded_domains)
    return dataset

def get_data(columns=cols):
    # importing the dataset

    train_data = pd.read_csv('/Users/shahrozahmed/Desktop/TrainingDat.csv', usecols=columns)  # validationing_data
    validation_data = pd.read_csv('/Users/shahrozahmed/Desktop/TrainingDat.csv', usecols=columns)

    # encode position - train data
    positionSeries = pd.Series(train_data['position'])
    position_encoded = pd.get_dummies(positionSeries, 'position')
    train_data = train_data.drop('position', axis=1)
    train_data = train_data.join(position_encoded)
    # encode position - validation data
    position_series = pd.Series(validation_data['position'])
    position_encoded = pd.get_dummies(position_series, 'position')
    validation_data = validation_data.drop('hour', axis=1)
    validation_data = validation_data.join(position_encoded)

    # encode nose - train data
    nose_series = train_data['nose']
    nose_encoded = pd.get_dummies(nose_series, 'nose')
    train_data = train_data.drop('nose', axis=1)
    train_data = train_data.join(nose_encoded)
    # encode nose - validation data
    nose_series = validation_data['nose']
    nose_encoded = pd.get_dummies(nose_series, 'nose')
    validation_data = validation_data.drop('nose', axis=1)
    validation_data = validation_data.join(nose_encoded)

    # encode neck - train data
    neck_series = train_data['neck']
    neck_encoded = pd.get_dummies(neck_series, 'neck')
    train_data = train_data.drop('neck', axis=1)
    train_data = train_data.join(neck_encoded)
    # encode neck - validation data
    neck_series = validation_data['neck']
    neck_encoded = pd.get_dummies(neck_series, 'neck')
    validation_data = validation_data.drop('neck', axis=1)
    validation_data = validation_data.join(neck_encoded)

    # encode rshoulder - train data
    rshoulder_series = train_data['rshoulder']
    rshoulder_encoded = pd.get_dummies(rshoulder_series, 'rshoulder')
    train_data = train_data.drop('rshoulder', axis=1)
    train_data = train_data.join(rshoulder_encoded)
    # encode rshoulder - validation data
    rshoulder_series = validation_data['rshoulder']
    rshoulder_encoded = pd.get_dummies(rshoulder_series, 'rshoulder')
    validation_data = validation_data.drop('rshoulder', axis=1)
    validation_data = validation_data.join(rshoulder_encoded)

    # encode relbow - train data
    relbow_series = train_data['relbow']
    relbow_encoded = pd.get_dummies(relbow_series, 'relbow')
    train_data = train_data.drop('relbow', axis=1)
    train_data = train_data.join(relbow_encoded)
    # encode relbow - validation data
    relbow_series = validation_data['relbow']
    relbow_encoded = pd.get_dummies(relbow_series, 'relbow')
    validation_data = validation_data.drop('relbow', axis=1)
    validation_data = validation_data.join(relbow_encoded)

    # encode rwrist - train data
    rwrist_series = train_data['rwrist']
    rwrist_encoded = pd.get_dummies(rwrist_series, 'rwrist')
    train_data = train_data.drop('rwrist', axis=1)
    train_data = train_data.join(rwrist_encoded)
    # encode rwrist - validation data
    rwrist_series = validation_data['rwrist']
    rwrist_encoded = pd.get_dummies(rwrist_series, 'rwrist')
    validation_data = validation_data.drop('rwrist', axis=1)
    validation_data = validation_data.join(rwrist_encoded)

    # encode lshoulder - train data
    lshoulder_series = train_data['lshoulder']
    lshoulder_encoded = pd.get_dummies(lshoulder_series, 'lshoulder')
    train_data = train_data.drop('lshoulder', axis=1)
    train_data = train_data.join(lshoulder_encoded)
    # encode lshoulder - validation data
    lshoulder_series = validation_data['lshoulder']
    lshoulder_encoded = pd.get_dummies(lshoulder_series, 'lshoulder')
    validation_data = validation_data.drop('lshoulder', axis=1)
    validation_data = validation_data.join(lshoulder_encoded)

    # encode lelbow - train data
    lelbow_series = train_data['lelbow']
    lelbow_encoded = pd.get_dummies(lelbow_series, 'lelbow')
    train_data = train_data.drop('lelbow', axis=1)
    train_data = train_data.join(lelbow_encoded)
    # encode lelbow - validation data
    lelbow_series = validation_data['lelbow']
    lelbow_encoded = pd.get_dummies(lelbow_series, 'lelbow')
    validation_data = validation_data.drop('lelbow', axis=1)
    validation_data = validation_data.join(lelbow_encoded)

    # encode lwrist - train data
    lwrist_series = train_data['lwrist']
    lelbow_encoded = pd.get_dummies(lwrist_series, 'lwrist')
    train_data = train_data.drop('lwrist', axis=1)
    train_data = train_data.join(lelbow_encoded)
    # encode lwrist - validation data
    lwrist_series = validation_data['lwrist']
    lelbow_encoded = pd.get_dummies(lwrist_series, 'lwrist')
    validation_data = validation_data.drop('lwrist', axis=1)
    validation_data = validation_data.join(lelbow_encoded)

    # encode midhip - train data
    midhip_series = train_data['midhip']
    midhip_encoded = pd.get_dummies(midhip_series, 'midhip')
    train_data = train_data.drop('midhip', axis=1)
    train_data = train_data.join(midhip_encoded)
    # encode midhip - validation data
    midhip_series = validation_data['midhip']
    midhip_encoded = pd.get_dummies(midhip_series, 'midhip')
    validation_data = validation_data.drop('midhip', axis=1)
    validation_data = validation_data.join(midhip_encoded)

    # encode rhip - train data
    rhip_series = train_data['rhip']
    rhip_encoded = pd.get_dummies(rhip_series, 'rhip')
    train_data = train_data.drop('rhip', axis=1)
    train_data = train_data.join(rhip_encoded)
    # encode rhip - validation data
    rhip_series = validation_data['rhip']
    rhip_encoded = pd.get_dummies(rhip_series, 'rhip')
    validation_data = validation_data.drop('rhip', axis=1)
    validation_data = validation_data.join(rhip_encoded)

    # encode rknee - train data
    rknee_series = train_data['rknee']
    rhip_encoded = pd.get_dummies(rknee_series, 'rknee')
    train_data = train_data.drop('rknee', axis=1)
    train_data = train_data.join(rhip_encoded)
    # encode rknee - validation data
    rknee_series = validation_data['rknee']
    rhip_encoded = pd.get_dummies(rknee_series, 'rknee')
    validation_data = validation_data.drop('rknee', axis=1)
    validation_data = validation_data.join(rhip_encoded)

    # encode rankle - train data
    rankle_series = train_data['rankle']
    rankle_encoded = pd.get_dummies(rankle_series, 'rankle')
    train_data = train_data.drop('rankle', axis=1)
    train_data = train_data.join(rankle_encoded)
    # encode rankle - validation data
    rankle_series = validation_data['rankle']
    rankle_encoded = pd.get_dummies(rankle_series, 'rankle')
    validation_data = validation_data.drop('rankle', axis=1)
    validation_data = validation_data.join(rankle_encoded)

    # encode lhip - train data
    lhip_series = train_data['lhip']
    lhip_encoded = pd.get_dummies(lhip_series, 'lhip')
    train_data = train_data.drop('lhip', axis=1)
    train_data = train_data.join(lhip_encoded)
    # encode lhip - validation data
    lhip_series = validation_data['lhip']
    lhip_encoded = pd.get_dummies(lhip_series, 'lhip')
    validation_data = validation_data.drop('lhip', axis=1)
    validation_data = validation_data.join(lhip_encoded)

    # encode lknee - train data
    lknee_series = train_data['lknee']
    lknee_encoded = pd.get_dummies(lknee_series, 'lknee')
    train_data = train_data.drop('lknee', axis=1)
    train_data = train_data.join(lknee_encoded)
    # encode lknee - validation data
    lknee_series = validation_data['lknee']
    lknee_encoded = pd.get_dummies(lknee_series, 'lknee')
    validation_data = validation_data.drop('lknee', axis=1)
    validation_data = validation_data.join(lknee_encoded)

    # encode lankle - train data
    lankle_series = train_data['lankle']
    lankle_encoded = pd.get_dummies(lankle_series, 'lankle')
    train_data = train_data.drop('lankle', axis=1)
    train_data = train_data.join(lankle_encoded)
    # encode lankle - validation data
    lankle_series = validation_data['lankle']
    lankle_encoded = pd.get_dummies(lankle_series, 'lankle')
    validation_data = validation_data.drop('lankle', axis=1)
    validation_data = validation_data.join(lankle_encoded)

    # encode reye - train data
    reye_series = train_data['reye']
    reye_encoded = pd.get_dummies(reye_series, 'reye')
    train_data = train_data.drop('reye', axis=1)
    train_data = train_data.join(reye_encoded)
    # encode reye - validation data
    reye_series = validation_data['reye']
    reye_encoded = pd.get_dummies(reye_series, 'reye')
    validation_data = validation_data.drop('reye', axis=1)
    validation_data = validation_data.join(reye_encoded)

    # encode leye - train data
    leye_series = train_data['leye']
    leye_encoded = pd.get_dummies(leye_series, 'leye')
    train_data = train_data.drop('leye', axis=1)
    train_data = train_data.join(leye_encoded)
    # encode leye - validation data
    leye_series = validation_data['leye']
    leye_encoded = pd.get_dummies(leye_series, 'leye')
    validation_data = validation_data.drop('leye', axis=1)
    validation_data = validation_data.join(leye_encoded)

    # encode rear - train data
    rear_series = train_data['rear']
    rear_encoded = pd.get_dummies(rear_series, 'rear')
    train_data = train_data.drop('rear', axis=1)
    train_data = train_data.join(rear_encoded)
    # encode rear - validation data
    rear_series = validation_data['rear']
    rear_encoded = pd.get_dummies(rear_series, 'rear')
    validation_data = validation_data.drop('rear', axis=1)
    validation_data = validation_data.join(rear_encoded)


# determine data rows
    X_train = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_train = train_data.iloc[:, 0].values  # predict position

    X_valid = validation_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    y_valid = validation_data.iloc[:, 0].values  # predict position

    return X_train, y_train, X_valid, y_valid, train_data, validation_data
