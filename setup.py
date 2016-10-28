from setuptools import setup, find_packages

VERSION = '0.0.4'


setup(
    name="mkdocs-gov-au-theme",
    version=VERSION,
    url='https://www.dto.gov.au/',
    license='MIT',
    description='DTO UI Kit theme for MkDocs',
    author='Digital Transformation Office',
    author_email='simon.schwartz@digital.gov.au',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'gov-au-theme = gov_au_theme',
        ]
    },
    zip_safe=False
)
