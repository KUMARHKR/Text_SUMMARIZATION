import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ = "0.0.1"

REPONAME = "Text-Summarization"
AUTHOR = "DIP KUMAR DHAWA"
SRC_REPO = "Text_SUMMARIZATION"
AUTHOR_EMAIL = "dipkumardhawa020@gmail.com"


setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A snall python NLP 'Text Summarization' App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/KUMARHKR/Text_SUMMARIZATION.git",
    package_dir={"": "src"},
    packages=setuptools.find_packages(),

)