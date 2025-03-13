# -------------------------------------------------------------------------------
# Name:        run_batch_pyora
# Purpose:     use multiprocessing to run Fortran Ecosse
# Author:      Mike Martin, based on module written by Mark Richards
# Created:     4 August 2017
# Description:  standard script for use in Global Ecosse
# -------------------------------------------------------------------------------
#
__author__ = 'so3mm5'
__prog__ = 'run_batch_pyora'
__version__ = '0.0'

from argparse import ArgumentParser
from datetime import datetime
from json import load as json_load
import math
from os.path import abspath, expanduser, expandvars, normpath, join, isfile, split, isdir
from os import getcwd, walk, chdir

from subprocess import Popen, PIPE, STDOUT
from sys import stdout, exit
from time import time, sleep
from multiprocessing import cpu_count

from socket import socket, AF_INET, SOCK_STREAM, gethostname
from copy import copy, deepcopy

from set_up_logging import set_up_logging
from initialise_pyorator import read_config_file, initiation, write_config_file

sleepTime = 5
WARN_STR = '*** Warning *** '
PROGRAM_ID = 'spec_run'
ERROR_STR = '*** Error *** '

class RunSites(object):
    """
    C
    """
    def __init__(self, parent=None):
        initiation(self)

def main():
    """
    Entry point
    """
    sim = RunSites()  # instantiate form
    # sim.run_ecosse()

if __name__ == '__main__':
    main()

