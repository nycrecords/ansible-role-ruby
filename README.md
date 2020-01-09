# Ansible Role: Ruby

![GitHub](https://img.shields.io/github/license/nycrecords/ansible-role-ruby)
[![Build Status](https://travis-ci.com/nycrecords/ansible-role-ruby.svg?branch=master)](https://travis-ci.com/nycrecords/ansible-role-ruby)
[![Galaxy](https://img.shields.io/badge/galaxy-nycrecords.ruby-blue.svg)](https://galaxy.ansible.com/nycrecords/ruby)
![Ansible](https://img.shields.io/ansible/role/d/45716)
![Ansible](https://img.shields.io/ansible/quality/45716)

Installs Ruby and bundler gem on Linux.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    workspace: /root

The location where temporary files will be downloaded in preparation for Ruby installation.

    ruby_install_bundler: true

Whether this role should install [Bundler](http://bundler.io/).

    ruby_install_gems: []

A list of Ruby gems to install (just the name of the gem to be installed). This is meant as a simple convenience, and will only install the latest version of the gem. If you need to install gems with more options or specificity, you can do so elsewhere in your playbook.

    ruby_install_gems_user: username

The user account under which Ruby gems will be installed. Defaults to the `ansible_ssh_user` if not set.

    ruby_install_from_source: false

By default, this role will install whatever version of ruby is available through your system's package manager (`apt` or `yum`). You can install whatever version you like (including the latest release) by setting this to `true` and/or updating the `ruby_download_url` and `ruby_version`.

    ruby_download_url: http://cache.ruby-lang.org/pub/ruby/2.5/ruby-2.4.4.tar.gz

The URL from which Ruby will be downloaded (only used if `ruby_install_from_source` is `true`).

    ruby_version: 2.5.1

The version of ruby that will be installed (only used if `ruby_install_from_source` is `true`).

    ruby_source_configure_command: ./configure --enable-shared

The `configure` command that will be run (only used if `ruby_install_from_source` is `true`).

    ruby_rubygems_package_name: rubygems

The name of the `rubygems` package. Generally, the default should work; but it will be set to `rubygems-integration` automatically on Ubuntu Trusty (14.04).

## Dependencies

None.

## Example Playbook

    - hosts: server
      roles:
        - role: geerlingguy.ruby

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
