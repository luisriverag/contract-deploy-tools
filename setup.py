from setuptools import setup, find_packages

setup(
    name='contract-deploy-tools',
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    packages=find_packages(),
    install_requires=[
        'py-solc',
        'web3',
    ]
)
