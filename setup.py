import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mes-character-sheet',
    version='0.0.0',
    packages=['character_manager', 'game_manager'],
    include_package_data=True,
    license='?',
    description='Two Django apps to manage character sheets and WoD games.',
    long_description=README,
    url='http://thecharonsheet.com/',
    author='Melissa Avery-Weir',
    author_email='melissa@thecharonsheet.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ???', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)