from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='githubstats',
    version='v0.1.0',
    packages=['githubstats'],
    url='https://github.com/JGCRI/github_analytics',
    license='BSD 2-Clause Simplified',
    author='Chris R. Vernon',
    author_email='chris.vernon@pnnl.gov',
    description='Mine and archive GitHub repositories for insight analytics',
    install_requires=requirements
)
