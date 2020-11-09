import setuptools
from __version__ import version
import sys
with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "requests",
    "cryptography",
    "mutagen",
    "tqdm",
    "click",
    "pyinquirer",
    'configset',
    'bitmath',
    'make_colors',
    'pydebugger',
    'pywget',
]

if sys.platform == 'win32':
    requirements.append('pywin32>=223')
    requirements.append('dcmd')
    requirements.append('clipboard')
    requirements.append('cefpython3')
if 'linux' in sys.platform:
    requirements.append('clipboard')
    requirements.append('cefpython3')

setuptools.setup(
    name="deezersdk",
    version=version,
    author="LICFACE",
    author_email="licfae@yahoo.com",
    description="A package to search and download musics on Deezer, Download MP3 or FLAC from Deezer.com by Artist Name (cli)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cumulus13/deezersdk",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    license="GNU GPL v3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points="""
        [console_scripts]
        deezer=deezersdk.deez:usage
    """
)
