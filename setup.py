from setuptools import setup

setup(
    name='sustime spammer',
    version='1.0',
    description='Når 1 sustime bare ikke er godt nok',
    author='ERItenov',
    author_email='elit1@elev.tec.dk',
    license='MIT',
    packages=['sustime spammer'],
    install_requires=[
        'selenium', 'webdriver_manager',
    ],
    zip_safe=False)