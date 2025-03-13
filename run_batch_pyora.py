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

from initialise_pyorator_batch import read_config_file, initiation

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
        pass

def main():
    """
    Entry point
    """
    RunSites()  # instantiate form
    # sim.run_ecosse()

if __name__ == '__main__':
    main()

