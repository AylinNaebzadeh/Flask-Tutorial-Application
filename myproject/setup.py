from os import name
from setuptools import find_packages, setup, version

# run (flask --version) in your terminal to check your flask version

setup(
    name='flasker',
    version='2.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)