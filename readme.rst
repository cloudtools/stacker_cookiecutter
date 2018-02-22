stacker_cookiecutter
####################

A `Cookiecutter`_ (project template) for creating a barebone
`stacker`_ project

Note:
 You do not have to setup your project this way, this is just meant as a
 suggestion and some simple guidance to help folks who are new to stacker.

Requirements
============

* Python 2.7 or 3.4+
* `cookiecutter`_
* `stacker`_

Usage
=====

1. Generate a ``stacker`` project, following the prompts from the command.

      .. code-block:: bash

          $ cookiecutter gh:remind101/stacker_cookiecutter
          project_name [myproject]:
          stacker_bucket [stacker-myproject]:
          repo_name [myproject]:
          description [stacker project for myproject]:

This command will create a new stacker project in your present working
directory. Note: You should try to make sure that your *stacker_bucket*
variable is something unique, since s3 buckets share a global namespace.  It
will default to *stacker-${project_name}* but you can name it whatever you
like, so long as it's unique.

Project tree
=================

In this example we have a product called ``myproduct`` and two environments
called ``dev`` and ``prod``.

Some notes about the files in this tree:

**conf/<env>.env**:
 This is an "environment" file which holds variables that change in the config
 based on the environment. This allows you to have a single config for all
 your environments, while changing small things per environment.

 See: `Environments`_

**stacker.yaml**:
 This is a "stacker config" file.

 See: `Stacker Configuration`_

**blueprints/touch.py**:
 This is a tiny ``stacker blueprint`` that doesn't do much of anything.
 A blueprint is used to programatically generate CloudFormation JSON.

 See: `Blueprints`_

**tests/blueprints/test_touch.py**:
  This is a tiny ``stacker blueprint`` test which only creates a simple
  resource in cloudformation (a WaitCondition, which does nothing on its own).

  See: `Testing Blueprints`_

Running a release
====================

In this example we use a ``Makefile`` to save commands.

To execute stacker using your dev environment, using the *--interactive* flag
run::

 make dev ARGS=--interactive

To execute stacker using the prod environment, run::

 make prod ARGS=--interactive

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`cookiecutter`: https://cookiecutter.readthedocs.io/en/latest/installation.html
.. _`stacker`: https://github.com/remind101/stacker#stacker
.. _`Environments`: http://stacker.readthedocs.io/en/latest/environments.html
.. _`Stacker Configuration`: http://stacker.readthedocs.io/en/latest/config.html
.. _`Blueprints`: http://stacker.readthedocs.io/en/latest/blueprints.html
.. _`Testing Blueprints`: http://stacker.readthedocs.io/en/latest/blueprints.html#testing-blueprints
