import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description =  f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_summarizer"
AUTHOR_USERNAME = "datasciencetush"
SRC_REPO = "Text_summarizer"
AUTHOR_EMAIL = "datasciencetush@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description='A text summarizer project',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues/",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)