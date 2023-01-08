# Getting started

First-time setup:
```bash
mamba env create
mamba activate mylib

pip install -e .[dev]
```

Run tests and check coverage:
```bash
coverage run -m pytest
coverage report -m
```

Build and publish:
```bash
# build
python -m build
# generates:
#   mylib-0.1.0.tar.gz           (source distribution)
#   mylib-0.1.0-py3-none-any.whl (wheel distribution)

# publish
python -m twine upload dist/mylib-0.1.0*  # upload both sdist and wheel
# use pypi user:pass or __token__:token
```

Since this is a library, you may want to test against multiple Python versions.

Consider using [`tox`](https://tox.wiki/en/latest/) to automate this.
