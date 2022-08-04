## keycloack experiments 

## Description
this is an experiment of keycloak behind nginx as reverse roxy


## Environment var 

### keycloak
- virtual_host: indicate the domain name (or subdomain name) that keycloak will be accessible through (VIRTUAL_HOST=auth.example.com)


- LETSENCRYPT_HOST contains the same value as VIRTUAL_HOST and indicates to acme-compagnon to ask for SSL certificate for this domain (or subdomain ) to Let’s encrypt


- LETSENCRYPT_EMAIL contains a valid email address required by let’s encrypt servers to issue an SSL certificate for our domain and to send notifications when the SSL certificate will be expired.


- PROXY_ADDRESS_FORWARDING is set to true when we run keycloak behind a reverse proxy. Without this variable set to true, we can’t log in to our keycloak server. (TO VALIDATE NOT SURE)

## network 
We use the Nginx-proxy container as a reverse proxy and it required all containers to be connected to a unique network so that it can easily handle traffic to them.

## Source 

[base guide](https://www.linkedin.com/pulse/how-deploy-sso-keycloak-linux-server-docker-compose-ssl-temfack)