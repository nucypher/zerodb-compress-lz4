from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'zerodb',
    'lz4-cffi']

setup(
    name="zerodb-compress-lz4",
    version="0.1",
    description="LZ4 compression for ZeroDB",
    author="ZeroDB Inc.",
    author_email="michael@zerodb.io",
    license="AGPLv3",
    url="http://zerodb.io",
    packages=find_packages(),
    namespace_packages=["zerodbext"],
    install_requires=INSTALL_REQUIRES,
)
