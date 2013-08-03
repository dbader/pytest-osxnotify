from setuptools import setup
setup(
    author="Daniel Bader",
    author_email="mail@dbader.org",
    version="0.1.0",
    description="OS X notifications for py.test results.",
    name="pytest-osxnotify",
    keywords="pytest, pytest-, osx, notifications, mountainlion, notificationcenter, py.test",
    packages=['pytest_osxnotify'],
    entry_points={'pytest11': ['pyest_osxnotify = pytest_osxnotify', ]},)
