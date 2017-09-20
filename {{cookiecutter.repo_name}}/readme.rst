{{cookiecutter.project_name}}
################################

A `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ (project template) for creating a barebone `stacker <https://github.com/remind101/stacker#stacker>`_ project

Note: You do not have to setup your project this way.

Requirements
============

* Python 2.7 or 3.4+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
=====

1. Generate a ``stacker`` project, following the prompts from the command.

      .. code-block:: bash

          $ cookiecutter gh:remind101/stacker_cookiecutter

This command will create a new stacker project in your present working directory.

Project tree
=================

In this example we have a product called ``{{cookiecutter.repo_name}}`` and two environments called ``dev`` and ``prod``.

Some notes about the files in this tree:

**conf/{{cookiecutter.repo_name}}/<env>.env**:
 This is an "environment" file which holds secrets and tunable variables/parameters.
 The only required key/value in this file is ``namespace``.

**{{cookiecutter.repo_name}}.yaml**:
 This is a "stacker config" file.

**blueprints/touch.py**:
 This is a tiny ``stacker blueprint`` that doesn't do much of anything.
 A blueprint is used to programatically generate CloudFormation JSON.

**tests/blueprints/test_touch.py**:
  This is a tiny ``stacker blueprint`` test.

Running a release
====================

In this example we use a ``Makefile`` to save commands.

To execute stacker on ``{{cookiecutter.repo_name}}`` dev, run::

 make {{cookiecutter.repo_name}} ENV_NAME=dev ARGS=--interactive

To execute stacker on ``{{cookiecutter.repo_name}}`` prod, run::

 make {{cookiecutter.repo_name}} ENV_NAME=prod ARGS=--interactive

