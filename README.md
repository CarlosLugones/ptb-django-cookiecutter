# PTB Django cookiecutter

![PTB Django Cookiecutter](docs/cover.jpg)

> A simple cookiecutter to create Python Telegram bots, wrapped with Django.

Based on:
* [python-telegram-bot (PTB)](https://python-telegram-bot.org)
* [Django](https://djangoproject.com)
* [Cookiecutter](https://cookiecutter.readthedocs.io)

## What's inside

* Django app with `dev` and `prod` environments.
* Model to store bot users data.
* Command to run the bot.
* Admin web interface to see the bot data.
* Authentication mechanism.
* Some example callbacks.
* Small engine to wrap the bot callbacks.
* Ready for deployment using Docker via `docker-compose`.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

    pip install -U cookiecutter

Create your bot using this cookiecutter:

    cookiecutter gh:lugodev/ptb-django-cookiecutter

This will clone the cookiecutter and launch a wizard to help you customize your new bot.

![Installation](docs/terminal0.png)

## Bot structure

Once you have generated your new bot, you will get this folders structure:

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


## Start your bot on dev environment

✨ **Tip (optional):** Create these aliases on on your `.bashrc` or `.zshrc`, like this

    alias poetry="python3 -m poetry"
    alias django="poetry run ./dev.py"
    alias djr="django runserver"
    alias djm="django makemigrations && django migrate"
    alias djmr="djm && djr"

Install the dependencies using [Poetry](https://python-poetry.org):

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    cd src/bot
    poetry install

Place your env vars to the `.env` file (never push the file to the repo):

    SECRET_KEY=your django random secret key
    TELEGRAM_TOKEN=your bot token

Start the bot (using the alias):

    django runbot

Or using Poetry:

    python3 -m poetry run ./dev.py runbot

## Deploy your bot

Clone your repo to the server, and create this folder structure:

* `codebase`: The repo itself, the source code.
* `storage`: The place to store the DB and other persistant files.

Create and fill the `./codebase/.env` file with the environment vars.

Then, deploy, using `docker-compose`:

    cd codebase
    docker-compose up --build -d

## Contribute

* Fork this repo.
* Commit your contributions to a new branch.
* Submit a pull request.

## Bots created with this cookiecutter

None yet. Want to be the first? Submit your bot if it's open source.
