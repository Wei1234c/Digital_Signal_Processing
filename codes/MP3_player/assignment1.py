import numpy as np


def weighted(x):
    N = len(x)
    n = np.arange(N)
    w = (1 - np.cos(2 * np.pi * n / (N - 1)))
    w = w / np.dot(w, w)
    return x * w


def dft(samples):
    samples = np.asarray(samples).reshape((-1, 1))
    N = len(samples)
    k = n = np.arange(N)
    W = np.exp(np.outer(-1j * np.pi * 2 / N * k, n))
    spectrum = np.dot(W, samples).ravel()
    return spectrum


def get_db(x):
    db = 20 * np.log10(x)
    db[np.where(x == 0)[0]] = -100
    return db


def scaled_fft_db(x, targeted_db = 96):
    # x = weighted(x)
    spectrum = abs(dft(x)) / len(x)
    spectrum = get_db(spectrum)
    spectrum = spectrum + targeted_db - np.max(spectrum)
    return spectrum[:257]
