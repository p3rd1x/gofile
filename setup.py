from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gofile',
    version='0.1.0',
    description='Package to access the gofile.io api ',
    long_description=readme,
    author='p3rd1x',
    author_email='p3rd1x@gmx.net',
    url='https://github.com/p3rd1x/gofile.py',
    license=license,
    packages=find_packages(),
    install_requires=[

    ]
)