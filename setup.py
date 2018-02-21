from setuptools import setup, find_packages
desc = "Command Line App to use Food2Fork's Search API through REST " \
       "to fetch top recipe for the given ingredients and report missing ones"

setup(
   name='foodie',
   version='0.0.3',
   url='https://github.com/rachit-ranjan16/foodie',
   description=desc,
   long_description=desc,
   license='GNU',
   author='rachit-ranjan16',
   author_email='rachit.ranjan93@gmail.com',
   classifiers=[
       "Development Status :: 5 - Production/Stable",
       "Intended Audience :: Developers",
       "Topic :: Software Development",
       "License :: OSI Approved :: GNU General Public License (GPL)",
       "Programming Language :: Python :: 3.5",
       ],
   keywords='rest-api food2fork',
   packages=find_packages(),  # same as name
   install_requires=['requests'],
   python_requires='~=3.5',
)
