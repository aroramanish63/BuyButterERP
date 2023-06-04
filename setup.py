from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in buybutterng/__init__.py
from buybutterng import __version__ as version

setup(
	name="buybutterng",
	version=version,
	description="Buy Butter",
	author="Manish Arora",
	author_email="aroramanish92@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
