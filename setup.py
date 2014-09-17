import sys

from setuptools import setup, find_packages

install_requires = [
    'Jinja2',
    'Routes',
]
if sys.version_info < (3, 4):
    install_requires.append('asyncio')


setup(
    name='induction',
    version='0.1',
    author='Bruno Renié',
    author_email='bruno@renie.fr',
    description='Simple asyncio-based web framework',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=install_requires,
    packages=find_packages(),
    test_suite='tests',
)
