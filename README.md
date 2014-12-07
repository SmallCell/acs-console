# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application support the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Virtualenv
```
$ . bin/activate
$ pip install -r requirements.txt --allow-all-external
$ foreman start wbe
```
http://0.0.0.0:5000

```
$ heroku run python manage.py shell
$ heroku run bash
```

## Database

### Local PSQL
```
createuser -P -s -e vlad
alter user vlad with password 'Omc3';
export DATABASE_URL=postgres://vlad:Omc3@localhost/python_getting_started
```

### Heroku PG
```
https://docs.djangoproject.com/en/dev/ref/settings/#databases
PGUSER=postgres PGPASSWORD=password heroku pg:pull HEROKU_POSTGRESQL_MAGENTA mylocaldb --app sushi
```

## Deploying to Heroku

```sh
$ heroku login # lib.aca55a@gmail.com / jasha123
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

```sh
$ heroku ps:scale web=1
```

## Manage releases
heroku releases
heroku releases:rollback v10

### Propagate
heroku pg:psql
psql -h localhost

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

heroku create                                                                                                                                  vlad@django
Creating rocky-wildwood-1445... done, stack is cedar
https://rocky-wildwood-1445.herokuapp.com/ | git@heroku.com:rocky-wildwood-1445.git
Git remote heroku added

### Emacs
C-c C-f (elpy-find-file)
M-x elpy-set-project-root
C-c C-c (elpy-shell-send-region-or-buffer)
C-M-x (python-shell-send-defun)
C-c C-v (elpy-check)
C-c C-d (elpy-doc)
C-c C-t (elpy-test)
C-c C-r (elpy-refactor)
M-TAB (elpy-company-backend)
  M-n and M-p, C-d, C-w
