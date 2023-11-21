#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name="wazo-fail2ban-backend",
    version="0.1",
    description="Backend to control fail2ban",
    author="Sylvain Boily",
    url="https://github.com/sboily/wazo-fail2ban-plugin",

    packages=find_packages(),
    include_package_data=True
)
