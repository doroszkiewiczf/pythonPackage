from setuptools import setup, find_packages

setup(
    name='AdviceLib',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='Example advice python package',
    install_requires=['csv'],
    url='https://github.com/doroszkiewiczf/pythonPackage',
    author='Filip Doroszkiewicz',
    author_email='doroszkiewicz.f@gmail.com'
)
