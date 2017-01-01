""" Setup the todo package """

from setuptools import setup
import sys

if sys.version_info[0] < 3:
    raise ValueError("Must be using Python 3")

setup(name="todo",
      packages=["todo"],
      version="0.0.0",
      description="A Flask-based ToDo system",
      author="Nathan Baker",
      author_email="nathanandrewbaker@gmail.com",
      license="MIT",
      install_requires=["flask"])
