FROM python:3.8-slim
# set working dir
WORKDIR /bx
# copy dependencies and install them
COPY /brandxpert/requirements.txt .
RUN \

 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


pip install --no-cache-dir -r  requirements.txt
# install doppler and configure it
RUN (curl -Ls --tlsv1.2 --proto "=https" --retry 3 https://cli.doppler.com/install.sh || wget -t 3 -qO- https://cli.doppler.com/install.sh) | sh
RUN doppler configure --service-token dp.st.dev.Zb7EWffOo6jiutnGYZ6gbdWVzxDJO5du6z6k6TqdGf1 --store dev
# copy project files
COPY /brandxpert/* .
# copy secrets fetch script
COPY secrets.sh .
RUN chmod +x /secrets.sh
# switch to non-root user
RUN useradd --uid 1000 bxuser && chown -R bxuser /bx
USER bxuser
# expose port
EXPOSE 8080
# entrypoint
ENTRYPOINT ["/secrets.sh", "gunicorn", "brandxpert.wsgi:application", "-b", "0.0.0.0:8000"]
