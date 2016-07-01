from setuptools import setup

setup(
    name='experiment-client',
    version='0.1',
    py_modules=['experiment-client'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        experiment-client=experiment-client:cli
    ''',
)