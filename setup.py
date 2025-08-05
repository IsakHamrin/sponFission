from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='sponFission',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Isak Hamrin',
    author_email="isak.hamrin@gmail.com",
    license="MIT",
    description='Estimate spontaneous fission rates for materials',
    url='https://github.com/IsakHamrin/sponFission',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
