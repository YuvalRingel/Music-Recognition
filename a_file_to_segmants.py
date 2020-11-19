import numpy as np
import matplotlib.pyplot as plt
from handle_file import *
from b_segments_to_fft import *
from scipy.signal import savgol_filter


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
    data_for_peaks = np.abs(data_1d)
    max_p = np.argmax(data_for_peaks)
    # = savgol_filter(data_1d, window_length = 1351, polyorder = 5)

    # first find big gaps
    peaks1, values = find_peaks(data_for_peaks,
                                prominence=data_for_peaks[max_p] // 16)

    # stating indices of start and end of chunks before big gaps
    gap = find_gap(peaks1, 512)
    indexes = find_chunks(peaks1, gap)

    # step 2: select the highest peaks in each part
    indexes2 = []
    for duo in indexes:
        data_for_peaks2 = data_for_peaks[duo[0]:duo[1]]  # only values from data in the chunk
        max_p = np.argmax(data_for_peaks2)  # highest peak in that chunk
        peaks2, values2 = find_peaks(data_for_peaks2,
                                     prominence=data_for_peaks2[max_p]//4)
        gap = find_gap(peaks2, 128)
        chunk_indexes = find_chunks(peaks2, gap, add=duo[0])
        indexes2 += chunk_indexes
        # plot_chunk(data_for_peaks2, peaks2, chunk_indexes, duo)


    # plotting the whole thing
    plot_all(data_for_peaks, peaks1, indexes, indexes2)


    # making list of all divided data from peaks2
    # make full stops every end of big chunk
    divided_data_list = []
    big_chunks_lists = []
    k = 0
    for i, j in indexes2:
        # if the start of small chunk is bigger the the end of a big chunk, it means there was a change in big chunks
        # the values in big_chunks_list are the last segments in each big chunk
        # after that segment there need to be a full stop
        if k < len(indexes) and i > indexes[k][1]:
            big_chunks_lists.append(len(divided_data_list)-1)
            k += 1
        # adding new segment
        new_segment = data_1d[i:j]
        divided_data_list.append(new_segment)
    return divided_data_list, big_chunks_lists

def find_gap(peaks, div):
    gaps = []
    for i in range(len(peaks) - 1):
        gaps.append(peaks[i + 1] - peaks[i])
    if div == 32:
        print('')
    sorted_gaps = sorted(gaps, reverse=True)
    s = sum(sorted_gaps[:len(sorted_gaps) // div])
    d = (len(sorted_gaps)) // div
    gap = s//d
    return gap

def find_chunks(peaks, gap, add=0):
    indexes = []
    start = peaks[0]
    finish = peaks[-1]
    for i in range(len(peaks) - 1):
        j = i + 1
        if (peaks[j] - peaks[i]) > gap:  # arbitrary
            finish = peaks[i]
            new_index = [start + add, finish + add]
            start = peaks[j]
            indexes.append(new_index)
        if j == (len(peaks) - 1):
            finish = peaks[j]
            new_index = [start + add, finish + add]
            indexes.append(new_index)

    # clean duos with the same values or too small gaps
    i = 0
    while i < len(indexes):
        duo = indexes[i]
        if (duo[1] - duo[0] <= gap):
            indexes.remove(duo)
        else:
            i += 1
    return indexes


def plot_chunk(data, peaks, chunk_indexes, duo):
    # plotting each big chunk for monitoring the loop
    plt.plot(data)
    plt.plot(peaks, data[peaks])
    list1=[]
    for i in chunk_indexes:
        list1.append(i[0]-duo[0])
        list1.append(i[1]-duo[0])
    plt.plot(list1, data[list1], "x")
    plt.show()

def plot_all(data ,peaks, indexes, indexes2):
    # setting for plotting the big gaps
    start_plot = []
    end_plot = []
    for duo in indexes:
        start_plot.append(duo[0])
        end_plot.append(duo[1])

    # setting for plotting the small gaps
    start_plot2 = []
    end_plot2 = []
    for duo in indexes2:
        start_plot2.append(duo[0])
        end_plot2.append(duo[1])

    # plotting the whole thing
    plt.plot(data)  # all the data
    plt.plot(peaks, data[peaks])  # all data from first find_peaks()
    plt.plot(start_plot, data[start_plot], "o")  # start of big chunks
    plt.plot(end_plot, data[end_plot], "o")  # end of big chunks
    plt.plot(start_plot2, data[start_plot2], "x")  # start of small chunks
    plt.plot(end_plot2, data[end_plot2], "x")  # end of small chunks
    plt.show()