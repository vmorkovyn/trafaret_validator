import os

from setuptools import setup


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


version = [line for line in read('trafaret_validator/__init__.py').split('\n')
           if '__version__' in line][0]
exec(version)


setup(name='trafaret_validator',
      version=__version__,
      description='A validation library for python using trafaret',
      long_description=read('README.rst'),
      classifiers=classifiers,
      platforms=["any"],
      author='Valeriy Morkovyn',
      author_email='minouts@gmail.com',
      url='https://github.com/Lex0ne/trafaret_validator',
      packages=["trafaret_validator"],
      install_requires=['trafaret'],
      test_suite='tests',
      include_package_data=True,
)
