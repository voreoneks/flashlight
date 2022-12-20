FROM python:3.10

ARG APP_ROOT="/usr/local/flashlight"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:${APP_ROOT}"

ENV APP_USER service_user
ENV C_FORCE_ROOT true

RUN groupadd -r docker \
    && useradd -r -m \
    --home-dir ${APP_ROOT} \
    -s /usr/sbin/nologin \
    -g docker ${APP_USER}
RUN usermod -aG sudo ${APP_USER}

WORKDIR ${APP_ROOT}

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# VOLUME [ "$APP_ROOT/data" ]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t flashlight .  
# docker run -i -p 8000:8000 --env--file ./env/.env.pred -v logs:/usr/local/flashlight/data --name flashlight_con flashlight:latest