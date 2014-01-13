import os

import numpy
from numpy.distutils.misc_util import Configuration


def configuration(parent_package="", top_path=None):
    config = Configuration("metrics", parent_package, top_path)
    libraries = []

    if os.name == 'posix':
        libraries.append('m')

    config.add_extension("metrics_fast",
                         sources=["metrics_fast.c"],
                         include_dirs=[numpy.get_include()],
                         libraries=libraries)

    config.add_extension("pairwise_fast",
                         sources=["pairwise_fast.c"],
                         include_dirs=[numpy.get_include()],
                         libraries=libraries)

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(**configuration().todict())
