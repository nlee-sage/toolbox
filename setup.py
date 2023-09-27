import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toolbox",
    version="0.0.1",
    author="Nicholas Lee",
    author_email="nicholas.lee@sagebase.org",
    description="Tools used for synapse curation and data modeling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nlee-sage/toolbox",
    project_urls={"Bug Tracker": "https://github.com/nlee-sage/toolbox/issues"},
    license="MIT",
    package_dir={"": "toolbox"},
    packages=find_packages("toolbox"),
    install_requires=["requests"],
)
