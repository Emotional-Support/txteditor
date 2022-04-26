from distutils.core import setup

setup(
    name="txteditor",  # How you named your package folder (MyLib)
    packages=["txteditor"],  # Chose the same as "name"
    version="0.4",  # Start with a small number and increase it with every change you make
    license="Apache license 2.0",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Package to interact with .txt files",  # Give a short description about your library
    author="Emotional Support",  # Type in your name
    author_email="poilash227@gmail.com",  # Type in your E-Mail
    url="https://github.com/Emotional-Support/txteditor",  # Provide either the link to your github or to your website
    download_url="https://github.com/Emotional-Support/txteditor/archive/refs/tags/v_04.tar.gz",  # I explain this later on
    keywords=["txteditor", "txt", "unpack"],  # Keywords that define your package best
    install_requires=[],  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which python versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.10",
    ],
)
