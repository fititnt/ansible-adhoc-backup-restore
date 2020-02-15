.. include:: Includes.txt

#################################
`abr` Ad-Hoc Backup Restore APIs
#################################

.. warning::

  `abr` still an Technology Preview. Releases before v1.0.0 may have small
  incompatibilities that may require, at least, you rename your variables.


.. contents:: Table of Contents of APIs

.. raw:: html

  <hr />

.. _ref-standard-apis:

**************
`abr_mode`
**************

When running `abr` it alwas have one mode enabled. By default it is
`abr_mode: restore-options`.

`backup`
=========

Source code: `tasks/mode-backup.yml <https://github.com/fititnt/ansible-adhoc-backup-restore/blob/master/tasks/mode-backup.yml>`_

`restore`
=========

Source code: `tasks/mode-restore.yml <https://github.com/fititnt/ansible-adhoc-backup-restore/blob/master/tasks/mode-restore.yml>`_

`restore-options`
=================


Source code: `tasks/mode-restore-options.yml <https://github.com/fititnt/ansible-adhoc-backup-restore/blob/master/tasks/mode-restore-options.yml>`_

**************
`abr_driver`
**************

.. tip::

  "`abr` drivers" is what `abr` uses to, when on `abr_mode: backup` convert
  your information to something it can undestand (like export a database to
  one or more files on disk), and when on on `abr_mode: restore` it convert
  back whatever you was backuping before (like a database restore).

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/copy/main.yml>

Database: MariaDB, Oracle MySQL, Percona, Galera Cluster
=========================================================

`mariadb-mydumper`
-------------------

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/copy/main.yml>

`abr_crons`
===========

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/cron/main.yml>

`abr_directories`
=================
