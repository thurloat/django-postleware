#!/usr/bin/env python
from setuptools import setup

install_requires = [
    'django>=1.2',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='django-postleware',
    version='1.0.2',
    author='Adam Thurlow',
    author_email='thurloat@gmail.com',
    url='http://github.com/thurloat/django-postleware',
    description='A simple django middleware that ensures POSTs aren\'t cached by clients.',
    long_description=readme,
    license='BSD',
    packages=['postleware'],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
)
