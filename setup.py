from setuptools import setup, find_packages

setup(
    name='pycon',
    version='0.0.1',
    description='PyCon ZA',
    author='Unomena Developers',
    author_email='dev@unomena.com',
    url='http://unomena.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    dependency_links = [
    ],
    install_requires = [
        'django-evolution',
        'python-memcached==1.48',
        'psycopg2==2.4.2',
        'flup',
    ],
    include_package_data=True,
)