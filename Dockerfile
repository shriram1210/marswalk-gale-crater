FROM python:3.12-slim AS unpack
WORKDIR /source
COPY deployment/ deployment/
COPY unpack.py .
RUN python unpack.py

FROM python:3.12-slim
WORKDIR /app
COPY --from=unpack /source/application/requirements-lock.txt .
RUN pip install --no-cache-dir -r requirements-lock.txt && useradd --uid 10001 --create-home marswalk
COPY --from=unpack --chown=marswalk:marswalk /source/application/ .
RUN python tools/build_dashboard.py && mkdir -p /app/state && chown marswalk:marswalk /app/state
USER marswalk
ENV PORT=10000 MARSWALK_STATE_DIR=/app/state
EXPOSE 10000
CMD ["sh", "-c", "exec python -m uvicorn marswalk.production:app --host 0.0.0.0 --port ${PORT:-10000} --workers 1 --limit-concurrency 8 --timeout-keep-alive 5 --no-server-header"]
