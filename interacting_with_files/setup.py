from setuptools import setup, find_packages


setup(
    name="interacting_with_files",
    version="0.1.0",
    author="Nhlakanipho",
    author_email="nhlakanipho.ngubo@umuzi.org",
    description="This project stores visitor data in separate json files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="Umuzi-org/Nhlakanipho-Ngubo-695-interacting-with-files-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.1",
    install_requires=[],
)
