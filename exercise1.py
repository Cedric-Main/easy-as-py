#!/usr/bin/python3

import os

path_components = os.getcwd()
path_components = path_components.split('/')
path_components = path_components[1:]

print(path_components)
