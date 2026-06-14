FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY README.md pyproject.toml ./
COPY src ./src
COPY tools ./tools
RUN uv sync --dev

CMD ["bash"]
