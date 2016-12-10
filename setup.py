from setuptools import setup, find_packages

install_requires = [
        'sqlalchemy',
        'flask',
        'bcrypt',
]

setup(
    name='portfolio',
    version='0.1.0',
    description='A CSST project open to public.',
    url='https://github.com/TumblrCommunity/PowerPortfolio',
    author='Neil Ashford',
    packages=find_packages(),
    install_requires=install_requires,
)
