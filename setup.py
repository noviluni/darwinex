from setuptools import setup
setup(
    name='darwinex_client',
    packages=['darwinex_client'],
    version='0.1.0',
    description='Darwinex API client',
    author='Marc Hernandez',
    author_email='noviluni@gmail.com',
    license='MIT',
    url='https://github.com/noviluni/darwinex',
    keywords='darwinex darwinex-api darwinex-client trading api-client',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['requests'],
    project_urls={
        'Bug Reports': 'https://github.com/noviluni/darwinex/issues',
        'Source': 'https://github.com/noviluni/darwinex',
    },
)
