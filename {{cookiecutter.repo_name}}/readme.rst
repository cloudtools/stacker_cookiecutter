{{cookiecutter.project_name}}
####################

A `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ (project template)
for creating a barebone
`stacker <https://github.com/cloudtools/stacker#stacker>`_ project

Note:
 You do not have to setup your project this way, this is just meant as a
 suggestion and some simple guidance to help folks who are new to stacker.

Requirements
============

* Python 2.7 or 3.4+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_
* `poetry <https://poetry.eustace.io/>`_

Usage
=====

1. Generate a ``stacker`` project, following the prompts from the command.

      .. code-block:: bash

          $ cookiecutter gh:cloudtools/stacker_cookiecutter
          project_name [myproject]:
          stacker_bucket [stacker-myproject]:
          repo_name [myproject]:
          description [stacker project for myproject]:

This command will create a new stacker project in your present working
directory. 

Note: You should try to make your ``stacker_bucket`` variable unique
since S3 bucket names share a global namespace. It will default to
``stacker-{{ cookiecutter.project_name }}`` but you may choose any unique value.

Project tree
=================

In this example we have a product called ``{{cookiecutter.repo_name}}`` and two environments
called ``dev`` and ``prod``.

Some notes about the files in this tree:

**conf/<env>.env**:
 This is an "environment" file which holds variables that change in the config
 based on the environment. This allows you to have a single config for all
 your environments, while changing small things per environment.

 See: http://stacker.readthedocs.io/en/latest/environments.html

**stacker.yaml**:
 This is a "stacker config" file.

 See: http://stacker.readthedocs.io/en/latest/config.html

**blueprints/touch.py**:
 This is a tiny ``stacker blueprint`` that doesn't do much of anything.
 A blueprint is used to programatically generate CloudFormation JSON.

 See: http://stacker.readthedocs.io/en/latest/blueprints.html

**tests/blueprints/test_touch.py**:
  This is a tiny ``stacker blueprint`` test which only creates a simple
  resource in CloudFormation (a WaitCondition, which does nothing on it's own).

  See: http://stacker.readthedocs.io/en/latest/blueprints.html#testing-blueprints

Running a release
====================

In this example we use a ``Makefile`` to save commands.  The commands will be
ran using **poetry** which will handle creating a virtualenv for you, as well
as insuring that the correct packages are installed.

To execute stacker using your dev environment, using the *--interactive* flag
run::

 make dev ARGS=--interactive

To execute stacker using the prod environment, run::

 make prod ARGS=--interactive
