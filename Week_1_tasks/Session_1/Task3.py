import os
import platform

# Print operating system information and System Paths
print("Operating System:", os.name)
print("System:", platform.system())
print("Release:", platform.release())
print("Version:", platform.version())
print("Paths:",os.environ['PATH'])
