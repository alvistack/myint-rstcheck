# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rstcheck']

package_data = \
{'': ['*']}

modules = \
['AUTHORS']
install_requires = \
[
    'importlib-metadata>=1.6,<5.0; python_version < "3.8"',
    'rstcheck-core>=1.0.2,<2.0.0',
    'typer[all]>=0.4.1,<0.8',
    'typing-extensions>=3.7.4,<5.0; python_version < "3.8"',
]

entry_points = \
{'console_scripts': ['rstcheck = rstcheck._cli:main']}

setup_kwargs = {
    'name': 'rstcheck',
    'version': '6.1.1',
    'description': 'Checks syntax of reStructuredText and code blocks nested within it',
    'author': 'Steven Myint',
    'author_email': 'git@stevenmyint.com',
    'maintainer': 'Christian Riedel',
    'maintainer_email': 'cielquan@protonmail.com',
    'url': 'https://github.com/rstcheck/rstcheck',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
