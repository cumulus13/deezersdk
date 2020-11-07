import setuptools
from __version__ import version

with open("README.md", "r") as f:
    long_description = f.read()

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
    install_requires=[
        "requests",
        "cryptography",
        "mutagen",
        "tqdm",
        "click",
        "pyinquirer",
        'configset',
        'clipboard',
        'bitmath',
        'make_colors',
        'pydebugger',
        'pywget',
        'pywin32>=223',
        'dcmd',
        'cefpython3'
    ],
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
