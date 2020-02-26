import os

from setuptools import find_packages, setup


setup(
    name="django-user-management",
    version="0.0.1",
    description="Django user management ",
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    install_requires=["Django", "djangorestframework"],
)
