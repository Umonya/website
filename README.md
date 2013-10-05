Umonya Website
==============

Getting it up and running
-------------------------

Deploying your own Umonya website is simple. It can be deployed on Heroku with minimal effort. We guide you through this process below. For people familiar with Django: this is a run-of-the-mill Django project. Feel free to deploy it any way you want. Just remember to assign a value to the `SECRET_KEY` production setting (important info [here](#secretkey))

Deploy on Heroku
****************

1. Install the Heroku Toolbelt locally. Heroku has instructions [here][https://toolbelt.herokuapp.com/]. Follow the instructions to the end to set up an SSH key, etc.

2. Clone the Umonya website repo: `git clone git@github.com:Umonya/website.git`.

3. Enter the project directory: `cd website`.

4. Create the new application: `heroku create`.

5. Configure your deployment: `heroku config:set 'DJANGO_SETTINGS_MODULE=website.settings.prod' 'DJANGO_SECRET_KEY=SECRET_KEY'`. Replace `SECRET_KEY` with your own value as specified [here](#secretkey).

6. Upload your application: `git push heroku develop:master`. This might take a while as Heroku deploys the application.

7. Run `heroku run python manage.py syncdb` and create a superuser when prompted. The superuser can be used to manage your site content.

8. Run `heroku run python manage.py migrate`.

9. Run `heroku open` and check out your newly deployed site!

### <a href="#secretkey"></a>Setting `SECRET_KEY` ###
You need to generate a random 50-character secret key to use for your Umonya deployment. After doing that, use it in production by setting an environment variable called `DJANGO_SECRET_KEY`. Step 5 above shows how to do it using the Heroku CLI. Do NOT use `SECRET_KEY` in `website.settings.dev` since it is visible to the public. It it only there for dev convenience.
