from distutils.core import setup

config = {
    'name': 'holidata',
    'version': '2020.1',
    'packages': ['holidata'],
    'license': 'MIT License',
    'description': 'Holidata is a utility for algorithmically producing holidays for a given locale and year',
    'url': 'https://github.com/GothenburgBitFactory/holidata',
    'author': 'Gothenburg Bit Factory',
    'author_email': 'support@gothenburgbitfactory.org',
    'requires': ['docopt', 'arrow'],
    'scripts': ['bin/holidata'],
}

setup(**config)
