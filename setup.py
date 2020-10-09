from setuptools import setup

#with open("READ_ME.txt", 'r') as f:
#    long_description = f.read()

dependency_lst = [
    # datastore_updater
    'bs4',
    'requests',
    'selenium',
    'numpy',
    'pandas',
    'openpyxl',
    'xlrd'                      # for pandas
]

setup(
    name='invest_scripts',
    version='0.0.0',
    description='collection of scripts for Lee investments',
#    long_description=long_description,
    author='Lee Tianli',
    author_email='94tian@gmail.com',
#    packages=['datastore_updater'],  #same as name
    install_requires=dependency_lst,
    setup_requires=dependency_lst,
)
