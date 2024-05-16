FROM python:3


SHELL ["/bin/bash", "-c"]
ENV SHELL="/bin/bash"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash appholder && chmod 777 /opt /run

WORKDIR /appholder

RUN mkdir /appholder/static && mkdir /appholder/media
RUN chown -R appholder:appholder /appholder && chmod 755 /appholder

COPY --chown=appholder:appholder . .

RUN pip install poetry
RUN poetry install

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
