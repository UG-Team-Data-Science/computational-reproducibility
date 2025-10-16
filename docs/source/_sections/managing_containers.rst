====================
Containers in Action
====================

Running Containers
------------------


.. revealjs-section::
   :data-auto-animate:

.. code-block:: console
   :linenos:

   docker run hello-world

.. revealjs-break::
   :data-auto-animate:

.. code-block:: text
   :linenos:

   docker run hello-world

   Hello from Docker!

    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:
    1. The Docker client contacted the Docker daemon.
    ...
    4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
    ...
    For more examples and ideas, visit:
    https://docs.docker.com/get-started/


Listing Containers and Images
-----------------------------

|
.. code-block:: python

   docker ps            # List running containers


   docker ps -a         # List all containers (including stopped)
   
   
   docker images        # List all images


Having fun with Containers
--------------------------

|

.. code-block:: python

   docker run -it debian bash                # Start an interactive bash session

   apt update                                # Update package lists

   apt install -y cowsay fortune             # Install cowsay and fortune

   /usr/games/fortune | /usr/games/cowsay    # Enjoy!


Inspecting Your Docker Environment
----------------------------------

|
Open a second terminal and run the following commands:


.. code-block:: python

   docker ps            # List running containers


   docker ps -a         # List all containers (including stopped)
   
   
   docker images        # List all images


Stopping Containers
-------------------

|

.. code-block:: python
      
      docker ps                     # List running containers

      docker stop <container_id>    # Stop a running container

      docker stop <container_name>  # Stop a running container

      docker ps                     # Verify the container has stopped



Container registry
------------------

.. image:: https://media.geeksforgeeks.org/wp-content/uploads/20240513153832/Docker-hub-registry-768.webp
   :alt: Container registry
   :width: 800px
   :align: center

