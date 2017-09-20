import os
import glob
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)

install_requires = [
    'PyYAML>=3.11',
    'stacker',
    'stacker_blueprints',
    'awacs>=0.6.0',
    'boto>=2.42'
]

tests_require = (
    'nose>=1.0',
    'mock==1.0.1',
    'coverage~=4.3.4',
    'flake8'
)


if __name__ == '__main__':
    setup(
        name='{{cookiecutter.repo_name}}',
        version='0.1.0',
        description='{{cookiecutter.description}}',
        install_requires=install_requires,
        tests_require=tests_require,
        test_suite='nose.collector',
        packages=find_packages(),
        scripts=glob.glob(os.path.join(src_dir, 'bin', 'scripts', '*'))
    )
