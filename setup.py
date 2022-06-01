# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rstcheck']

package_data = \
{'': ['*']}

modules = \
['test_rstcheck', 'test', 'AUTHORS']
install_requires = \
['docutils>=0.7,<0.19',
 'types-docutils>=0.18,<0.19',
 'typing-extensions>=4.1,<5']

extras_require = \
{'sphinx': ['sphinx>=4,<5']}

entry_points = \
{'console_scripts': ['rstcheck = rstcheck:main']}

setup_kwargs = {
    'name': 'rstcheck',
    'version': '4.0.0',
    'description': 'Checks syntax of reStructuredText and code blocks nested within it',
    'long_description': "========\nrstcheck\n========\n\n.. image:: https://travis-ci.org/myint/rstcheck.svg?branch=master\n    :target: https://travis-ci.org/myint/rstcheck\n    :alt: Build status\n\nChecks syntax of reStructuredText and code blocks nested within it.\n\n\n.. contents::\n\n\nInstallation\n============\n\nFrom pip::\n\n    $ pip install rstcheck\n\n\nSupported languages in code blocks\n==================================\n\n- Bash\n- Doctest\n- C (C99)\n- C++ (C++11)\n- JSON\n- XML\n- Python\n- reStructuredText\n\n\nExamples\n========\n\nWith bad Python syntax:\n\n.. code:: rst\n\n    ====\n    Test\n    ====\n\n    .. code:: python\n\n        print(\n\n::\n\n    $ rstcheck bad_python.rst\n    bad_python.rst:7: (ERROR/3) (python) unexpected EOF while parsing\n\nWith bad C++ syntax:\n\n.. code:: rst\n\n    ====\n    Test\n    ====\n\n    .. code:: cpp\n\n        int main()\n        {\n            return x;\n        }\n\n::\n\n    $ rstcheck bad_cpp.rst\n    bad_cpp.rst:9: (ERROR/3) (cpp) error: 'x' was not declared in this scope\n\nWith bad syntax in the reStructuredText document itself:\n\n.. code:: rst\n\n    ====\n    Test\n    ===\n\n::\n\n    $ rstcheck bad_rst.rst\n    bad_rst.rst:1: (SEVERE/4) Title overline & underline mismatch.\n\n\nOptions\n=======\n\n::\n\n    usage: rstcheck [-h] [--config CONFIG] [-r] [--report level]\n                    [--ignore-language language] [--ignore-messages messages]\n                    [--ignore-directives directives]\n                    [--ignore-substitutions substitutions] [--ignore-roles roles]\n                    [--debug] [--version]\n                    files [files ...]\n\n    Checks code blocks in reStructuredText. Sphinx is enabled.\n\n    positional arguments:\n      files                 files to check\n\n    optional arguments:\n      -h, --help            show this help message and exit\n      --config CONFIG       location of config file\n      -r, --recursive       run recursively over directories\n      --report level        report system messages at or higher than level; info,\n                            warning, error, severe, none (default: info)\n      --ignore-language language, --ignore language\n                            comma-separated list of languages to ignore\n      --ignore-messages messages\n                            python regex that match the messages to ignore\n      --ignore-directives directives\n                            comma-separated list of directives to ignore\n      --ignore-substitutions substitutions\n                            comma-separated list of substitutions to ignore\n      --ignore-roles roles  comma-separated list of roles to ignore\n      --debug               show messages helpful for debugging\n      --version             show program's version number and exit\n\n\nIgnore specific languages\n=========================\n\nYou can ignore checking of nested code blocks by language. Either use the\ncommand-line option ``--ignore`` or put a comment in the document:\n\n.. code-block:: rst\n\n    .. rstcheck: ignore-language=cpp,python,rst\n\nIgnore specific errors\n======================\n\nSince docutils doesn't categorize their error messages beyond the high-level\ncategories of: info, warning, error, and severe; we need filter them out at a\ntextual level. This is done by passing a Python regex. As example you can pass\na regex like this to ignore several errors::\n\n    (Title underline too short.*|Duplicate implicit target.*')\n\nConfiguration file\n==================\n\nYou can use the same arguments from the command line as options in the\nlocal configuration file of the project (just replace ``-`` for ``_``).\n``rstcheck`` looks for a file ``.rstcheck.cfg`` or ``setup.cfg`` in the\ndirectory or ancestor directories of the file it is checking.\n\nFor example, consider a project with the following directory structure::\n\n    foo\n    ├── docs\n    │   └── bar.rst\n    ├── index.rst\n    └── .rstcheck.cfg\n\n``.rstcheck.cfg`` contains:\n\n.. code-block:: cfg\n\n    [rstcheck]\n    ignore_directives=one,two,three\n    ignore_roles=src,RFC\n    ignore_messages=(Document or section may not begin with a transition\\.$)\n    report=warning\n\n``bar.rst`` contains:\n\n.. code-block:: rst\n\n    Bar\n    ===\n\n    :src:`hello_world.py`\n    :RFC:`793`\n\n    .. one::\n\n       Hello\n\n``rstcheck`` will make use of the ``.rstcheck.cfg``::\n\n    $ rstcheck foo/docs/bar.rst\n\n\nFor a Python project, you should put the configuration settings for\n``rstcheck`` inside the general ``setup.cfg`` `distutils configuration file`_,\nin the project root.\n\nYou can override the location of the config file with the ``--config`` argument::\n\n    $ rstcheck --config $HOME/.rstcheck.ini foo/docs/bar.rst\n\nwill use the file ``.rstcheck.ini`` in your home directory. If the argument to\n``--config`` is a directory, ``rstcheck`` will search that directory and any\nany of its ancestors for a file ``.rstcheck.cfg`` or ``setup.cfg``::\n\n   $ rstcheck --config foo /tmp/bar.rst\n\nwould use the project configuration in ``./foo/.rstcheck.cfg`` to check the\nunrelated file ``/tmp/bar.rst``.\nCalling ``rstcheck`` with the ``--debug`` option will show the location of the\nconfig file that is being used, if any.\n\n.. _distutils configuration file: https://docs.python.org/3/distutils/configfile.html\n\n\nSphinx\n======\n\nTo enable Sphinx::\n\n    $ pip install rstcheck[sphinx]\n\n    # or\n\n    $ pip install sphinx\n\nWith version 4.0 ``rstcheck`` added Sphinx as an optional extra where the version's lower\nconstraint is >=4.0 because of Sphinx's open upper constraints on jinja2 and markupsafe,\nwhich result in import errors if not pinned below version 3 and 2 respectively. This happend\nin Sphinx version 4.0.\n\nYou can also add Sphinx by yourself but the installed Sphinx version must be at least 1.5.\n\nTo check that Sphinx support is enabled::\n\n    $ rstcheck -h | grep 'Sphinx is enabled'\n\n\nUsage in Vim\n============\n\nUsing with Syntastic_:\n----------------------\n\n.. code:: vim\n\n    let g:syntastic_rst_checkers = ['rstcheck']\n\nUsing with ALE_:\n----------------\n\nJust install ``rstcheck`` and make sure is on your path.\n\n.. _Syntastic: https://github.com/scrooloose/syntastic\n.. _ALE: https://github.com/w0rp/ale\n\n\nUse as a module\n===============\n\n``rstcheck.check()`` yields a series of tuples. The first value of each tuple\nis the line number (not the line index). The second value is the error message.\n\n>>> import rstcheck\n>>> list(rstcheck.check('Example\\n==='))\n[(2, '(INFO/1) Possible title underline, too short for the title.')]\n\nNote that this does not load any configuration as that would mutate the\n``docutils`` registries.\n\nUse as a pre-commit hook\n========================\n\nAdd this to your ``.pre-commit-config.yaml``\n\n.. code-block:: yaml\n\n    -   repo: https://github.com/myint/rstcheck\n        rev: ''  # Use the sha / tag you want to point at\n        hooks:\n        -   id: rstcheck\n\nTesting\n=======\n\nTo run all the tests, do::\n\n    $ make test\n\nUnit tests are in ``test_rstcheck.py``.\n\nSystem tests are composed of example good/bad input. The test inputs are\ncontained in the ``examples`` directory. For basic tests, adding a test should\njust be a matter of adding files to ``examples/good`` or ``examples/bad``.\n\n\nHistory\n=======\n\n(next version)\n--------------\n\n4.0.0 (2022-04-15)\n------------------\n\n- Drop support for python versions prior 3.7\n- Add inline type annotations\n- Add ``sphinx`` as extra\n- Update build process and set up ``poetry``\n- Add ``pre-commit`` and ``tox`` for automated testing, linting and formatting\n- Move from travis to github actions\n- Activate dependabot\n\n3.5.0 (2022-04-14)\n------------------\n\n- Deprecate python versions prior 3.7\n\n3.4.0 (2022-04-12)\n------------------\n\n- Add ``--config`` option to change the location of the config file.\n- Add ``pre-commit`` hooks config.\n\n3.3.1 (2018-10-09)\n------------------\n\n- Make compatible with Sphinx >= 1.8.\n\n3.3 (2018-03-17)\n----------------\n\n- Parse more options from configuration file (thanks to Santos Gallegos).\n- Allow ignoring specific (info/warning/error) messages via\n  ``--ignore-messages`` (thanks to Santos Gallegos).\n\n3.2 (2018-02-17)\n----------------\n\n- Check for invalid Markdown-style links (thanks to biscuitsnake).\n- Allow configuration to be stored in ``setup.cfg`` (thanks to Maël Pedretti).\n- Add ``--recursive`` option to recursively drill down directories to check for\n  all ``*.rst`` files.\n\n3.1 (2017-03-08)\n----------------\n\n- Add support for checking XML code blocks (thanks to Sameer Singh).\n\n3.0.1 (2017-03-01)\n------------------\n\n- Support UTF-8 byte order marks (BOM). Previously, ``docutils`` would\n  interpret the BOM as a visible character, which would lead to false positives\n  about underlines being too short.\n\n3.0 (2016-12-19)\n----------------\n\n- Optionally support Sphinx 1.5. Sphinx support will be enabled if Sphinx is\n  installed.\n\n2.0 (2015-07-27)\n----------------\n\n- Support loading settings from configuration files.\n\n1.0 (2015-03-14)\n----------------\n\n- Add Sphinx support.\n\n0.1 (2013-12-02)\n----------------\n\n- Initial version.\n\n\n.. rstcheck: ignore-language=cpp,python,rst\n",
    'author': 'Steven Myint',
    'author_email': 'git@stevenmyint.com',
    'maintainer': 'Christian Riedel',
    'maintainer_email': 'cielquan@protonmail.com',
    'url': 'https://github.com/myint/rstcheck',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
