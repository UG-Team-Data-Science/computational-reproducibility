=========================================
Containers in action
=========================================

Containers, key concepts
------------------------
+-------------------------------+-------------------------------+
| - **Images**                  | - **Volumes**                 |
| - **Containers**              | - **Registries**              |
| - **Dockerfile**              | - **Docker Hub**              |
| - **Ports**                   | - **Networking**              |
| - **etc.**                    | - **Docker daemon**           |
+-------------------------------+-------------------------------+


How to run the visualizations?
------------------------------

.. raw:: html

        <iframe src="https://clauswilke.com/dataviz/" width="100%" height="600px"></iframe>

Running containers in Binder
----------------------------

|rug_binder| |mybinder|

.. |rug_binder| image:: https://img.shields.io/badge/launch%20-rug%20binder-009CEF?logo=jupyter
   :target: https://binderhub.app.rug.nl/v2/gh/Venustiano/datavizclaus/HEAD
   :alt: Launch RUG Binder



.. |mybinder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/Venustiano/datavizclaus/HEAD?urlpath=lab
   :alt: Launch MyBinder

`Right click` on a badge + `Open link in new tab`

The Binder Workflow
--------------------

.. image:: https://book.the-turing-way.org/build/binder-comic-a9582f496f3175d3eb22028a3db29507.png
   :alt: The Turing Way's reproducibility definitions
   :width: 800px
   :align: center

The BinderHub architecture
--------------------------

.. image:: https://book.the-turing-way.org/build/binderhub-d184fb6c57b53b18920764dc08dc5791.svg
   :alt: The Turing Way's reproducibility definitions
   :width: 800px
   :align: center

Container architecture
----------------------

.. raw:: html

    <div style="display: flex; justify-content: center; gap: 40px;">
      <img src="https://www.docker.com/app/uploads/2021/11/container-what-is-container-1110x961.png" alt="Container architecture" width="500px"/>
      <img src="https://www.docker.com/app/uploads/2021/11/Docker-Website-2018-Diagrams-071918-V5_26_Docker-today-1110x919.png" alt="Cross Platform Containers" width="500px"/>
    </div>


Container Lifecycle
-------------------
.. image:: https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgevspybo00m3a7l4hfrz.png
   :alt: Docker Container Lifecycle
   :width: 800px
   :align: center