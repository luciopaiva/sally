from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sally',
    version='0.1.0',
    description='A command line tool to check the status of repositories in all subdirectories',
    long_description=long_description,
    url='https://github.com/luciopaiva/sally',
    author='Lucio Paiva',
    author_email='luciopaiva@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control'

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='version control git mercurial',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'sally=sally.sally:main',
        ],
    },
)
