import io
import re
from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("mqsenser/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="RabbitMQ",
    version=version,
    description="To send the data to Rabbit mq server  ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Venkatesh509/Rabbitmqsender",
    author="Venkatesh Areti",
    author_email="venkateshareti509@gmail.com",
    license="MIT",
    packages=["mqsender"],
    install_requires=["pika"],
    extras_require={
        "dev": [
            "pika",
            "pytest",
            "flake8"
        ],
        "docs": ["mkdocs", "mkdocs-material"],
    },
    project_urls={
        "Documentation": "https://ahmednafies.github.io/covid/",
        "Source": "https://github.com/ahmednafies/covid",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["covid=covid.cli:app"]},
    zip_safe=False,
    python_requires=">=3.6",
)