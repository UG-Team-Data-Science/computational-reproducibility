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

+------------------+--------------+----------------+
| Analysis \\ Data | **Same**     | **Different**  |
+==================+==============+================+
| **Same**         | Reproducible | Replicable     |
+------------------+--------------+----------------+
| **Different**    | Robust       | Generalisable  |
+------------------+--------------+----------------+

Spectrum of reproducibility
---------------------------

.. image:: https://book.the-turing-way.org/build/reproducible-definit-bb9a842f3405716bc9ad3f5bd422dfc8.svg
   :alt: The Turing Way's reproducibility definitions
   :width: 800px
   :align: center



Tools for Computational Reproducibility
---------------------------------------
- Version control
- Virtualization
  * **Containerization**
  * Virtual machines
  * Package managers (pip, conda, CRAN, Bioconductor)
- Workflow systems
- Data repositories
- Notebooks and literate programming
- Community standards


Capturing Computational Environments
------------------------------------

.. image:: https://book.the-turing-way.org/build/computational-enviro-40d731cc2965c8bd2ce5e9b2e0f0742d.jpg
   :alt: The Turing Way's capturing computational environments
   :width: 800px
   :align: center

State of the Art
----------------

- Docker
- Singularity/Apptainer
- ReproZip
- Guix
- CodeOcean
- Binder
- ... and many more!


