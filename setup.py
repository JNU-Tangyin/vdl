from setuptools import setup, find_packages

setup(
    name="vdl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "yt-dlp>=2023.11.16",
        "beautifulsoup4>=4.12.2",
        "click>=8.1.7",
        "rich>=13.7.0",
    ],
    entry_points={
        "console_scripts": [
            "vdl=vdl:cli",
        ],
    },
    author="Yin",
    description="A command-line video downloader supporting multiple platforms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vdl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
