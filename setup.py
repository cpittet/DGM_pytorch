from setuptools import setup

setup(
    name='DGM',
    author='Luca Cosmo et al.'
    url='https://github.com/lcosmo/DGM_pytorch'
    install_requires=[
        'pytorch',
        'torchaudio',
        'torchvision',
        'pytorch_lightning',
        'torch-scatter',
        'torch-sparse',
        'torch-geometric'
    ]
)