# Browser-first, disposable KiCad CLI development environment.
# Debian Trixie repository provides a stable KiCad generation; do not assume
# this is KiCad 10 until its package version is explicitly verified.
FROM debian:trixie
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git curl bash jq make python3 python3-venv python3-pip \
    python3-pcbnew kicad kicad-cli 2>/dev/null || true
# Avoid guessing that 'kicad-cli' is an independent Debian package:
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git curl bash jq make python3 python3-venv python3-pip \
    kicad && rm -rf /var/lib/apt/lists/*
WORKDIR /workspaces
CMD ["sleep", "infinity"]
