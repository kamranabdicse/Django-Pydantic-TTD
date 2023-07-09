FROM python:3.11

WORKDIR /
ENV PYTHONPATH=/


# Install Poetry version 1
RUN pip install poetry
RUN poetry config virtualenvs.create false
# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock* .
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt
RUN pip install -r requirements.txt

COPY ./ .


# Install Poetry version 2
# RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
#     cd /usr/local/bin && \
#     ln -s /opt/poetry/bin/poetry && \
#     poetry config virtualenvs.create false



CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "config.wsgi:application"]