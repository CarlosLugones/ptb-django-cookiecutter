{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![{{ cookiecutter.project_name }}](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})

[![{{ cookiecutter.project_name }}](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}

> {{ cookiecutter.project_short_description }}

{% if is_open_source %}
# Open source
* License: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

## Features

* TODO

## Start developing your bot 💻

🤖 Welcome to your new bot. You have successfully generated your bot structure using `ptb-django-cookiecutter`.

Before you start creating your bot, you need to understand the bot structure:

* `src/bot`: The bot source code.
    * `core`:
        * `authentication.py`: The authentication mechanism.
        * `callbacks.py`: Your callbacks here.
        * `commands.py`: Your commands here.
        * `constants.py`: Your conversation states, defined as constants.
        * `conversation.py`: Your conversation callbacks.
        * `engine.py`: The bot engine.
        * `messages.py`: The message filter callbacks.
        * `models.py`: Your bot models, defined as Django model classes.
        * `renderers.py`: Methods to render your messages.

## Install your bot dependencies 📦

You have two primary options to install de bot Python dependencies: pip or Poetry. You can also use pipenv, virtualenvwrapper or another package managers. We recommend Poetry.

1. Install dependencies using [Poetry](https://python-poetry.org):

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    cd src/bot
    poetry install

✨ **Tip (optional):** Create these aliases on on your `.bashrc` or `.zshrc`, like this

    alias poetry="python3 -m poetry"
    alias django="poetry run ./dev.py"
    alias djr="django runserver"
    alias djm="django makemigrations && django migrate"
    alias djmr="djm && djr"

2. Or install your dependencies using pip.

    pip3 install -r requirements.txt

## Initialize your bot environment variables

Place your env vars to the `.env` file (never push this file to the repo):

    SECRET_KEY=your django random secret key
    TELEGRAM_TOKEN=your bot token


## Start the bot

Start the bot (using the previously suggested alias, optional):

    django runbot

Or using Poetry:

    python3 -m poetry run ./dev.py runbot

Or using Python:

    python3 dev.py runbot

## Deploy your bot 🚀

Clone your repo to the server, and create this folder structure:

* `codebase`: The repo itself, the source code.
* `storage`: The place to store the DB and other persistant files.

Create and fill the `./codebase/.env` file with the environment vars.

Then, deploy, using `docker-compose`:

    cd codebase
    docker-compose up --build -d

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)  and the [python-telegram-bot (PTB)](https://python-telegram-bot.org) project template.
