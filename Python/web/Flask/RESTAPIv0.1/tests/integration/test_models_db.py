import pytest
from models.item import ItemModel
import json
from app import app
from db import db


name = 'string name'
# price = 1923.23
#
# @pytest.fixture
# def item():
#     return ItemModel(name, price)


@pytest.fixture(scope='module')
def get_app_client():
    return app.test_client


@pytest.fixture(scope='module')
def get_app_context(request):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    with app.app_context():
        db.init_app(app)
        db.create_all()

    def teardown_db():
        with app.app_context():
            db.session.remove()
            db.drop_all()
        print("-------------teardown_db---------------")
    request.addfinalizer(teardown_db)
    return app.app_context


def test_crud(item, get_app_context):
    with get_app_context():
        assert ItemModel.find_by_name(name) is None
        item.save_to_db()
        assert ItemModel.find_by_name(name) is not None
        item.delete_from_db()
        assert ItemModel.find_by_name(name) is None