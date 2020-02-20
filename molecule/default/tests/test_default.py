import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    # assert f.group == 'root'


def test_www_site1_index_html(host):
    f = host.file('/var/www/site-1/index.html')

    assert f.exists
    assert f.user == 'root'
    # assert f.group == 'root'


def test_www_site1_style_css(host):
    f = host.file('/var/www/site-1/style.css')

    assert f.exists
    assert f.user == 'root'
    # assert f.group == 'root'


def test_www_site1_script_js(host):
    f = host.file('/var/www/site-1/script.js')

    assert f.exists
    assert f.user == 'root'
    # assert f.group == 'root'
