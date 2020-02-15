.. include:: Includes.txt

.. Ad-Hoc Backup Restore (abbreviated: abr), released as an very extensible
   Ansible role, allows control the full workflow of backup, storage, and
   restore of anything supported by it's drivers.

################################################
Ad-Hoc Backup Restore ("`abr`") documentation
################################################

.. |image-maturity-technology-preview| image:: https://img.shields.io/badge/Maturity-technology--preview-informational
    :alt: Maturity: Technology Preview

|image-maturity-technology-preview| **Ad-Hoc Backup Restore
(abbreviated: `abr`), released as an very extensible Ansible role, allows
control the full workflow of backup, storage, and restore of anything
supported by it's drivers.**

While it *may* be executed automated (e.g. running via
`Ansible AWX <https://github.com/ansible/awx>`_ the main reason to exist have
an *somewhat standard* workflow to humans do *Ad-Hoc backups* (quick backups)
**OR** *Ad-Hoc restore*.


*************
Installation
*************

If you are new to Ansible, we recommend read our :doc:`installation`. TL;DR:

.. code-block:: bash

  # "a2s is installable as an Ansible role and is distributed over Ansible Galaxy
  ansible-galaxy install fititnt.syntactic_sugar


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   installation
   quickstart
   api
   standards
   todo
   alternatives

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
