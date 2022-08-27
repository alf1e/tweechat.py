import setuptools

import tweechat

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="tweechat.py",
    version=tweechat.__version__,
    author="ItsMeAlfie0",
    description="Unofficial Tweechat python libray",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["tweechat"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=requirements,
)