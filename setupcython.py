# from setuptools import setup
# from Cython.Build import cythonize
# import os

# # Print working directory to verify
# print(f"Current working directory: {os.getcwd()}")

# # Compile the Cython file
# setup(
#     ext_modules = cythonize("./local_file ΑΣΚΗΣΕΙΣ\sum_of_squares.pyx")  # Change the path if needed
# )

#PS ./local_file ΑΣΚΗΣΕΙΣ> python setupcython.py build_ext --inplace


from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(r"./data")#(r"./local_file ΑΣΚΗΣΕΙΣ\\sum_of_squares.pyx")
)
