# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:K0b!e741@SQLALCHEMY_DATABASE_URI = flasktest.ci6o13prk84i.eu-central-1.rds.amazonaws.com:3306/flaskapp'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'i0P0D0US85emyqhIt2m6rl9bfeHqM+HWVv2ajMaB'
