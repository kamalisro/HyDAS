from cx_Freeze import setup, Executable as cxExecutable
import PIL
includefiles = ["Bands","Data","DispImage","Icons","Results"]

excludes = []
packages = ["atexit","PIL"]
WIN_Target = cxExecutable(
    script='setup.py',
    targetName='HyDaS.exe',
    compress=True,
    appendScriptToLibrary=True,
    appendScriptToExe=True,
    shortcutName="HyDaS",
    shortcutDir="Desktop",

    )

setup(
    name='Varun',
    description="HyDaS",
    version='0.1',
    author="VARUN TIWARI",

    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles,}},
    executables=[WIN_Target]
    )
