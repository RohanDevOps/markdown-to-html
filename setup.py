from setuptools import setup, find_packages

setup(
    name="markdown-to-html",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'flake8>=3.9',
        ],
    },
    entry_points={
        'console_scripts': [
            'md2html=converter:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Markdown to HTML converter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RohanDevOps/markdown-to-html",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)