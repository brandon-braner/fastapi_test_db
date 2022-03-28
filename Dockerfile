FROM python:3.10.4

WORKDIR /opt/service

# Install poetry
RUN pip install poetry


COPY ./poetry.lock /opt/service/poetry.lock
COPY ./pyproject.toml /opt/service/pyproject.toml
COPY ./alembic.ini /opt/service/alembic.ini

#RUN poetry install
RUN poetry install

COPY ./ /opt/service

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]