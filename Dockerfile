FROM python:3.10.4

WORKDIR /opt/service

# Install poetry
RUN pip install poetry


COPY ./poetry.lock /opt/service/poetry.lock
COPY ./pyproject.toml /opt/service/pyproject.toml

#RUN poetry install
RUN poetry install

COPY ./app /opt/service/app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]