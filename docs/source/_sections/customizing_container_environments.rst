===================================
Working with Container Environments
===================================



Running Customized Environments
-------------------------------

|
|

.. raw:: html

    <div style="display: flex; justify-content: center; gap: 40px;">
      <img src="https://jupyter-docker-stacks.readthedocs.io/en/latest/_static/jupyter-logo.svg" alt="Container architecture" width="150px"/>
      <img src="https://rocker-project.org/img/rocker.png" width="150px"/>
    </div>

Jupyter stacks
--------------

.. image:: https://raw.githubusercontent.com/jupyter/docker-stacks/refs/heads/main/docs/images/inherit.svg
   :alt: Jupyter stacks dependency tree of the core images.
   :width: 900px
   :align: center

Running a container
-------------------

|

.. code-block:: python


    docker run -it -p 8888:8888 quay.io/jupyter/scipy-notebook:2025-03-14

    # Entered start.sh with args: jupyter lab

    # ...

    #     To access the server, open this file in a browser:
    #         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
    #     Or copy and paste one of these URLs:
    #         http://eca4aa01751c:8888/lab?token=d4ac9278f5f5388e88097a3a8ebbe9401be206cfa0b83099
    #         http://127.0.0.1:8888/lab?token=d4ac9278f5f5388e88097a3a8ebbe9401be206cfa0b83099


100 numpy exercises
-------------------

1. Once in JupyterLab, open a terminal and run:

    .. code-block:: python

       cd work 

       git clone https://github.com/rougier/numpy-100.git

       pip install mdutils

2. Double-click on ``100_numpy_exercises.ipynb`` to open the notebook.
3. Have some fun!
4. On the menu `File` click on `Shut Down` to stop the server.


Understanding the command
-------------------------

|

.. code-block:: python
     
    docker run -it -p 8888:8888 quay.io/jupyter/scipy-notebook:2025-03-14
       |    |   |   |               |         |                    |
       |    |   |   |               |         |                    └── Version tag
       |    |   |   |               |         └── Image name from Jupyter
       |    |   |   |               └── Registry (Quay.io)
       |    |   |   └── Port mapping (host:container)
       |    |   └── Interactive terminal
       |    └── Run a container
       └── Docker command


Port mapping
------------

.. image:: https://k21academy.com/wp-content/uploads/2020/11/portmapping.drawio.png
   :alt: Understanding port mapping
   :align: center
   :target: https://k21academy.com/docker-kubernetes/docker-container-lifecycle-management/

Docker image search
-------------------

`Docker Hub web interface <https://hub.docker.com/search?q=jupyter>`_ : best practices 🔍

1. **Check Image Source**
   
   - Prefer official images
   - Verify trusted publishers

2. **Version Control**
   
   - Always use specific tags
   - Avoid `latest` tag for reproducibility



Restarting or removing a container
----------------------------------

|

.. code-block:: python

    # list containers
    docker ps --all
    # CONTAINER ID   IMAGE                                       COMMAND                  CREATED              STATUS                     PORTS     NAMES
    # eca4aa01751c   quay.io/jupyter/scipy-notebook:2025-03-14   "tini -g -- start-no…"   About a minute ago   Exited (0) 5 seconds ago             silly_panini

    # start the stopped container
    docker start --attach -i eca4aa01751c
    # Entered start.sh with args: jupyter lab
    # ...

    # remove the stopped container
    docker rm eca4aa01751c
    # eca4aa01751c

Persistent storage
------------------

.. image:: https://iamachs.com/images/posts/docker/part-5-understanding-docker-storage-and-volumes/docker-storage.png
   :alt: Persistent storage with Docker volumes
   :width: 500px
   :align: center
   :target: https://iamachs.com/blog/docker/part-5-understanding-docker-storage-and-volumes/

Persistent storage
------------------

.. image:: /_static/images/ChatGPT_Image_Oct_27_2025_10_37_27_PM.png
   :alt: ChatGPT Screenshot
   :width: 600px


*Image credit: OpenAI ChatGPT*

What are Bind Mounts?
---------------------
- Bind mounts map a file or directory from the host into a container.
- Changes on the host are reflected in the container and vice versa.

How Bind Mounts Work?
---------------------
- Specify a host path and a container path.
- Docker mounts the host path into the container at runtime.
