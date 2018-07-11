#This method is used to clean up data during the video classification process
def clean_data(human_array):
    #neck
    if human_array[3] == 0.0 or human_array[4] == 0.0:
        return None
    #midhip, rhip, lhip
    elif (human_array[17] == 0.0 or human_array[18] == 0.0) and (human_array[19] == 0.0 or human_array[20] == 0.0) and (human_array[25] == 0.0 or human_array[26] == 0.0):
        return None
    elif (human_array[21] == 0.0 or human_array[22] == 0.0) and (human_array[27] == 0.0 or human_array[28] == 0.0):
        return None
    else:
        return human_array

#This method is used to clean up data during the feature extraction process
def clean_string_data(human_string):

    human_array = human_string.split(',')
    #neck
    if human_array[3] == '0.0' or human_array[4] == '0.0':
        return None
    #midhip, rhip, lhip
    elif (human_array[17] == '0.0' or human_array[18] == '0.0') and (human_array[19] == '0.0' or human_array[20] == '0.0') and (human_array[25] == '0.0' or human_array[26] == '0.0'):
        return None
    #left or right knee
    elif (human_array[21] == '0.0' or human_array[22] == '0.0') and (human_array[27] == '0.0' or human_array[28] == '0.0'):
        return None
    else:
        return human_string
