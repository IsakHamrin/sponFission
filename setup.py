from setuptools import setup, find_packages

setup(
    name='sponFission',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    author='Isak Hamrin',
    description='Estimate spontaneous fission rates for materials',
    url='https://github.com/IsakHamrin/sponFission',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
