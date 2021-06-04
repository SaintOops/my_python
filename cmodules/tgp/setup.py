from distutils.core import setup, Extension

setup(name='tgpAlghoritm', version='1.0',\
      ext_modules=[Extension('tgpAlghoritm', ['geneticprogramming.c'])])
