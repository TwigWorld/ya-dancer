from setuptools import setup

version = "2.1.0"
readme = open("README.md").read()

setup(
    name="ya-dancer",
    version=version,
    description="Get a response json reflecting the current status of the site.",
    long_description=readme,
    author="David Paule",
    author_email="jdpaule@twig-world.com",
    url="https://github.com/TwigWorld/ya-dancer",
    packages=[
        "ya_dancer",
    ],
    include_package_data=True,
    install_requires=[
        "Django<3",
        "mongoengine",
    ],
    zip_safe=False,
    keywords="ya-dancer",
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    extras_require={
        "testing": [
            "black",
            "isort",
            "check_pdb_hook",
            "pre-commit",
        ]
    },
)
