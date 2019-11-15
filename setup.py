import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='tkinter-nav',
    version='0.0.5',
    author='Maximilien Zaleski',
    author_email='maximilienzaleski@yahoo.com',
    description='Lightweight navigation wrapper for Tkinter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maxzaleski/tkinter-nav',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License'
    ],
    python_requires='>=3.6',
)
