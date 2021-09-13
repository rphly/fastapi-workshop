import pyrebase

config = {

}

# Temporarily replace quote function


def noquote(s):
    return s


pyrebase.pyrebase.quote = noquote

firebase = pyrebase.initialize_app(config)
db = firebase.database()
