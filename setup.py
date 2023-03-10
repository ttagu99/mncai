import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mncai", 
    version="0.0.1",
    author="daewoo myoung",
    author_email="dwmyoung@mnc.ai",
    description="mncai dev pack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ttagu99/mncai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
