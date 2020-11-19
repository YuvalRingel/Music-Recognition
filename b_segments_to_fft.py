import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# tdl
# figure out fft_to_freqs
# understand fft alg
# get better formula for scaling

def get_freqs(datas_list, samplerate):
    freq_list = []
    for data in datas_list:
        data = denoise(data)
        new_batch = analyze_fft(data, samplerate)
        freq_list.append(new_batch)
    return freq_list


def denoise(data):
    # windowing
    return data


def analyze_fft(data, samplerate):
    len_data = len(data)

    #### ??? ####
    channel_1 = np.zeros(2 ** (int(np.ceil(np.log2(len_data)))))
    channel_1[0:len_data] = data
    #############

    fourier = np.fft.fft(channel_1)
    x = np.linspace(0, 44000, len(fourier))

    # First half is the real component, second half is imaginary
    fourier_to_plot = fourier[0:len(fourier) // 2]
    # x = x[0:len(fourier) // 2]
    fourier = np.abs(fourier)
    fourier_to_plot = fourier[0:20000]
    x = x[0:20000]
    #### plotting
    # plt.figure(1)
    # plt.plot(x, fourier_to_plot)
    # plt.xlabel('frequency')
    # plt.ylabel('amplitude')
    # plt.show()
    #####

    limit = 6
    return fft_to_freqs(fourier_to_plot, x, samplerate, limit)


def fft_to_freqs(fft, x, samplerate, limit=0):
    max_p = np.argmax(fft)
    peaks, values = find_peaks(fft,
                               height=fft[max_p] // 8,
                               prominence=fft[max_p] // 64,  # figure out correct formula. and only 6 highest
                               width=1)
    peaks = peaks * x[-1] // len(fft)
    heights = values.get('peak_heights')
    if limit:
        limit_peaks = get_limit_peaks(peaks, heights, limit)
    else:
        limit_peaks = peaks
    #scaled_max_p = [peak for peak in limit_peaks]  ##figure out more accurate formula
    ############
    # filter the recieved freqs to get the right ones
    ############
    ### plotting ###
    # plt.plot(x, fft)
    # # test = np.ndarray.astype(limit_peaks,int)
    # plt.plot(limit_peaks, fft[limit_peaks], "x")
    # plt.show()
    ################
    return limit_peaks


def get_limit_peaks(peaks, heights, limit):
    if len(peaks) > limit:
        peaks_dict = {}
        for i in range(len(peaks)):
            peaks_dict[peaks[i]] = heights[i]
        sorted_peaks = sorted(peaks_dict, key=lambda x: peaks_dict[x], reverse=True)
        peaks = sorted_peaks[:limit]
    return peaks
