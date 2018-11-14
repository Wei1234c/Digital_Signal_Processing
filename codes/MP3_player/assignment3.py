from assignment2 import *
from waves.sound.tools.music import *



def subband_filtering(x, h):
    """ ASSIGNMENT 3

        Write a routine to implement the efficient version of the subband filter
        as specified by the MP3 standard

        Arguments:
        x:  a new 512-point data buffer, in time-reversed order [x[n],x[n-1],...,x[n-511]].
        h:  The prototype filter of the filter bank you found in the previous assignment

        Returns:
        s: 32 new output samples
    """

    # h = prototype_filter()
    # r = x * h
    #
    # bands_idx = np.arange(32)
    # q = np.arange(64)
    # p = np.arange(8)
    # c = np.zeros_like(q)
    #
    # for qi in q:
    #     cqi = [(-1) ** pi * r[qi + 64 * pi] for pi in p]
    #     c[qi] = np.sum(cqi)
    #
    # s = []
    # for band in bands_idx:
    #     s.append([np.cos(np.pi / 64 * (2 * band + 1) * (qi - 16)) * c[qi] for qi in q])
    #
    # s = np.vstack(s)
    #
    # # BR = np.fft.fft(s, axis = -1)[:, :257]
    # # plt.plot(abs(BR.T))
    # # plt.show()
    # #
    #
    # s = s**2
    # s = s.sum(axis = 1)
    #
    # plt.plot(s)
    # plt.show()
    # return s

    # 產生 cosine bank
    N = len(x)
    bands_idx = np.arange(32)
    offsets = (bands_idx * 2 + 1).reshape((-1, 1))
    n = np.arange(N) - 16
    freq = np.pi / 64
    cosine_bank = np.cos(offsets * n * freq)

    # 產生 subband filters
    h = prototype_filter()
    subband_filters = cosine_bank * h

    # 測試 subband filters
    # x = np.zeros_like(x)
    # x[0] = 1
    band_responses = signal.lfilter(x, 1, subband_filters, axis = -1)
    # band_responses = np.vstack([np.convolve(x, subband_filter) for subband_filter in subband_filters])

    # plot 測試 subband filters 的結果
    BR = np.fft.fft(band_responses, axis = -1)[:, :257]
    plt.plot(abs(BR.T))
    plt.show()

    # band_responses = band_responses**2
    # band_responses = band_responses[::32]
    band_responses = np.sum(band_responses, axis = -1)
    return band_responses
