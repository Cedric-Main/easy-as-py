#!/usr/bin/python3

import os

def get_path_components():
	path_components = os.getcwd()
	path_components = path_components.split('/')
	path_components = path_components[1:]
	return path_components
print(get_path_components())
