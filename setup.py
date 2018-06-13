from cx_Freeze import setup, Executable

base = None
executables = [Executable("lagrange.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "lagrange",
    options = options,
    version = "0.1",
    description = 'lagrange interpolation',
    executables = executables
)