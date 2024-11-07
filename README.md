# Extinction map in M31
An extinction distribution of the Andromeda Galaxy (M31) is constructed with member stars identified by Ren at al. (2021a) as tracers by fitting multiband photometric data from UKIRT/WFCAM, PS1, and Gaia DR3.
The resulting extinction distribution covers approximately 10 deg$^2$ of M31 with a resolution of approximately 50 arcsec, providing the largest coverage to date based on stellar observations.
The derived average extinction, $A_V = 0.96$ mag, agrees well with previous studies. 
To account for foreground extinction, an extinction map of the Milky Way toward M31 with a resolution of $\sim$ 1.7 arcmin is also constructed, yielding an average extinction of $A_V \approx 0.19$ mag. 
The results offer a valuable tool for extinction correction in future observations, such as those from the China Space Station Telescope, and provide insights for improving dust models based on the spatial distribution of dust in galaxies like M31.

# Data access
The extinction map in M31 can be accessed at: https://nadc.china-vo.org/res/file_upload/download?id=47823  
The foreground extinction map toward M31 can be accessed at: https://nadc.china-vo.org/res/file_upload/download?id=47822

# How to use the maps
To use our maps, we have provided a python procedure 'Wang2024_map.py'. The procedure relies on the dustmaps package (https://github.com/gregreen/dustmaps).

The following steps show how to install our procedure:  
1. Install the dustmaps package (pip install dustmaps).  
2. Download the procedure 'Wang2024_map.py' in this project and run it.  
3. Download the extinction map and the foreground extinction map to the same directory.

An example is given below to show how to obtain E(B-V) values from our dust maps:

    >>> from Wang2024_map import M31_extinction, M31_fgd_extinction
    >>> ra, dec = 10.8, 41.375 # Example coordinates (RA, Dec)
    >>> av_value = M31_extinction(ra, dec)
    >>> print(f"Extinction at RA={ra}, Dec={dec}: Av={av_value}")
    >>> av_value = M31_fgd_extinction(ra, dec)
    >>> print(f"Foreground Extinction at RA={ra}, Dec={dec}: Av={av_value}")

If you have any questions or need more informations, please send emall to Yuxi Wang (yuxiwang@qlnu.edu.cn) and Yi Ren (yiren@qlnu.edu.cn).
