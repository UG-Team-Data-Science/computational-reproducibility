===================================
Working with Container Environments
===================================

Running Customized Environments
-------------------------------
.. raw:: html

    <div style="display: flex; justify-content: center; gap: 40px;">
      <img src="https://jupyter-docker-stacks.readthedocs.io/en/latest/_static/jupyter-logo.svg" alt="Container architecture" width="150px"/>
      <img src="https://rocker-project.org/img/rocker.png" width="150px"/>
    </div>

Jupyter stacks
--------------

.. image:: https://raw.githubusercontent.com/jupyter/docker-stacks/refs/heads/main/docs/images/inherit.svg
   :alt: Jupyter stacks dependency tree of the core images.
   :width: 800px
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


Running a container
-------------------

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