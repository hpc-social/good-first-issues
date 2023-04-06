---
tags: ,enhancement
title: "Preprocessing for EZStat format"
html_url: "https://github.com/ECSHackWeek/impedance.py/issues/172"
user: xraymancs
repo: ECSHackWeek/impedance.py
---

Would it be possible to add a read routine for the EZStat file format which has frequency, |Z|, phase, Re{Z} and -Im{Z} as its 5 columns with a header line.  The specific EZStat code would be as follows:

def readEZStat(filename):
    """ function for reading EZStat csv files
    Parameters
    ----------
    filename: string
        Filename of .csv file to extract impedance data from
    Returns
    -------
    frequencies : np.ndarray
        Array of frequencies
    impedance : np.ndarray of complex numbers
        Array of complex impedances
    """
    data = np.genfromtxt(filename, delimiter=',')

    f = data[1:, 0]
    Z = data[1:, 3] - 1j*data[1:, 4]

    return f, Z
