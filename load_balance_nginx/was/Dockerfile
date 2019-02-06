FROM ibmcom/websphere-traditional:latest
COPY --chown=was:was java_hello_world.ear /work/
COPY --chown=was:was install_app.py /work/config
RUN /work/configure.sh
