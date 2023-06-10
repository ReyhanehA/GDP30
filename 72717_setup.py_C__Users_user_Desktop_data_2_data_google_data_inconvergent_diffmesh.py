#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

_extra = ['-O3', '-ffast-math']

extensions = [
  Extension('mesh',
            sources = ['./src/mesh.pyx'],
            extra_compile_args = _extra
  ),
  Extension('differential',
            sources = ['./src/differential.pyx'],
            extra_compile_args = _extra
  )
]

setup(
  name = "diffmesh",
  cmdclass={'build_ext' : build_ext},
  include_dirs = [],
  ext_modules = cythonize(extensions,include_path = [])
)
