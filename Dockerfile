# Start from a base image with Python + Jupyter
FROM jupyter/scipy-notebook:python-3.11

# Switch to root to install packages
USER root

# Install system dependencies (nodejs, npm, curl for code-server, LaTeX for PDF builds)
RUN apt-get update && apt-get install -y \
    curl \
    git \
    nodejs \
    npm \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    latexmk \
 && rm -rf /var/lib/apt/lists/*

# Install code-server (VS Code in browser)
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Python extension
RUN code-server --install-extension ms-python.python && \
    code-server --install-extension lextudio.restructuredtext && \
    code-server --install-extension trond-snekvik.simple-rst

# Install Jupyter extensions for VS Code integration + Sphinx toolchain
RUN pip install --no-cache-dir \
    jupyter-server-proxy \
    jupyter-vscode-proxy \
    sphinx \
    sphinx-revealjs \
    esbonio

# Expose port for Jupyter
EXPOSE 8888

# Switch back to notebook user
USER $NB_UID

# Start Jupyter Lab (with VS Code available in the UI)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

