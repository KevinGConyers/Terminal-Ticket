from setuptools import setup
setup(
    name = 'ttkt',
    version = '0.1.0',
    packages = ['ttkt'],
    entry_points = {
        'console_scripts': [
            'ttkt = ttkt.__main__:main'
        ]
    })
