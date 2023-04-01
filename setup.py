import setuptools

setuptools.setup(
    name="neuroshard",
    version='1.0.0',
    author="Nobody",
    author_email="nobody@gmail.com",
    description="neuroshard",
    url="https://github.com/nobody/neuroshard",
    keywords=["Sharding"],
    packages=setuptools.find_packages(exclude=('tests',)),
    requires_python='>=3.8',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
