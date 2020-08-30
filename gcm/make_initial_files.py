import numpy as np
from matplotlib import pyplot as plt
import xarray as xr
from xmitgcm import open_mdsdataset
import sys
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integer', type=int, help='display an integer')
args = parser.parse_args()

print(args.integer)
mon = args.integer

def write_field(fname, data):
    print('wrote to file: ' + fname)
    fid = open(fname, "wb")
    data.tofile(fid)
    fid.close()

#step = int(mon * 2880)
#print(step)
monfn = '/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/RCLV/flt_2d/' + str(mon).zfill(3) + '/'
#tmpfn = '/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/floater_eddy/floater_3d/layer_1/tmpfile/'

#read data
ds = open_mdsdataset(monfn, iters=8640, prefix={'T','U','V','Eta'}).chunk()
#print(ds)

temp = ds['T'][0,:,:,:].load().data
temp = temp.astype('>f8')

uu = ds['U'][0,:,:,:].load().data
uu = uu.astype('>f8')

vv = ds['V'][0,:,:,:].load().data
vv = vv.astype('>f8')

hh = ds['Eta'][0,:,:].load().data
hh = hh.astype('>f8')

#output
savefile = '/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/RCLV/flt_2d/tmpfile/'

out_filename_h = savefile + 'ssh_floater.bin'
write_field(out_filename_h, hh)

out_filename_temp = savefile + 'temp_floater.bin'
write_field(out_filename_temp, temp)

out_filename_u = savefile + 'u_floater.bin'
write_field(out_filename_u, uu)

out_filename_v = savefile + 'v_floater.bin'
write_field(out_filename_v, vv)

print('initial files generated')

