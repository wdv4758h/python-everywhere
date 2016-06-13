from setuptools import find_packages, setup


version = __import__('everywhere').VERSION
exclude_from_packages = []
requires = []


setup(
    name='python-everywhere',
    version=version,
    url='https://github.com/wdv4758h/python-everywhere',
    author='Chiu-Hsiang Hsu',
    author_email='wdv4758h@gmail.com',
    description=('A template project for Python'),
    long_description=open("README.rst").read(),
    download_url="https://github.com/wdv4758h/python-everywhere/archive/v{}.zip".format(
        version
    ),
    license='BSD',
    setup_requires=['pytest-runner',
                    'coverage', 'pytest-cov',
                    'flake8', 'pytest-flake8',
                    'pylint', 'pytest-pylint',
                    'mypy-lang',
                    'pydocstyle'],
    tests_require=['pytest'],
    install_requires=requires,
    packages=find_packages(exclude=exclude_from_packages),
    include_package_data=True,
    scripts=[],
    extras_require={},
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
