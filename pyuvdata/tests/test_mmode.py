"""
Tests for mmode transfer matrix translation
"""

testdir = os.path.join(DATA_PATH, 'mmode_test_data/')
import nose.tools as nt
import os
from pyuvdata import UVData
import pyuvdata.utils as uvutils
import pyuvdata.tests as uvtest
from pyuvdata.data import DATA_PATH
import numpy as np
from pyuvdata.mmode import UVDataDrift
from pyuvsim import AnalyticBeam

def test_write_transfer_matrices():
    '''
    test computing a transit telescope
    from analytic beam simulation
    and writing transfer matrix
    '''
    uv_uniform = UVData()
    uv_uniform.read_uvfits(os.path.join(testdir,'two_antennas_equator_uniform.uvfits'))
    uv_beams_uniform = [ AnalyticBeam('uniform'), AnalyticBeam('uniform') ]
    uv_drift_uniform = UVDataDrift()
    uv_drift_uniform.set_beams(uv_beams_uniform)
    uv_drift_uniform.set_uv(uv_uniform)
