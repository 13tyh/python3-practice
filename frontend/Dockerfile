FROM node:22-alpine

WORKDIR /workspace/frontend

RUN corepack enable

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

CMD ["pnpm", "dev", "--host", "0.0.0.0"]
