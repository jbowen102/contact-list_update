try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Contact List Update',
    'author': 'Jonathan Bowen',
    'url': 'https://github.com/jbowen102/contact-list_update'
    'download_url': 'https://github.com/jbowen102/contact-list_update',
    'author_email': 'jjbowen19@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'pandas'],
    'packages': [],
    'scripts': [],
    'name': 'contact_list_update'
}

setup(**config)
