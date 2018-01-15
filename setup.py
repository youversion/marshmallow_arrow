"""A Marshmallow Custom Field for Arrow objects."""

from setuptools import setup

setup(
    name='Marshmallow-Arrow',
    version='1.0',
    url='https://github.com/youversion/marshmallow_arrow',
    download_url='https://github.com/youversion/marshmallow_arrow/archive/master.zip',
    license='MIT',
    author='Alex Ronoquillo',
    author_email='developers@youversion.com',
    description='A Marshmallow Custom Field for Arrow objects.',
    long_description=__doc__,
    packages=['marshmallow_arrow'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'arrow',
        'marshmallow'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['marshmallow', 'arrow'],
    test_suite='tests',
)
