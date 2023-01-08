# sample-python-package

Accompanying code for the article ["Python packaging for developers in a hurry"](https://giovannipcarvalho.github.io/2023/01/08/python-packaging-in-a-hurry.html).

The toolset:
* [mamba](https://github.com/mamba-org/mamba) (from the [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) distribution) for managing Python environments and installing packages which are only available in conda's repositories
* [pip-tools](https://github.com/jazzband/pip-tools) for managing and pinning direct and transitive dependencies for applications (libraries are only [loosely-pinned](https://github.com/Yelp/requirements-tools#our-stance-on-pinning-requirements))
* [setuptools](https://setuptools.pypa.io/en/latest/) for packaging the project with a declarative configuration in `setup.cfg`
* [build](https://github.com/pypa/build) and [twine](https://github.com/pypa/twine) for sane and foolproof packaging and publishing of **libraries** on [PyPI](https://pypi.org/)
* [docker](https://www.docker.com/) for packaging code and runtime environment of **applications**

The benefits:
* Effortless and consistent workflow across Linux, Windows and macOS
* Access to a vast catalog of packages that are hard-to-install, available from conda's repositories (`mamba`)
* Fast, easy-to-manage, and human-readable generation of pinned application dependencies for reproducible environments (`pip-tools`)
* Simple, easy-to-manage declarative configuration for packaging the project (`setuptools` and `setup.cfg`)
* Easy to get right, hard to [get wrong](https://jwodder.github.io/kbits/posts/pypkg-mistakes/) building of source and wheel distributions for libraries (`build` and `twine`)
* Fast-to-build and cache-friendly docker images for applications, with a helpful `dev` stage for usage in CI environments (`docker`)

## Contents
* `application`: contains a sample project structure for an application (where pinning dependencies, simple builds and isolated environments are key)
* `library`: contains a sample project structure for a library (where maximizing compatibility, and robust and reproducible building of source and wheel distributions are important)

Each folder contains a `README.md` that guides you through the (very similar) steps for getting started with them.
