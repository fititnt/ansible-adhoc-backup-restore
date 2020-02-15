.. include:: Includes.txt

###########################################
`abr` standards (for extension developers)
###########################################

.. warning::

  This page is a draft.


.. contents:: Table of Contents of APIs

.. raw:: html

  <hr />

*******************************
Common to all `abr` extensions
*******************************

1. **Setup VS Run**: `abr` by default implements an setup step, that always
   run for all running modes, except if the user use `abr_skip_setup: true`
   (or some more specific variable used). Whatever is a driver or an strategy,
   except if is a quick check (like if a file or folder exist on disk) **don't
   repeat what should be on a setup stage on a run stage of your task**. The
   setup step of your extension can be slow (and in fact if a restore fail,
   the user may use `abr_skip_setup: true` to go directly).
2. **Setup steps can be different between types of run**: if you look at `abr`
   source code, while most of the time setup of extensions tend to just have
   an `main.yml` file, it's will only be loaded if the folder does not have
   and `{{ abr_mode }}.yml` file (e.g. `backup.yml`, `restore.yml`,
   `restore-options.yml`, etc. You can use this in your advantage. **But assume
   at one restore can occour on a machine that was not used to generate a
   backup** (e.g. it's a good idea to test at least once this case).

**************
`abr` Drivers
**************

When creating and `abr` driver, assume it's reason to exist is the
**lower level** translation betwen what need to be exported and what later
needs to be imported back to whatever the end user is applying an
`abr_mode: backup` or `abr_mode: restore` run.

The following are expected from an driver:

1. The input and output of a driver must be an single file or an single folder
   acessible by the local filesystem.

      - Whatever is on this single file or single folder it's up to the driver,
        **but it must be able to undestand how to import the single file or
        single folder that was exported**
      - While a driver on `abr_mode: restore` may abort the import before
        starting, try to show relevant error messages by the underlining tool
        used. You don't need to think all possible solutions, things that
        the underlining tools could add options like `--force` ,
        `--ignore-errors` consider implementing on your custom error message
        and explicitly giving the "copy and paste code/command line option"
        to the end user re-run the `abr`

2. Drivers that

*****************
`abr` Strategies
*****************

.. notice::

  Topic is a draft.
