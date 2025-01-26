from setuptools import setup


def parse_requirements(filename='requirements.txt'):
    """ load requirements from a pip requirements file """
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]


setup(
    name='npeet',
    version='2.0',
    packages=['npeet'],
    url='https://github.com/gregversteeg/NPEET',
    install_requires=parse_requirements(),
)
