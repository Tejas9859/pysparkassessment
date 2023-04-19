from setuptools import setup

setup(
    name="movieLensDemo",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "pyspark==3.1.3",
    ],
)
