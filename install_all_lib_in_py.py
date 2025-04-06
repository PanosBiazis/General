from pypi_simple import PyPISimple
import subprocess

# Initialize PyPISimple
pypi = PyPISimple()

# Get a list of all available packages
packages = pypi.get_projects()

# Install each package
for package in packages:
    subprocess.run(['pip', 'install', package])
