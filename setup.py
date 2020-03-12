# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pygame
from pygame.locals import *



with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algoedu',
    version='0.1',
    packages=find_packages()
    
)