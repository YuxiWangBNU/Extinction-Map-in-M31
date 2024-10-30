#%%
from Wang2024_map import M31_extinction, M31_fgd_extinction

# Example coordinates (RA, Dec)
ra, dec = 10.8, 41.375 
av_value = M31_extinction(ra, dec)
print(f"Extinction at RA={ra}, Dec={dec}: Av={av_value}")
#%%
ra, dec = 10.8, 41.375
av_value = M31_fgd_extinction(ra, dec)
print(f"Extinction at RA={ra}, Dec={dec}: Av={av_value}")
# %%
