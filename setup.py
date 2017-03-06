from setuptools import setup, find_packages

setup(name='terrible-pip-package',
      version='0.1',
      description='terrible pip package',
      url='',
      author='Someone',
      author_email='someone@email.com',
      license='Apache',
      packages=find_packages(),
      install_requires=[
        'pymongo'
      ],
      zip_safe=False)
