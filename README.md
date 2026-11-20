# Reproducible Research: a container approach

## Description
This repository provides a hands-on introduction to reproducible research using modern computational tools. It demonstrates best practices for creating, sharing, and maintaining reproducible scientific workflows, with a focus on Jupyter, VS Code, Docker, and Binder. The included materials guide users through setting up interactive environments, building and running containers, and generating shareable documentation and slides. Whether you are a researcher, educator, or student, this project helps you understand and apply reproducibility principles in your own computational work.  
Key features include:

- Interactive Jupyter and VS Code environments via Docker and Binder
- Step-by-step instructions for building and running containers
- Automated documentation and slide generation
- Examples and templates for reproducible workflows
- Support for collaborative development and sharing

Explore the resources to learn how to make your research transparent, repeatable, and easy to share.


[![GitLab Pages](https://gitrepo.service.rug.nl/dcc/training/computational-reproducibility/badges/main/pipeline.svg?job=pages)](https://gitrepo.service.rug.nl/dcc/training/computational-reproducibility/-/commits/main)

[![GitHub Pages](https://github.com/UG-Team-Data-Science/computational-reproducibility/actions/workflows/pages.yml/badge.svg)](https://ug-team-data-science.github.io/computational-reproducibility/)

## Published slides

### GitHub Pages

- [Workshop slides, January 2026](https://ug-team-data-science.github.io/computational-reproducibility/)

- [Workshop slides, November 2026](https://ug-team-data-science.github.io/computational-reproducibility/slides-november-2026.html)

### GitLab Pages


<a href="https://gitpages.service.rug.nl/dcc/training/computational-reproducibility/">
  <img src="https://user-images.githubusercontent.com/1769619/195922332-4308bb3c-ccfd-47e6-b6a6-f48b94c22fcf.svg" height="18" alt="Quarto Logo"/>
  <span style="font-size:14px; position:relative; top:-3px;">Workshop slides, January 2026</span>
</a>

<br>

<a href="https://gitpages.service.rug.nl/dcc/training/computational-reproducibility/slides-november-2026.html">
  <img src="https://user-images.githubusercontent.com/1769619/195922332-4308bb3c-ccfd-47e6-b6a6-f48b94c22fcf.svg" height="18" alt="Quarto Logo"/>
  <span style="font-size:14px; position:relative; top:-3px;">Workshop slides, November 2026</span>
</a>



## Test the environment in Binder

Binder is a playground environment where you can test the environment and code. All the changes will disappear when the Tabs are closed.

1. Right click on the Binder badge below and then `Open Link in New Tab`

    [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UG-Team-Data-Science/computational-reproducibility/HEAD)

2. When the `Jupyter Lab` interface is displayed, click on the `VS Code` icon.
3. Make some changes in `./docs/quarto/slides.qmd` (optional).
4. Render the `html` slides, open a new terminal and run
    ```bash
    quarto render docs/quarto/slides.qmd
    quarto render docs/quarto/slides-november-2026.qmd
    ```
  The rendered files will be created at:
  - `docs/quarto/slides.html`
  - `docs/quarto/slides-november-2026.html`
5. Render the `pdf` slides (optional), run
    ```bash
  quarto render docs/quarto/slides.qmd --to pdf
    ```
  Then the PDF will be saved next to the source file in `docs/quarto/`.
6. To inspect changes immediately run
    ```bash
  quarto preview docs/quarto/slides.qmd
    ```
  in the pop up `window` click on `Open in browser`. Any changes in the slides will be reflected after refreshing the tab.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

### Build the docker container

```bash
cd docker
docker build -t jupyter-vscode:1.0 .
```

or 

```bash
docker build --network=host -t jupyter-vscode:1.0 .
```

### Run the container

```bash
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan jupyter-vscode:1.0
```

or

```bash
docker run -it --rm \
  -p 8888:8888 \
  --user root \
  -e NB_USER=root \
  -e NB_UID=0 \
  -e NB_GID=0 \
  -v ~/.ssh:/home/jovyan/.ssh:ro \
  -v ~/.gitconfig:/home/jovyan/.gitconfig:ro \
  -v "${PWD}":/home/jovyan/work \
  jupyter-vscode:1.0
```

## Usage

Visit the link provided in the terminal
```bash
...
        http://127.0.0.1:8888/lab?token=9cc59e2fa3b64f29d857332aa41cc5fc3463b8319b513406
```
Click on `VS Code`.

### Build documentation

Open a terminal `Menu->Terminal->New Terminal` and move to the `docs` folder
```bash
  cd docs/quarto
```
Build the html slides
```bash
  quarto render slides.qmd
  quarto render slides-november-2026.qmd
```
Build the pdf slides (make sure you run the above command)
```bash
  quarto render slides.qmd --to pdf
```
Rebuild automatically (useful during continuous file changes)
```bash
  quarto preview slides.qmd
```
and follow the link on the terminal `ctrl + click`

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
In progress
