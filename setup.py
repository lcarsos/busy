"""Installer for busy"""
import os.path
from setuptools import setup, find_packages

from busy import version

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='busy',
    version=version,
    description='A todo list application for people serious about todo lists',
    long_description=long_description,
    url='https://github.com/lcarsos/busy.git',
    author='Ezekiel (lcarsos) Chopper',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
    keywords=['todo', 'pomodoro', 'task management', 'time tracking'],
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'busy=busy:main',
        ],
    },
)
