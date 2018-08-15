import os

import pandas as pd

import math

cols = ['Position', 'SpineBaseX', 'SpineBaseY', 'SpineBaseZ', 'SpineMidX', 'SpineMidY', 'SpineMidZ', 'NeckX', 'NeckY',
        'NeckZ', 'HeadX', 'HeadY', 'HeadZ', 'ShoulderLeftX', 'ShoulderLeftY', 'ShoulderLeftZ', 'ElbowLeftX',
        'ElbowLeftY', 'ElbowLeftZ', 'WristLeftX', 'WristLeftY', 'WristLeftZ', 'HandLeftX', 'HandLeftY', 'HandLeftZ',
        'ShoulderRightX', 'ShoulderRightY', 'ShoulderRightZ', 'ElbowRightX', 'ElbowRightY', 'ElbowRightZ',
        'WristRightX', 'WristRightY', 'WristRightZ', 'HandRightX', 'HandRightY', 'HandRightZ', 'HipLeftX', 'HipLeftY',
        'HipLeftZ', 'KneeLeftX', 'KneeLeftY', 'KneeLeftZ', 'AnkleLeftX', 'AnkleLeftY', 'AnkleLeftZ', 'FootLeftX',
        'FootLeftY', 'FootLeftZ', 'HipRightX', 'HipRightY', 'HipRightZ', 'KneeRightX', 'KneeRightY', 'KneeRightZ',
        'AnkleRightX', 'AnkleRightY', 'AnkleRightZ', 'FootRightX', 'FootRightY', 'FootRightZ', 'SpineShoulderX',
        'SpineShoulderY', 'SpineShoulderZ', 'HandTipLeftX', 'HandTipLeftY', 'HandTipLeftZ', 'ThumbLeftX', 'ThumbLeftY',
        'ThumbLeftZ', 'HandTipRightX', 'HandTipRightY', 'HandTipRightZ', 'ThumbRightX', 'ThumbRightY', 'ThumbRightZ']

folder = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir + os.sep
                          + os.pardir + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)
csv_dir = os.path.normpath(folder + '/Datasets/kinect_training.csv')


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


def get_data(columns=cols,
             data_dir=csv_dir):

    train_data = pd.read_csv(data_dir, usecols=columns)

    if "Position" in columns:
        # # encode Position - train data
        encode_var(train_data, "Position")

    if "SpineBaseX" in columns and "SpineBaseY" in columns and "SpineBaseZ" in columns:
        # encode SpineBase - train data
        train_data.SpineBaseX = clean_up_data(train_data.SpineBaseX)
        train_data.SpineBaseY = clean_up_data(train_data.SpineBaseY)
        train_data.SpineBaseZ = clean_up_data(train_data.SpineBaseZ)

    if "SpineMidX" in columns and "SpineMidY" in columns and "SpineMidZ" in columns:
        # encode SpineMid - train data
        train_data.SpineMidX = clean_up_data(train_data.SpineMidX)
        train_data.SpineMidY = clean_up_data(train_data.SpineMidY)
        train_data.SpineMidZ = clean_up_data(train_data.SpineMidZ)

    if "NeckX" in columns and "NeckY" in columns and "NeckZ" in columns:
        # encode Neck - train data
        train_data.NeckX = clean_up_data(train_data.NeckX)
        train_data.NeckY = clean_up_data(train_data.NeckY)
        train_data.NeckZ = clean_up_data(train_data.NeckZ)

    if "HeadX" in columns and "HeadY" in columns and "HeadZ" in columns:
        # encode Head - train data
        train_data.HeadX = clean_up_data(train_data.HeadX)
        train_data.HeadY = clean_up_data(train_data.HeadY)
        train_data.HeadZ = clean_up_data(train_data.HeadZ)

    if "ShoulderLeftX" in columns and "ShoulderLeftY" in columns and "ShoulderLeftZ" in columns:
        # encode ShoulderLeft - train data
        train_data.ShoulderLeftX = clean_up_data(train_data.ShoulderLeftX)
        train_data.ShoulderLeftY = clean_up_data(train_data.ShoulderLeftY)
        train_data.ShoulderLeftZ = clean_up_data(train_data.ShoulderLeftZ)

    if "ElbowLeftX" in columns and "ElbowLeftY" in columns and "ElbowLeftZ" in columns:
        # encode ElbowLeft - train data
        train_data.ElbowLeftX = clean_up_data(train_data.ElbowLeftX)
        train_data.ElbowLeftY = clean_up_data(train_data.ElbowLeftY)
        train_data.ElbowLeftZ = clean_up_data(train_data.ElbowLeftZ)

    if "WristLeftX" in columns and "WristLeftY" in columns and "WristLeftZ" in columns:
        # encode WristLeft - train data
        train_data.WristLeftX = clean_up_data(train_data.WristLeftX)
        train_data.WristLeftY = clean_up_data(train_data.WristLeftY)
        train_data.WristLeftZ = clean_up_data(train_data.WristLeftZ)

    if "HandLeftX" in columns and "HandLeftY" in columns and "HandLeftZ" in columns:
        # encode HandLeft - train data
        train_data.HandLeftX = clean_up_data(train_data.HandLeftX)
        train_data.HandLeftY = clean_up_data(train_data.HandLeftY)
        train_data.HandLeftZ = clean_up_data(train_data.HandLeftZ)

    if "ShoulderRightX" in columns and "ShoulderRightY" in columns and "ShoulderRightZ" in columns:
        # encode ShoulderRight - train data
        train_data.ShoulderRightX = clean_up_data(train_data.ShoulderRightX)
        train_data.ShoulderRightY = clean_up_data(train_data.ShoulderRightY)
        train_data.ShoulderRightZ = clean_up_data(train_data.ShoulderRightZ)

    if "ElbowRightX" in columns and "ElbowRightY" in columns and "ElbowRightZ" in columns:
        # encode ElbowRight - train data
        train_data.ElbowRightX = clean_up_data(train_data.ElbowRightX)
        train_data.ElbowRightY = clean_up_data(train_data.ElbowRightY)
        train_data.ElbowRightZ = clean_up_data(train_data.ElbowRightZ)

    if "WristRightX" in columns and "WristRightY" in columns and "WristRightZ" in columns:
        # encode WristRight - train data
        train_data.WristRightX = clean_up_data(train_data.WristRightX)
        train_data.WristRightY = clean_up_data(train_data.WristRightY)
        train_data.WristRightZ = clean_up_data(train_data.WristRightZ)

    if "HandRightX" in columns and "HandRightY" in columns and "HandRightZ" in columns:
        # encode HandRight - train data
        train_data.HandRightX = clean_up_data(train_data.HandRightX)
        train_data.HandRightY = clean_up_data(train_data.HandRightY)
        train_data.HandRightZ = clean_up_data(train_data.HandRightZ)

    if "HipLeftX" in columns and "HipLeftY" in columns and "HipLeftZ" in columns:
        # encode HipLeft - train data
        train_data.HipLeftX = clean_up_data(train_data.HipLeftX)
        train_data.HipLeftY = clean_up_data(train_data.HipLeftY)
        train_data.HipLeftZ = clean_up_data(train_data.HipLeftZ)

    if "KneeLeftX" in columns and "KneeLeftY" in columns and "KneeLeftZ" in columns:
        # encode KneeLeft - train data
        train_data.KneeLeftX = clean_up_data(train_data.KneeLeftX)
        train_data.KneeLeftY = clean_up_data(train_data.KneeLeftY)
        train_data.KneeLeftZ = clean_up_data(train_data.KneeLeftZ)

    if "AnkleLeftX" in columns and "AnkleLeftY" in columns and "AnkleLeftZ" in columns:
        # encode AnkleLeft - train data
        train_data.AnkleLeftX = clean_up_data(train_data.AnkleLeftX)
        train_data.AnkleLeftY = clean_up_data(train_data.AnkleLeftY)
        train_data.AnkleLeftZ = clean_up_data(train_data.AnkleLeftZ)

    if "FootLeftX" in columns and "FootLeftY" in columns and "FootLeftZ" in columns:
        # encode FootLeft - train data
        train_data.FootLeftX = clean_up_data(train_data.FootLeftX)
        train_data.FootLeftY = clean_up_data(train_data.FootLeftY)
        train_data.FootLeftZ = clean_up_data(train_data.FootLeftZ)

    if "HipRightX" in columns and "HipRightY" in columns and "HipRightZ" in columns:
        # encode HipRight - train data
        train_data.HipRightX = clean_up_data(train_data.HipRightX)
        train_data.HipRightY = clean_up_data(train_data.HipRightY)
        train_data.HipRightZ = clean_up_data(train_data.HipRightZ)

    if "KneeRightX" in columns and "KneeRightY" in columns and "KneeRightZ" in columns:
        # encode KneeRight - train data
        train_data.KneeRightX = clean_up_data(train_data.KneeRightX)
        train_data.KneeRightY = clean_up_data(train_data.KneeRightY)
        train_data.KneeRightZ = clean_up_data(train_data.KneeRightZ)

    if "AnkleRightX" in columns and "AnkleRightY" in columns and "AnkleRightZ" in columns:
        # encode AnkleRight - train data
        train_data.AnkleRightX = clean_up_data(train_data.AnkleRightX)
        train_data.AnkleRightY = clean_up_data(train_data.AnkleRightY)
        train_data.AnkleRightZ = clean_up_data(train_data.AnkleRightZ)

    if "FootRightX" in columns and "FootRightY" in columns and "FootRightZ" in columns:
        # encode FootRight - train data
        train_data.FootRightX = clean_up_data(train_data.FootRightX)
        train_data.FootRightY = clean_up_data(train_data.FootRightY)
        train_data.FootRightZ = clean_up_data(train_data.FootRightZ)

    if "SpineShoulderX" in columns and "SpineShoulderY" in columns and "SpineShoulderZ" in columns:
        # encode SpineShoulder - train data
        train_data.SpineShoulderX = clean_up_data(train_data.SpineShoulderX)
        train_data.SpineShoulderY = clean_up_data(train_data.SpineShoulderY)
        train_data.SpineShoulderZ = clean_up_data(train_data.SpineShoulderZ)

    if "HandTipLeftX" in columns and "HandTipLeftY" in columns and "HandTipLeftZ" in columns:
        # encode HandTipLeft - train data
        train_data.HandTipLeftX = clean_up_data(train_data.HandTipLeftX)
        train_data.HandTipLeftY = clean_up_data(train_data.HandTipLeftY)
        train_data.HandTipLeftZ = clean_up_data(train_data.HandTipLeftZ)

    if "ThumbLeftX" in columns and "ThumbLeftY" in columns and "ThumbLeftZ" in columns:
        # encode ThumbLeft - train data
        train_data.ThumbLeftX = clean_up_data(train_data.ThumbLeftX)
        train_data.ThumbLeftY = clean_up_data(train_data.ThumbLeftY)
        train_data.ThumbLeftZ = clean_up_data(train_data.ThumbLeftZ)

    if "HandTipRightX" in columns and "HandTipRightY" in columns and "HandTipRightZ" in columns:
        # encode HandTipRight - train data
        train_data.HandTipRightX = clean_up_data(train_data.HandTipRightX)
        train_data.HandTipRightY = clean_up_data(train_data.HandTipRightY)
        train_data.HandTipRightZ = clean_up_data(train_data.HandTipRightZ)

    if "ThumbRightX" in columns and "ThumbRightY" in columns and "ThumbRightZ" in columns:
        # encode ThumbRight - train data
        train_data.ThumbRightX = clean_up_data(train_data.ThumbRightX)
        train_data.ThumbRightY = clean_up_data(train_data.ThumbRightY)
        train_data.ThumbRightZ = clean_up_data(train_data.ThumbRightZ)

    # determine data rows
    data = train_data.iloc[:, 1:len(train_data.columns)].values  # drop position
    labels = train_data.iloc[:, 0].values  # predict position

    return data, labels
