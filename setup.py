from cx_Freeze import setup, Executable

setup(
    name = "AdditionApp",
    version = "0.1",
    description = "A simple addition script",
    executables = [Executable("addition.py")]
)
