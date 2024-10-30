#%%
from dustmaps.config import config
import healpy as hp
from astropy.coordinates import SkyCoord
import numpy as np
import os
import shutil

#%%

# Load the M31 data and ensure it's available in the dustmaps data directory
def load_M31_dustmap():
    data_dir = config['data_dir']   
    filepath = os.path.join(data_dir, 'revise0_m31_dustmap.fits')  

    # Check if map.fits already exists in the dustmaps directory
    if os.path.exists(filepath):
        print(f"{filepath} already exists. Skipping copy.")
    else:
        local_map_path = './revise0_m31_dustmap.fits'   # Ensure map.fits is in 
        os.makedirs(data_dir, exist_ok=True)
        shutil.copy(local_map_path, filepath)
    return hp.read_map(filepath)

# Define a function to query extinction values based on RA and Dec coordinates
def M31_extinction(ra, dec):
    # Load the dustmap data if not already loaded
    map_data = load_M31_dustmap()
    coords = SkyCoord(ra=ra, dec=dec, unit='deg', frame='icrs')
    theta, phi = np.radians(90 - coords.dec.deg), np.radians(coords.ra.deg)
    pix_index = hp.ang2pix(hp.get_nside(map_data), theta, phi)
    return map_data[pix_index]

# Load the M31 foreground data and ensure it's available in the dustmaps data directory
def load_M31_fgd_dustmap():
    data_dir = config['data_dir']
    filepath_fgd = os.path.join(data_dir, 'revise0_m31_fgd_dustmap.fits')
    if os.path.exists(filepath_fgd):
        print(f"{filepath_fgd} already exists. Skipping copy.")
    else:
        local_map_fgd_path = './revise0_m31_fgd_dustmap.fits'
        os.makedirs(data_dir, exist_ok=True)
        shutil.copy(local_map_fgd_path, filepath_fgd)
    return hp.read_map(filepath_fgd)

# Define a function to query extinction values based on RA and Dec coordinates
def M31_fgd_extinction(ra, dec):
    # Load the dustmap data if not already loaded
    map_data = load_M31_fgd_dustmap()
    coords = SkyCoord(ra=ra, dec=dec, unit='deg', frame='icrs')
    theta, phi = np.radians(90 - coords.dec.deg), np.radians(coords.ra.deg)
    pix_index = hp.ang2pix(hp.get_nside(map_data), theta, phi)
    return map_data[pix_index]



# %%
