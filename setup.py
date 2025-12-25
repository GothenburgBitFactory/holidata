#!/usr/bin/env python3

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="holidata",
    version="2025.12.0",
    description="Holidata is a utility for algorithmically producing holidays for a given locale and year",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GothenburgBitFactory/holidata",
    author="Gothenburg Bit Factory",
    author_email="support@gothenburgbitfactory.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="holiday, calendar",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.10, <4",
    install_requires=[
        "arrow >= 1.4.0",
        "docopt >= 0.6.2",
    ],
    extras_require={
        "test": [
            "pytest >= 9.0.2",
            "syrupy >= 5.0.0",
        ]
    },
    scripts=["bin/holidata"],
    project_urls={
        "Bug Reports": "https://github.com/GothenburgBitFactory/holidata/issues",
        "Source": "https://github.com/GothenburgBitFactory/holidata",
        "Website": "https://holidata.net",
    },
)
