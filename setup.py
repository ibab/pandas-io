from setuptools import setup

setup(name='pandas_io',
      version='0.0',
      description='Read and save DataFrames using various additional data formats',
      url='http://github.com/ibab/pandas-io',
      author='Igor Babuschkin',
      author_email='igor@babuschk.in',
      license='BSD3',
      install_requires=[
          'numpy',
          'pandas',
      ],
      packages=['pandas.io.external'],
      zip_safe=False)
