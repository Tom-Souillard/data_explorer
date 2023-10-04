from setuptools import setup, find_packages

# Long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="data_explorer",
    version="0.1.0",
    author="Tom Souillard",
    author_email="tom.souillard@gmail.com",
    description="A versatile script for exploratory data analysis, including data loading, cleaning, descriptive analysis, and visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tom-Souillard/data-explorer",
    project_urls={
        "Bug Tracker": "https://github.com/Tom-Souillard/data-explorer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pandas>=2.2.2",
        "numpy>=1.26.4",
        "matplotlib>=3.9.0",
        "seaborn>=0.13.2",
        "scikit-learn>=1.5.0",
        "jupyter>=1.0.0",
        "notebook>=7.2.0",
        "pytest>=8.2.1"
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "data_explorer=data_explorer:main",
        ],
    },
)
