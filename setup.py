from setuptools import setup
setup(name='digit_rec',
      version='0.1',
      description='Detect digit given an image',
      url='https://github.com/ajayrfhp/digit_rec',
      author='ajayrfhp',
      author_email='ajayrfhp1710@gmail.com',
      license='MIT',
      packages=['digit_rec'],
      test_suite='nose.collector',
      install_requires=[
      	'numpy',
            'nose'
      ],
      zip_safe=False)