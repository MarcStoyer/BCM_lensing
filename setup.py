from setuptools import setup, find_packages

setup(
    name="BCM_git",
    version="0.1.0",
    description="from MaxLee's github",
    packages=find_packages(
        include=["BCM_lensing", "BCM_lensing.*"],
    ),
    install_requires=[],
    python_requires=">=3.8",
)
