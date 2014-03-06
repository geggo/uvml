#!/usr/bin/env python

def configuration():
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info

    mkl_info = get_info('mkl')
    mkl_info['libraries'].append('gfortran')

    config = Configuration(package_name = 'vml')
    config.add_extension('uvml', 
                         sources = ['vml/uvml_module.c.src'],
                         #extra_compile_args = ['-O2','-march=core2',],
                         **mkl_info)
    return config

def setup_package():
    from numpy.distutils.core import setup
    
    setup(
        name = 'vml',
        maintainer = 'Gregor Thalhammer',
        maintainer_email = 'gregor.thalhammer@gmail.com',
        description = "provides fast vector math functions, using Intel's Vector Math Library (vml)",
        license = 'BSD',
        packages = ['vml'],
        configuration = configuration)

if __name__ == '__main__':
    setup_package()
