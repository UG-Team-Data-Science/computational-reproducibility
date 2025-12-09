# Code Server Docker Compose Setup

This directory contains a Docker Compose configuration for running Code Server (VS Code in a browser) with a custom development environment. This setup is designed to provide a complete development environment for creating workshop slides using Quarto (located in `../docs/quarto/slides.qmd`).

## Prerequisites

- Docker
- Docker Compose
- Bash shell

## Building and Running the Service

### 1. Build the Docker Image

Navigate to the `compose` directory and build the custom image:

```bash
cd compose
docker compose build
```

**Optional:** Specify a custom Quarto version during build:

```bash
docker compose build --build-arg QUARTO_VERSION=1.9.0
```

The default Quarto version is `1.8.26`.

### 2. Start the Service

Run the service in the foreground (recommended for first-time setup to see logs):

```bash
docker compose up
```

Or run in the background (detached mode):

```bash
docker compose up -d
```

### 3. Stop the Service

To stop the running service:

```bash
docker compose down
```

## Accessing the Service

Once the service is running, access Code Server at:

```
https://localhost:8443
```

**Note:** You may see a security warning about the SSL certificate. This is expected with the default self-signed certificate. You can safely proceed by accepting the certificate in your browser.

## Configuration

### Environment Variables

- `PUID=1000`: User ID for container processes
- `PGID=1000`: Group ID for container processes
- `TZ=Etc/UTC`: Timezone for the container
- `QUARTO_VERSION`: Quarto version to install (default: 1.8.26)

### Volumes

The following paths are mounted in the container:

| Host Path | Container Path | Mode | Purpose |
|-----------|-----------------|------|---------|
| `.config` | `/config` | read-write | Code Server configuration |
| `~/.ssh` | `/config/.ssh` | read-only | SSH keys for git operations |
| `../` | `/config/workspace` | read-write | Workspace files |

### Port

- **8443**: HTTPS port for accessing Code Server

## Restart Policy

The service is configured with `restart: unless-stopped`, meaning:
- The container will automatically restart if it crashes
- The container will NOT automatically restart after a Docker daemon restart

To change this behavior, modify the `restart` policy in `compose.yml`:
- `no`: Do not automatically restart
- `always`: Always restart
- `on-failure`: Restart only on failure
- `unless-stopped`: Always restart unless explicitly stopped (default)

## Logs

To view the service logs:

```bash
# View recent logs
docker compose logs

# Follow logs in real-time
docker compose logs -f

# View logs for a specific service
docker compose logs code-server
```

## Troubleshooting

### Port Already in Use

If port 8443 is already in use, modify the port mapping in `compose.yml`:

```yaml
ports:
  - 8444:8443  # Map to a different port
```

Then access Code Server at `https://localhost:8444`.

### SSH Keys Not Available

Ensure your SSH keys are in `~/.ssh` directory. The compose configuration mounts them as read-only to support git operations:

```bash
ls ~/.ssh
```

### Container Exits Immediately

Check the build logs:

```bash
docker compose build --no-cache
docker compose up
```

## Build Details

The custom Docker image is built using:
- **Dockerfile:** `Dockerfile.code-server`
- **Context:** Current directory (compose)
- **Base Image:** Defined in `Dockerfile.code-server`
- **Quarto:** Installed with version specified by `QUARTO_VERSION`

The image includes all necessary tools and extensions for development with Code Server, including Quarto support.

## Dockerfile.code-server Overview

The `Dockerfile.code-server` builds a custom development environment with the following components:

### Base Image
- **linuxserver/code-server:latest** - Latest Code Server image with proper VS Code integration

### Installed Tools and Libraries
- **Base utilities:** wget, curl, ca-certificates, gnupg2, software-properties-common
- **Build tools:** build-essential, libssl-dev, libxml2-dev, libcurl4-openssl-dev
- **R environment:** R base and R development packages from CRAN
- **Quarto CLI:** Publishing system for technical documents (version configurable via `QUARTO_VERSION` build argument)
- **R packages:** reticulate (for Python-R integration)

### VS Code Extensions
- Extensions are automatically installed via the `extensions.sh` script during container startup
- This allows for a consistent IDE setup across all development sessions

### Key Features
- **Architecture-aware:** Automatically detects and installs the correct Quarto binary for your system (amd64 or arm64)
- **Marketplace integration:** Configured with Microsoft's official VS Code Marketplace for extension management
- **R and Python support:** Full support for both R and Python development with proper integration
- **Optimized:** Minimized image size by cleaning up apt caches

This environment is specifically configured for creating and previewing Quarto-based workshop slides located at `../docs/quarto/slides.qmd`. You can:
- Edit slides in VS Code
- Use Quarto to preview and render presentations
- Leverage R and Python code within slides
- Maintain full version control with git

## Docker Compose File Location

Configuration file: `compose.yml`

## Additional Commands

Check service status:

```bash
docker compose ps
```

Execute commands inside the container:

```bash
docker compose exec code-server bash
```

Remove all containers and volumes:

```bash
docker compose down -v
```

## Notes

- The workspace directory (`../`) is mounted at `/config/workspace` inside the container
- Changes made in the editor are persisted to your host filesystem
- SSH configuration is read-only to prevent accidental modifications
- Configuration data is stored in `.config` directory
