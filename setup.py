from setuptools import find_packages, setup

NAME = "feast_pheonixdb_online_store"
REQUIRES_PYTHON = ">=3.7.0"

setup(
    name=NAME,
    description=open("README.md").read(),
    version="0.0.1",
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(include=["feast_phoenixdb_online_store"]),
    install_requires=[
        "phoenixdb==1.1",
        "feast==0.12.1"
    ],
    license="Apache",
)
