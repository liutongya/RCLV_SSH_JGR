import numpy as np

import xmitgcm 
from IPython.display import display, clear_output
import time

import os
import xarray as xr
import floater

import csv
import pandas as pd
from floater.generators import FloatSet

from floater import generators
from floater import utils

import sys
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integer', type=int, help='display an integer')
args = parser.parse_args()

print(args.integer)
mon = args.integer

dir_in = '/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/RCLV/flt_2d/' + str(mon+1).zfill(3) + '/'
dir_out = '/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/RCLV/output/flt_2d/' + str(mon+1).zfill(3) + '/'

utils.floats_to_netcdf(input_dir=dir_in,
                       output_fname='float_trajectories',
                       float_file_prefix='float_trajectories',
                       output_dir=dir_out,
                       output_prefix='float_trajectories',
                       pkl_path='/rigel/ocp/users/tl2913/floater/floatset_80_2d.pkl')
