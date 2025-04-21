from distutils.core import setup

setup(
    name="parapred-pytorch",
    version="1.0.2",
    author = "Alchemab",
    author_email = "jin@alchemab.com",
    description="PyTorch implementation of Parapred",
    packages=["parapred"],
    package_dir={
        "parapred": "parapred/"
    },
    package_data = {
        'parapred': ['weights/parapred_pytorch.h5']
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "parapred=parapred.cli:cli",
        ],
    },
)
