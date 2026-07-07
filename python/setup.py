from setuptools import setup, find_packages

setup(
    name="hydrofoil-scada",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "pyserial"
    ],
    include_package_data=True,
)

