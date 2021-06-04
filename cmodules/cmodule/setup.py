from distutils.core import setup, Extension

setup(name='someSimpleFunc', version='1.0',\
      ext_modules=[Extension('someSimpleFunc', ['func.c'])])
