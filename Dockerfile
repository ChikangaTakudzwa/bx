FROM python:3.8-alpine

# set working dir
WORKDIR /brand

# set root dir to path
ENV PATH="/brand/:$PATH"

# copy dependencies and install them
COPY /brandxpert/requirements.txt /brand
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt && \
 apk --purge del .build-deps && \
 apk add --no-cache curl && \
 apk add --no-cache gnupg

# Install Doppler CLI
RUN wget -q -t3 'https://packages.doppler.com/public/cli/rsa.8004D9FF50437357.key' -O /etc/apk/keys/cli@doppler-8004D9FF50437357.rsa.pub && \
    echo 'https://packages.doppler.com/public/cli/alpine/any-version/main' | tee -a /etc/apk/repositories && \
    apk add doppler

# copy project files
COPY /brandxpert/ /brand/

# switch to non-root user
RUN adduser -D bxuser && chown -R bxuser /brand
USER bxuser

# expose port
EXPOSE 8000

CMD ["doppler", "run", "gunicorn", "--bind=0.0.0.0:8000", "--log-level=info", "brandxpert.wsgi"]
