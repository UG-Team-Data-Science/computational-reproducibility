====
Goal
====
Computational reproducibility means that research results obtained through computation can be consistently **re-produced** by others  given the same inputs and methods. 


The Pillars
-----------
- Code
- Data
- **Environment**
- Documentation
- Workflows

The Challenges
--------------

- Software rot
- Data availability
- Complexity
- Human factors


Benefits of Computational Reproducibility
-----------------------------------------

1. Integrity and Trust
2. **Efficiency and Reuse**
3. Collaboration and Transparency
4. `Long-term` Preservation
5. Scalability and Generalization
6. Policy and Funding Compliance


Spectrum of reproducibility
---------------------------


.. image:: /_static/images/reproducible-matrix.jpg
   :alt: Reproducibility matrix
   :width: 800px
   :align: center
   :target: https://book.the-turing-way.org/reproducible-research/overview/overview-definitions/#rr-overview-definitions-reproducibility

Tools for Computational Reproducibility
---------------------------------------
- Version control
- Virtualization 
    - **Containerization**
    - Virtual machines
    - Package managers (pip, conda, CRAN, Bioconductor)
- Workflow systems
- Data repositories
- Notebooks and literate programming
- Community standards


Capturing Computational Environments
------------------------------------

.. image:: /_static/images/computational-enviro.png
   :alt: The Turing Way's capturing computational environments
   :width: 800px
   :align: center
   :target: https://book.the-turing-way.org/reproducible-research/renv/renv-options/

Why docker containers?
----------------------

CON:

**Costs time**

PRO:

**Can saeve you time**

State of the Art
----------------

- Docker
- Singularity/Apptainer
- ReproZip
- Guix
- CodeOcean
- Binder
- ... and many more!


