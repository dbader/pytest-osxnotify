from distutils.core import setup

__VERSION__ = '0.1.6'
__URL__ = 'https://github.com/dbader/pytest-osxnotify'
__DOWNLOAD_URL__ = (__URL__ + '/tarball/' + __VERSION__)

setup(
    author='Daniel Bader',
    author_email='mail@dbader.org',
    version=__VERSION__,
    description='OS X notifications for py.test results.',
    url=__URL__,
    download_url=__DOWNLOAD_URL__,
    name='pytest-osxnotify',
    keywords=[
        'pytest', 'pytest-', 'osx', 'notifications', 'mountainlion',
        'notificationcenter', 'py.test'],
    packages=['pytest_osxnotify'],
    entry_points={'pytest11': ['pyest_osxnotify = pytest_osxnotify', ]},
    install_requires=[
        'pyobjc-core',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
