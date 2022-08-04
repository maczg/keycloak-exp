FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/default.conf
VOLUME /var/log/nginx/log
RUN nginx -t
EXPOSE 80
