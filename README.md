# `abr`Ad-Hoc Backup Restore with Ansible
**Ad-Hoc Backup Restore (abbreviated: `abr`), released as an very extensible
Ansible role, allows control the full workflow of backup, storage, and restore
of anything supported by it's drivers.**

While it _may_ be executed automated (e.g. running via [Ansible AWX](https://github.com/ansible/awx)) the main reason to exist have an _somewhat standard_ workflow to humans do
_Ad-Hoc backups_ (quick backups) **OR** _Ad-Hoc restore_.

## Usage

Visite the complete official documentation at <https://ansible-adhoc-backup-restore.readthedocs.io/>

### Quickstart

```bash
# Too long didn't read:
# "abr is installable as an Ansible role and is distributed over Ansible Galaxy
ansible-galaxy install fititnt.adhoc_backup_restore
```

<!--

**Ansible Role to performn Ad Hoc backup/restore for MariaDB/MySQL/Galera Cluster.
Uses [mydumper/myloader](https://github.com/maxbube/mydumper) for performance
otimized export/import of COMPLETE server and optimal send/receive using
[rclone](https://rclone.org/).**

Note: this role is otimized for Ad Hoc (e.g. executed with human intervention)
instead of automated cron backups.

-->

<!--
Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Public Domain

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

-->