# syntax=docker/dockerfile:1.7
FROM node:22-alpine

WORKDIR /workspace/frontend

ENV PNPM_HOME=/pnpm
ENV PATH=$PNPM_HOME:$PATH

RUN corepack enable

COPY package.json pnpm-lock.yaml ./
RUN --mount=type=cache,id=pnpm-store,target=/pnpm/store \
    pnpm install --frozen-lockfile --store-dir /pnpm/store

CMD ["pnpm", "dev", "--host", "0.0.0.0"]
