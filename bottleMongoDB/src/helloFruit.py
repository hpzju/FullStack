import pymongo
from bottle import route, run, template, post, request


@route('/')
def home_page():
    favorite = ["Apple", "Orange", "Banana", "Peach"]
    return template("./template/homepage_helloFruit.tpl", {'username': "hubert", 'things': favorite})


@post('/favorite_fruit')
def favorite_fruit():
    fruit = request.forms.get('fruit')
    if(fruit == None or fruit == ""):
        fruit = "No Fruit Selected"

    return template("./template/favorite_fruit.tpl", {'fruit': fruit})

    # connnecto to the db on standard port
    # myClient = pymongo.Connection("mongodb://localhost")
    # myDB = myClient["m101"]
    # myCol = myDB["fruits"]
    # myCol.insert({'favorite': ["Apple", "Orange", "Banana", "Peach"]})


run(host='localhost', port=8080)
