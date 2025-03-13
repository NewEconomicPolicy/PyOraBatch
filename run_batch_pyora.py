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
from os.path import abspath, expanduser, expandvars, normpath, join, isfile, split, isdir

from initialise_pyorator_batch import read_config_file, initiation

sleepTime = 5
WARN_STR = '*** Warning *** '
PROGRAM_ID = 'spec_run'
ERROR_STR = '*** Error *** '
FNAME_RUN = 'FarmWthrMgmt.xlsx'

class RunSite(object):
    """
    C
    """
    def __init__(self, run_fns_dir):
        """
        C
        """
        initiation(self)
        read_config_file(self)
        pass

def main():
    """
    Entry point
    """
    argparser = ArgumentParser(prog=__prog__,
                               description='Run ECOSSE in parallel for spatial simulations.',
                               usage='{} runfile'.format(__prog__))
    argparser.add_argument('runfnsdir', help='Full path of for the Excel run files' + FNAME_RUN)
    args = argparser.parse_args()
    args.runfnsdir= abspath(normpath(expanduser(expandvars(args.runfnsdir))))

    RunSite(args.runfnsdir)  # instantiate model run
    # sim.run_ecosse()

if __name__ == '__main__':
    main()

