from setuptools import setup

with open("README.md", "r", encoding="UTF-8") as fin:
      long_description = fin.read()

setup(name='pyLOPE',
      version='0.1.2',
      description='A python package for paedological purpose',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/seantyh/pyLOPE',
      author='Sean Tseng',
      author_email='seantyh@gmail.com',
      license='MIT',
      install_requires=[
      ],
      packages=['pyLOPE'],
      test_suite='pyLOPE.tests',
      zip_safe=False)

