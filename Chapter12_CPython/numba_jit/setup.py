from distutils.core import setup

from math_numba import cc


setup(name="math_numba",
      version="1.0.0",
      description="Numba module in Python",
      ext_modules=[cc.distutils_extension()])
