from setuptools import setup

def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()

configuration = {
    'name' : 'finishline',
    'version': '0.2.0',
    'description' : 'Framework for Building Beautiful and Functional Dashbords',
    'long_description' : readme(),
    'classifiers' : [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3 :: Only',
    ],
    'keywords' : 'dash dashboard ui grid layout',
    'url' : 'http://github.com/AlgorithmHub/finishline',
    'maintainer' : 'Alex Cabello',
    'maintainer_email' : 'alex.cabello@algorithmhub.com',
    'license' : 'MIT',
    'packages' : ['finishline'],
    'install_requires': ['dash >= 0.40.0',
                         'dash-responsive-grid-layout >= 0.2.0',
                         'dash-building-blocks >= 0.1.2'],
    'ext_modules' : [],
    'cmdclass' : {},
    'test_suite' : '',
    'tests_require' : [],
    'data_files' : ()
    }

setup(**configuration)
