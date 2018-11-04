from waves.tools.dsp import *



def prototype_filter_remez():
    """ ASSIGNMENT 2

        Compute the prototype filter used in subband coding. The filter
        is a 512-point lowpass FIR h[n] with bandwidth pi/64 and stopband
        starting at pi/32

        You should use the remez routine (signal.remez()). See
        http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.remez.html
    """

    from scipy import signal

    M = 512
    Fs = 44100
    F_nyquist = Fs // 2

    Fpass = F_nyquist * (1 / 128)
    Fstop = F_nyquist * (1 / 32)
    bpass = signal.remez(numtaps = M,
                         bands = [0, Fpass, Fstop, F_nyquist],
                         desired = [2, 0], Hz = Fs)

    return bpass



def prototype_filter2():
    """ ASSIGNMENT 2

        Compute the prototype filter used in subband coding. The filter
        is a 512-point lowpass FIR h[n] with bandwidth pi/64 and stopband
        starting at pi/32

        You should use the remez routine (signal.remez()). See
        http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.remez.html
    """

    N = 512
    w = dsp.get_freq_bins(N)

    H = np.zeros_like(w)
    H[abs(w) <= np.pi / 128] = 2

    fourier.plot = False
    h = fourier.idtft(H, n_samples = N, plt_abs = False)

    return h



prototype_filter = prototype_filter_remez
# prototype_filter = prototype_filter2
