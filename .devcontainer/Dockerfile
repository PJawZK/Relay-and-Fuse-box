# Disposable, browser-first tool environment. KiCad version derives from
# Debian Trixie and must be printed/validated before use.
FROM debian:trixie
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git curl bash jq make python3 python3-venv python3-pip \
    kicad && rm -rf /var/lib/apt/lists/*
WORKDIR /workspaces
CMD ["sleep", "infinity"]
