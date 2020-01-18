from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="pytemp",
    version="0.1.0",
    description="Sample Python Template",
    long_description=readme,
    author="Yutaka Kato",
    author_email="kato.yutaka@gmail.com",
    url="https://github.com/yukkun007/python-template",
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        pytemp = main:main
    """,
)
