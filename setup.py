from setuptools import setup, find_packages
import os 

os.environ

setup(name='terrible-pip-package',
      version=os.environ['GIT_TAG'],
      description='terrible pip package',
      url='https://github.com/jensendw/terrible-pip-package',
      author='Someone',
      author_email='someone@email.com',
      license='Apache',
      packages=find_packages(),
      install_requires=[
        'pymongo'
      ],
      zip_safe=False)
