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
# install doppler and configure it
RUN (curl -Ls --tlsv1.2 --proto "=https" --retry 3 https://cli.doppler.com/install.sh || wget -t 3 -qO- https://cli.doppler.com/install.sh) | sh
ENV TKN="dp.st.dev.n5AWDB6bJI5RJLNYmyqMMMcp5AJvOKP7KlCTw6YqKN4"
# copy secrets fetch script
COPY secrets.sh /brand
RUN chmod +x /brand/secrets.sh

# run doppler configure
RUN doppler configure -t TKN
COPY path.sh /brand
RUN chmod +x /brand/path.sh && path.sh
ENV DOPPLER_ENV=1

# copy project files
COPY /brandxpert/ /brand/
# switch to non-root user
RUN adduser -D bxuser && chown -R bxuser /brand
USER bxuser
# expose port
EXPOSE 8000
#List Directory
# RUN ls -la
# entrypoint
# ENTRYPOINT ["python3"]
CMD ["gunicorn", "brandxpert.wsgi:application", "-b", "0.0.0.0:8000"]
