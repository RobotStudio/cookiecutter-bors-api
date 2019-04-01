=====================
Cookiecutter Bors API
=====================

.. image:: https://travis-ci.org/RobotStudio/cookiecutter-bors-api.svg?branch=master
    :target: https://travis-ci.org/RobotStudio/cookiecutter-bors-api

A cookiecutter_ template for creating reusable bors API integrations quickly as
installable apps.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Features
--------

* Sane setup.py for easy PyPI registration/distribution
* Travis-CI configuration
* Codecov configuration
* Tox configuration
* Sphinx Documentation
* BSD licensed by default
* Basic stubs generation

Usage
-----

First, create your empty repo on Github and set up your virtual environment with your favorite method.

**Note**: Your project will be created with README.rst file containing a pypi badge, a travis-ci badge and a link to documentation on readthedocs.io. You don't need to have these accounts set up before using Cookiecutter or cookiecutter-bors-api.

Now, get Cookiecutter_. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter gh:RobotStudio/cookiecutter-bors-api

You'll be prompted for some questions, answer them, then it will create a directory that is your new package.

Let's pretend you want to create a reusable API integration app called "my-api" with an app that can be placed
in ``INSTALLED_APPS`` as "my_api" Rather than have to copy/paste from other people's projects and
then fight enthusiasm-destroying app layout issues like `setup.py` configuration and creating test
harnesses, you get Cookiecutter_ to do all the work.

**Warning**: After this point, change 'Bobby', 'karma0', etc to your own information.

It prompts you for information that it uses to create the app, with defaults in square brackets. Answer them::

    Cloning into 'cookiecutter-bors-api'...
    remote: Counting objects: 49, done.
    remote: Compressing objects: 100% (33/33), done.
    remote: Total 49 (delta 6), reused 48 (delta 5)
    Unpacking objects: 100% (49/49), done.
    full_name [Your full name here]: Bobby
    email [you@example.com]: karma0@gmail.com
    github_username [yourname]: karma0
    project_name [bors-api]: my-api
    repo_name [my_api]:
    app_name [my_api]:
    project_short_description [Your project description goes here]: A sample API integration
    calls [Comma-separated list of API calls]: Scoop, Flavor
    bors_versions [0.3.2],
    version [0.1.0]:
    create_example_project [N]:
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - ISCL
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]:

Enter the project and take a look around::

    $ cd my_api/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:karma0/my_api.git
    $ git push -u origin master

Now take a look at your repo. Awesome, right?

It's time to write the code!!!

Running Tests
~~~~~~~~~~~~~

Code has been written, but does it actually work? Let's find out!

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Setting up Travis
~~~~~~~~~~~~~~~~~

You will need to explicitly activate your repo in your `Travis CI profile`_.
If the repo isn't showing up, run a manual synchronisation.

.. _Travis CI profile: https://travis-ci.org/profile/

Integration with codecov.io
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code coverage is integrated with `Codecov`_. Make sure you have an account
and that you've granted access to your repo. In case of a private repo, you
will need to generate a token and pass it when submitting coverage.

.. _CodeCov: https://codecov.io/

Register on PyPI
~~~~~~~~~~~~~~~~

Once you've got at least a prototype working and tests running, it's time to register the app on PyPI::

    python setup.py register


Releasing on PyPI
~~~~~~~~~~~~~~~~~

Time to release a new version? Easy!

First, use `bumpversion` to up the release number::

    $ pip install bumpversion
    $ bumpversion --current-version VERSION_NUMBER minor --config-file setup.cfg

Where `VERSION_NUMBER` is the current version, e.g. `0.1.0`.

Then run::

    $ python setup.py publish

It will answer with something like::

    You probably want to also tag the version now:
          git tag -a 0.1.0 -m 'version 0.1.0'
          git push --tags

Go ahead and follow those instructions.
