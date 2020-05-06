# https://stackoverflow.com/questions/42048421/how-to-package-a-python-c-extension-such-that-it-is-a-submodule-of-a-normal-pyth
#  -- how to put c-code inside a submodule
"""
According to GSL documentation (http://www.gnu.org/software/gsl/manual/html_node/Shared-Libraries.html), 
in order to run the different operations one must include the GSL library, the GSLCBLAS library and the 
math library. To compile in C one must do:
  	
  gcc -Wall -c filename.c

And then:

  gcc -static nombredelarchivo.o -lgsl -lgslcblas -lm

The first part is done by Python by this file. The second part (adding "-lgsl -lgslcblas -lm"), obviously isn't. To add any libraries that in C would be called by:

  gcc -static nombredelarchivo.o -lname1 -lname2 -lname3...

Is as simple as putting libraries=['name1','name2',...] inside the Extension module. Here we do it with "gsl", "gslcblas" and "m".
"""

from numpy import get_include

try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension

module = Extension('flicker.Wavelets.FWT',
                   sources=['flicker/Wavelets/FWT.c'],
                   libraries=['m'],
                   include_dirs=[get_include(), '/usr/local/include'])

setup(name='flicker',
      version=0.1,
      description=('Carter/Winn Debauchie Wavelet Analysis'
                   'for Transit Light Curves'),
      long_description=open('README.md').read(),
      url='https://github.com/exowanderer/flicker-noise',
      license='GPL3',
      author="Nestor Espinoz (nespino) and Jonathan Fraine (exowanderer)",
      packages=find_packages(),
      install_requires=['numpy', 'scipy'],
      ext_modules=[module]
      )
