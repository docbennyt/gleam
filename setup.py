from setuptools import setup, find_packages

setup(
    name="GLEAM",
    version="0.1.0",
    author="Dr BennyT",
    author_email="dr.bennyt.09@gmail.com",
    description="Gamified Learning Examiner AI Module (GLEAM) - AI-driven quiz generation and adaptive testing framework",
    long_description=open("README.md", encoding="utf-8").read() if True else "",
    long_description_content_type="text/markdown",
    url="https://github.com/docbennyt/gleam",  # Update with your repo
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        "transformers>=4.0.0",
        "torch",           # Required by transformers
        "PyPDF2>=3.0.0",
        "flask>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Framework :: Flask",
    ],
    entry_points={
        'console_scripts': [
            # Optional CLI entry points can be added here
            # e.g. 'gleam-cli=gleam.cli:main',
        ],
    },
    include_package_data=True,
    keywords="quiz AI learning exam adaptive testing education",
)