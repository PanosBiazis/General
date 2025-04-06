# from setuptools import setup
# from Cython.Build import cythonize
# import os

# # Print working directory to verify
# print(f"Current working directory: {os.getcwd()}")

# # Compile the Cython file
# setup(
#     ext_modules = cythonize("F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\sum_of_squares.pyx")  # Change the path if needed
# )

#PS F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ> python setupcython.py build_ext --inplace


from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/sum_of_squares.pyx")#(r"F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\sum_of_squares.pyx")
)
