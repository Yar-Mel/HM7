from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='file sorter for specific extensions',
    url='https://github.com/Yar-Mel/HM7',
    author='Yaroslav Melnychuk',
    author_email='yarmel.dev@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean']}
)