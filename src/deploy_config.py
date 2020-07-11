from sqlalchemy import false

# SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.dd'
SQLALCHEMY_DATABASE_URI = 'postgres://saspjteooejvzy:88d28e7e1183f84d651c5592cea2383a0113d4c5b0c8f3175eefb25fb4a18465' \
                          '@ec2-18-211-48-247.compute-1.amazonaws.com:5432/dfb47qre2auqtp '
SQLALCHEMY_TRACK_MODIFICATIONS = false
SECRET_KEY = 'THIS_IS_SECRET'

# heroku addons:create heroku-postgresql:hobby-dev --app flasktutorialjoao
# heroku config --app flasktutorialjoao