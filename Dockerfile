FROM python:3.8-alpine
# set working dir
WORKDIR /brand
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
ENV TKN="dp.st.dev.Zb7EWffOo6jiutnGYZ6gbdWVzxDJO5du6z6k6TqdGf1"

# copy secrets fetch script
COPY secrets.sh /brand
RUN chmod +x /brand/secrets.sh

# run doppler configure
RUN doppler configure -t TKN
# copy project files
COPY /brandxpert/* /brand/
# switch to non-root user
RUN adduser -D bxuser && chown -R bxuser /bx
USER bxuser
# expose port
EXPOSE 8080
#
#List Directory
#
RUN ls -la
# entrypoint
ENTRYPOINT ["./secrets.sh"]
CMD ["gunicorn", "brandxpert.wsgi:application", "-b", "0.0.0.0:8000"]
