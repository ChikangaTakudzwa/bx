FROM python:3.8-slim
# set working dir
WORKDIR /bx
# copy dependencies and install them
COPY /brandxpert/requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt
# install doppler and configure it
RUN (curl -Ls --tlsv1.2 --proto "=https" --retry 3 https://cli.doppler.com/install.sh || wget -t 3 -qO- https://cli.doppler.com/install.sh) | sh
RUN doppler configure --service-token YOUR_API_KEY --store YOUR_STORE_NAME
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
