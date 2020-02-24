# `abr`Ad-Hoc Backup Restore with Ansible
**Ad-Hoc Backup Restore (abbreviated: `abr`), released as an very extensible
Ansible role, allows control the full workflow of backup, storage, and restore
of anything supported by it's drivers.**

While it _may_ be executed automated (e.g. running via [Ansible AWX](https://github.com/ansible/awx)) the main reason to exist have an standard workflow to humans do _Ad-Hoc backups_ (quick backups)
**OR** _Ad-Hoc restore_ <sup>(optional default
`full-temp-backup-before-restore`)</sup> and may be as simple as rename
`abr_mode: "backup"` to `abr_mode: "restore"`.

While by default the _control node_ will use as `abr_bucket` a local folder
`/var/local/abr/bucket/`, you are encoraged to store your backups on a remote
server (even some just with FTP account).  **Since we use <https://rclone.org/>,
ABR out-of-the-box support Google Drive, Amazon Drive, S3, Dropbox,
Backblaze B2, One Drive, Swift, Hubic, Cloudfiles, Google Cloud Storage,
Yandex Files and more!** The use of custom `abr_prefix` to organize
the subfolders where the data will be is recommended.

ABR try to keep it's internal steps somewhat standard to make easier you to edit
or create intermediate transformatons.

<!--
Some features and optionated design decisions:

1. While out of the box uses `/var/local/abr/bucket/` as `abr_bucket`, the way
   it mean to be used is storing on a remote storage. **You can define any
   custom server to store via FTP or SSH, but also popular storages, like
   Google Drive, Amazon Drive, S3, Dropbox, Backblaze B2, One Drive, Swift,
   Hubic, Cloudfiles, Google Cloud Storage & Yandex Files!** Check
   <https://rclone.org/>
2. ABR is **optimized for human Ad-Hoc usage**, with difference from backup to
  restore **may** be as simple as renaming `abr_mode: "backup"` to
   `abr_mode: "restore"` and internal steps designed in a pipeline-like
   workflow.
   1. Some steps may be less computer efficient (in special need of **temporary
      storage**) than the equivalent without ABR. This design decision on
      plugins may help new people create custom extensions with less chance to
      break.
   2. We don't provide cron-like backups, if you really want, can use
     [Ansible AWX](https://github.com/ansible/awx)).
3. Out-of-the-box all drivers support a feature called
   `full-temp-backup-before-restore` when `abr_paranoid: true`. If you servers
   are faster enough and have extra storage, you may like leave it enabled.
-->

<!--

-->


## Usage

Visit the complete official documentation at
<https://ansible-adhoc-backup-restore.readthedocs.io/>.

### TL;DR
If you already know Ansible the _"3 files to quick look"_ are
[defaults/main.yml](defaults/main.yml),
[tasks/mode-backup.yml](tasks/mode-backup.yml) and
[tasks/mode-restore.yml](tasks/mode-restore.yml).

To install:

```bash
# Too long didn't read:
# "abr is installable as an Ansible role and is distributed over Ansible Galaxy
ansible-galaxy install fititnt.adhoc_backup_restore
```

#### How extensible is ABR?
90%+ of it's files can be replaced without need to fork the repository. Files
under `{{ playbook_dir }}/overrides/roles/adhoc_backup_restore/` will have
higher priority. It's both usefull to customize a single file or create your
custom strategies.

### Example

```yaml
# ansible -i myihost.com, backup-directory-site-1.yml
- name: "Converge: backup fs-directory"
  hosts: all
  remote_user: root
  vars:
    # backup? restore? restore-options?
    abr_mode: backup

    # Where will the backup/restore be saved?
    # abr_bucket: ... # 20+ options, check https://rclone.org/
    abr_prefix: "www-site-1/"

    abr_driver: "fs-directory"
    abr_fs_path: "/var/www/site-1/"

    abr_strategy_compression: "targz-default"
    abr_strategy_encryption: "base64-default"

    abr_timestamped: false
  roles:
    - role: ansible-adhoc-backup-restore
```

(...)

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