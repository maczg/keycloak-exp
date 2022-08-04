FROM nginx:alpine
VOLUME /var/log/nginx/log
EXPOSE 8080

RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf && \
        addgroup nginx root && \
        chmod g+rwx /var/cache/nginx /var/run /var/log/nginx

COPY default.conf.production /etc/nginx/templates/default.conf.template

#USER nginx
