'''
Task description: Write a python program to access environment variables.

'''

import os
import platform

print("Operating System:", os.name)
print("System:", platform.system())
print("Release:", platform.release())
print("Version:", platform.version())

env_variable_names = os.environ.keys()

path_variables = [name for name in env_variable_names if 'PATH' in name]

print("\nEnvironment variables related to paths:")
for path_var in path_variables:
    print(f"{path_var}: {os.environ[path_var]}")
