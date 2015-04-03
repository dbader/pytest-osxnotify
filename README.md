pytest-osxnotify
================

[![PyPI](https://pypip.in/v/pytest-osxnotify/badge.png)](https://pypi.python.org/pypi/pytest-osxnotify)
[![PyPI](https://pypip.in/d/pytest-osxnotify/badge.png)](https://pypi.python.org/pypi/pytest-osxnotify)<br>
![Demo](https://raw.github.com/dbader/pytest-osxnotify/master/demo.gif)

A py.test plugin that displays test results using native Mac OS X
notifications (`NSUserNotification`). Works with Python 2.7 and 3.3+ on
Mountain Lion or better.


Usage
-----

```shell
$ pip install pytest-osxnotify
$ py.test
```

How to test a change to the plugin
----------------------------------

```shell
$ virtualenv venv && . venv/bin/activate
$ pip install pytest -r requirements.txt
$ python setup.py install
$ venv/bin/py.test --traceconfig example_test.py -p pytest_osxnotify
```

How to submit a new release to PyPi
-----------------------------------

```shell
$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags
$ python setup.py sdist upload -r pypi
```

Meta
----

Daniel Bader – [@dbader_org](https://twitter.com/dbader_org>) – mail@dbader.org

Distributed under the MIT license. See ``LICENSE`` for more information.

https://github.com/dbader/pytest-osxnotify
