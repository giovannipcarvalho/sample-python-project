# --- base image -----------------------------------------------------------------------
FROM python:3.10-slim-bullseye as base

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

# venv
RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

# base dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install build

WORKDIR /src

# --- dev stage ------------------------------------------------------------------------
FROM base as dev

# dev-only dependencies
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY myapp /src/myapp
COPY setup.* /src/
RUN pip install . --use-pep517 --no-deps

# --- runtime stage --------------------------------------------------------------------
FROM base as runtime

COPY myapp /src/myapp
COPY setup.* /src/
RUN pip install . --use-pep517 --no-deps

CMD ["python", "-m", "myapp"]
