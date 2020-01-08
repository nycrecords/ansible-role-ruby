import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_ruby_installed(host):
    ruby = host.package("rh-ruby25")

    assert ruby.is_installed


def test_rubygems_installed(host):
    rubygems = host.package("rh-ruby25-rubygems")

    assert rubygems.is_installed


def test_bundler_installed(host):
    bundler = host.package("rh-ruby25-rubygem-bundler")

    assert bundler.is_installed
