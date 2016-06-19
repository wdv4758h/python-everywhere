from setuptools import find_packages, setup, Extension


def cythonize(*args, **kwargs):
    '''
    dirty hack, only import cythonize at the time you use it.

    if you don't write Cython extension,
    you won't fail even if you don't install Cython.
    '''
    global cythonize
    from Cython.Build import cythonize
    return cythonize(*args, **kwargs)


def mbcs_work_around():
    '''
    work around for mbcs codec to make "bdist_wininst" work
    https://mail.python.org/pipermail/python-list/2012-February/620326.html
    '''
    import codecs
    try:
        codecs.lookup('mbcs')
    except LookupError:
        ascii = codecs.lookup('ascii')
        codecs.register(lambda name: {True: ascii}.get(name == 'mbcs'))


version = __import__('everywhere').VERSION
exclude_from_packages = []
requires = []
extensions = [
    # TODO write your own extensions
    Extension('everywhere._base',
              sources=['everywhere/_base.c']),
    *cythonize(
        Extension('everywhere._base_cy',
                  sources=['everywhere/_base_cy.pyx']),
    ),
]

mbcs_work_around()


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
    ext_modules=extensions,
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
