import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { defineConfig } from "vitest/config";
import vue from "@vitejs/plugin-vue";

const indexPath = resolve(__dirname, "index.html");
let indexHtml = readFileSync(indexPath);

export default defineConfig({
  plugins: [
    {
      name: "serve-index-fast",
      configureServer(server) {
        server.watcher.add(indexPath);
        server.watcher.on("change", (file) => {
          if (resolve(file) === indexPath) {
            indexHtml = readFileSync(indexPath);
          }
        });

        server.middlewares.use(async (req, res, next) => {
          if (req.url !== "/" && req.url !== "/index.html") {
            next();
            return;
          }

          res.setHeader("Content-Type", "text/html");
          res.end(indexHtml);
        });
      },
    },
    vue(),
  ],
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true,
    warmup: {
      clientFiles: ["./src/main.ts", "./src/App.vue"],
    },
    hmr: {
      host: "localhost",
      clientPort: 5173,
    },
    watch: {
      usePolling: true,
      interval: 300,
    },
  },
  test: {
    environment: "jsdom",
    setupFiles: ["./src/test/setup.ts"],
  },
});
