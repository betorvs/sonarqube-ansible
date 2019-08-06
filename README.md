Role Name
=========

TravisCI: [![Build Status](https://travis-ci.org/betorvs/sonarqube-ansible.svg?branch=master)](https://travis-ci.org/betorvs/sonarqube-ansible)

Install Sonarqube Server without database. 

Requirements
------------

This ansible role doesn't install database. Please, use an Cloud Postgresql service for this. Sonarqube needs access to a database called: `sonarqube`.


Role Variables
--------------

There are these variables:
- sonar_url: URL to download sonarqube.
- sonar_dir: sonarqube name for the directory and used for file name too.
- sonar_username: sonarqube username.
- sonar_version: Sonarqube version.
- sonar_dbuser: Database user for sonarqube.
- sonar_dbpass: Database password.
- sonar_dburl: Database postgresql URL.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: sonarqube-ansible }


Postgresql azure:
-----------------

Example of creation of database on Azure Postgresql service:

```sh
$ psql --host=POSTGRESQL.postgres.database.azure.com --username="sonaradmin@POSTGRESQL" --dbname="postgres" -W
postgres=> CREATE database sonarqube;
```



License
-------

MIT

Author Information
------------------

Roberto Scudeller beto.rvs@gmail.com


Reference 
---------

https://blog.travis-ci.com/2017-11-30-testing-ansible-roles-using-docker-on-travis

