FROM python:3.13-slim AS builder

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install \ 
    --root-user-action=ignore \
    --upgrade pip

COPY requirements.txt /app/
RUN pip install  \
    --root-user-action=ignore \
    --no-cache-dir -r requirements.txt

##
# Stage 2
##

FROM python:3.13-slim
RUN mkdir -p /app/static

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
WORKDIR /app
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["gunicorn", "vesctige_app.asgi:application", \
    "-k", "uvicorn.workers.UvicornWorker", \
    "--bind", "0.0.0.0:8000", \
    "--workers", "3", \
    "--timeout", "60" \
]
