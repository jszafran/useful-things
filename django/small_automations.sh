#    Small automations I created while working on my django project.
#
#    1. Activate your app virtual environment quickly
#
#    I use pipenv for managing my app virtual environment.
#    It's convinient to create a script changing directory
#    and activating your virtual environment, for example:

cd /home/kuba/Desktop/w84it/
pipenv shell

#    Later, this can be aliased, for example with your project's name.
#    I added below alias to .bashrc (executed by non-login shells - as
#    that's how I am working with terminal on dev machine. By adding this
#    to mentioned file, you make sure this alias will be set every time
#    you run an instance of terminal on your machine.

alias w84it='/path/to/above/script/'

#    2. Aliasing frequently used commands for Django
#
#    Instead of typing 'python manage.py runserver' every time, it's a good idea
#    to alias such commands. Please find my examples below. You can add them to 
#    .bashrc file as well.

alias drun='python manage.py runserver'
alias dmkm='python manage.py makemigrations '
alias dmg='python manage.py migrate'
alias dshell='python manage.py shell'
alias dtest='python manage.py test'
