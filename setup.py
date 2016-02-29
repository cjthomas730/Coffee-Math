"""
Setup script for coffee-math
"""

from setuptools import setup

with open('README.md') as f:
    readme = f.read().strip()

setup(
    name='coffee-math',
    author='Christian Thomas',
    author_email='cjthomas730@gmail.com',
    classifiers=[
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    description="Calculate the right amount of coffee to make.",
    install_requires=[
        'six'
    ],
    keywords='coffee',
    license="New BSD",
    long_description=readme,
    url='https://github.com/cjthomas730/Coffee-Math',
    version='0.1',
    zip_safe=True,
    py_modules=['coffee_math'],
    entry_points="""
        [console_scripts]
        coffee-math=coffee_math:_cli
    """

)