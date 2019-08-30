import pytest
from models.item import ItemModel
from models.store import StoreModel
from app import app
from db import db

name = 'string name'
price = 1923.23
store_id = 1

storename = 'Starbuck'


@pytest.fixture(scope='module')
def store():
    return StoreModel(storename)


@pytest.fixture
def item():
    return ItemModel(name, price, store_id)


@pytest.fixture(scope='module')
def get_app_client():
    return app.test_client


@pytest.fixture(scope='module')
def needs_init_app():
    def helper():
        yield True
        while True:
            yield False
    gen = helper()
    return gen


@pytest.fixture(scope='function')
def get_app_context(needs_init_app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    with app.app_context():
        if next(needs_init_app):
            db.init_app(app)
        db.create_all()

    print("-------------setup_app_context---------------")

    yield app.app_context

    with app.app_context():
        db.session.remove()
        db.drop_all()
        print("-------------teardown_app_context---------------")