from handle_file import *
import numpy as np
import matplotlib.pyplot as plt
from segments_to_fft import *


# tdl
# handle divide data

def get_data(link=False, path=False):
    if path is not False:
        data = load_sound(path)
    elif link is not False:
        data = download_sound(link)
    return data


def divide_data(data, samplerate):
    data_1d = np.delete(data, 1, 1)
    data_1d = data_1d.transpose()
    data_1d = data_1d[0]

    max_p = np.argmax(data_1d)
    peaks, values = find_peaks(data_1d,
                               height=data_1d[max_p] // 16,
                               prominence=data_1d[max_p] // 2,  # figure out correct formula.
                               width=50)
    heights = values.get('peak_heights')

    ### plotting ###
    # plt.plot(data_1d)
    # plt.plot(peaks, data_1d[peaks], "x")
    # plt.show()

    indexes = []
    start = peaks[0]
    finish = peaks[-1]
    for i in range(len(peaks)-1):
        j = i + 1
        #if i == 1098:
        #    print('stop')
        if (peaks[j] - peaks[i]) > 10000:  # arbitrary
            finish = peaks[i]
            new_index = [start, finish]
            start = peaks[j]
            indexes.append(new_index)
        if j == (len(peaks) - 1):
            finish = peaks[j]
            new_index = [start, finish]
            indexes.append(new_index)

    divided_data_list = []
    for i, j in indexes:
        new_segment = data_1d[i:j]
        #print(i, j)
        divided_data_list.append(new_segment)

    # plotting
    div_plot = []
    for duo in indexes:
        div_plot.append(duo[0])
        div_plot.append(duo[1])
    plt.plot(data_1d)
    plt.plot(div_plot, data_1d[div_plot], "x")
    plt.show()


    # smooth the waveform

    return divided_data_list
