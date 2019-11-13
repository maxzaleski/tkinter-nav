import setuptools
import tkinternav

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='tkinter-nav-mzaleski',
    version='0.0.1',
    author='Maximilien Zaleski',
    author_email='maximilienzaleski@yahoo.com',
    description='Lightweight navigation wrapper for Tkinter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maxzaleski/tkinter-nav',
    packages=[tkinternav],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache-2.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
