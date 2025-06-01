from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='localStoragePy',
      version='0.3.0',
      description='A familiar API from the Web, adapted to storing data locally with Python.',
      url='https://github.com/surajmandalcell/LocalStoragePro',
      author='Suraj Mandal',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author_email='contact@surajmandal.com',
      license='MIT',
      packages=['localStoragePy'],
      classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
      ],
      zip_safe=False
)

