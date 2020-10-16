"""
this is where we install our little module.  The endgame here is to get a hook into .venv/<user's package name>/.../site-packages
"""

# TODO: Finish this setup once things are in a better state otherwise.

from setuptools import setup

setup(
    name="PythonNanny",
    version="0.1",
    author="Ben Morsillo",
    author_email="benmorsillo@gmail",
    packages=["pythonanny"]
)
