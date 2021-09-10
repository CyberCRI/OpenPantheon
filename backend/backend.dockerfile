FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./backend/app/pyproject.toml ./backend/app/poetry.lock /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "set -e ; if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi" && \
    rm -rf /root/.cache

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
ARG INSTALL_JUPYTER=false
RUN bash -c "set -e ; if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi" && \
    rm -rf /root/.cache

ENV PYTHONPATH=/app \
    PORT=8080 \
    WORKER_CLASS=app.uvicorn_worker.OpenPantheonUvicornWorker

EXPOSE 8080

COPY ./backend/app /app
