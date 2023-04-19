#----------------------------------------------------------------------
# Steps To Create Pythonic DLL Known As PYD(Windows)/SO(Linux)
#----------------------------------------------------------------------
# Steps:
"""
  1. pip install cython
  2. Create A Pythonic Program: test.py
  3. Re-save it as test.pyx
  4. Build The setup.py (python setup.py build_ext --inplace)
      --> setup(ext_modules = cythonize('test.pyx')
  5. Import the built pyd into your program (test.cp39-win_amd64.pyd <-- import test)

"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize([
                          Extension("test", ["test.pyx"]),
                          #Extension("test1", ["test1.pyx"]),
  
                          #...
  
                          #Extension("testn", ["testn.pyx"]),
  
  setup(ext_modules = ext_modules)
