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
    # fft functions and send it to get_freq
    # data = data[0:len(data)] #####dafuq?
    len_data = len(data)

    #### ??? ####
    channel_1 = np.zeros(2 ** (int(np.ceil(np.log2(len_data)))))
    channel_1[0:len_data] = data
    #############

    fourier = np.fft.fft(channel_1)
    x = np.linspace(0, 44000, len(fourier))

    # First half is the real component, second half is imaginary
    # fourier_to_plot = fourier[0:len(fourier) // 2]
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

    return fft_to_freqs(True, fourier_to_plot, x, samplerate)


def fft_to_freqs(six, fft, x, samplerate):
    max_p = np.argmax(fft)
    peaks, values = find_peaks(fft,
                               height=fft[max_p] // 16,
                               prominence=fft[max_p] // 32)  # figure out correct formula. and only 6 highest
    # width=5)
    heights = values.get('peak_heights')
    if six:
        six_peaks = get_six_peaks(peaks, heights)
    else:
        six_peaks = peaks
    scaled_max_p = [peak * (0.17) for peak in six_peaks]  ##figure out more accurate formula
    ############
    # filter the recieved freqs to get the right ones
    ############
    ### plotting ###
    # plt.plot(x, fft)
    # plt.plot(scaled_max_p, fft[six_peaks], "x")
    # plt.show()
    ################
    return scaled_max_p


def get_six_peaks(peaks, heights):
    if len(peaks) > 6:
        peaks_dict = {}
        for i in range(len(peaks)):
            peaks_dict[peaks[i]] = heights[i]
        sorted_peaks = sorted(peaks_dict, key=lambda x: peaks_dict[x], reverse=True)
        peaks = sorted_peaks[:6]
    return peaks
