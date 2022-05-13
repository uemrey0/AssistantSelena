from setuptools import setup


def _get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='AsistantSelena',
    version='1.1.0a',
    url='https://github.com/uemrey0/AssistantSelena',
    license='GPL-3.0',
    install_requires=_get_requirements(),
    author='uemrey0',
    author_email='ufukemreyuceturk@hotmail.com',
    description='Voice assistant with Turkish language'
)