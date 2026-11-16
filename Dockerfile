FROM grafana/grafana:latest
ENV GF_SECURITY_ADMIN_USER=admin
ENV GF_SECURITY_ADMIN_PASSWORD=greenleaf_soc
ENV GF_AUTH_ANONYMOUS_ENABLED=true
ENV GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer
COPY dashboards/ /var/lib/grafana/dashboards/
EXPOSE 3000
