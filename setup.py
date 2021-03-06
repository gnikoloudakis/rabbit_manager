import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rabbit-manager",
    version="0.0.3b",
    author="Yannis Nikoloudis",
    author_email="author@example.com",
    description="A small rabbitMQ package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gnikoloudakis/rabbit_manager",
    project_urls={
        "Bug Tracker": "https://github.com/gnikoloudakis/rabbit_manager",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)