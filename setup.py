from setuptools import setup

setup(
    name='experiment_client',
    version='0.1',
    py_modules=['experiment_client'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        experiment_client=experiment_client:cli
    ''',
)