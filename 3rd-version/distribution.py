
from setuptools import setup, find_packages

setup(
    name='personal-data-entry-form',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'flask-sqlalchemy',
        'marshmallow',
        'mysql-connector-python',
        'flask-cors',  
    ],
)
