# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-hadi-M", # the name that you will install via pip
    version="1.0",
    author="Hadi Modares",
    author_email="modareshadi@gmail.com",
    description="Unit3, Sprint1, Module1, Assignment",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/hadi-M/lambdata_hadi-M",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)