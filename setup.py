from setuptools import setup
setup(name='license_plate_recognition',
      version='0.1',
      description='Detect license plate number of a car',
      url='https://github.com/ajayrfhp/license_plate_recognition',
      author='ajayrfhp',
      author_email='ajayrfhp1710@gmail.com',
      license='MIT',
      packages=['license_plate_recognition'],
      install_requires=[
      	'sklearn',
      	'numpy',
      	'pickle'
      ],
      zip_safe=False)