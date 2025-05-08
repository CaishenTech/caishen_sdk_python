from setuptools import setup, find_packages

setup(
    name="caishen_sdk_python",
    version="0.1.2",
    description="The Caishen SDK gives every agent or user access to unlimited multi-chain crypto wallets",
    author="CaishenTech",
    author_email="hello@caishen.tech",
    url="https://github.com/CaishenTech/caishen_sdk_python/",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "pydantic>=1.10,<3.0",
        "langchain-core",
        "openai"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
