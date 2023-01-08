# Getting started

First-time setup:
```bash
mamba env create
mamba activate myapp
pip install pip-tools
pip-sync requirements-dev.txt
```

Run tests and check coverage:
```bash
coverage run -m pytest
coverage report -m
```

Run locally:
```bash
python -m myapp
```

Build and run container:
```bash
docker build . -t myapp  # builds into a ~150MB image
docker run --rm -it -p 5000:5000 myapp
```

Manage dependencies:
```bash
# generate pinned dependencies: requirements.txt and requirements-dev.txt
pip-compile setup.cfg --resolver backtracking -o requirements.txt
pip-compile setup.cfg --resolver backtracking -o requirements-dev.txt --extra dev

# selectively upgrade dependencies
pip-compile setup.cfg --resolver backtracking -o requirements.txt --upgrade-package flask
```
