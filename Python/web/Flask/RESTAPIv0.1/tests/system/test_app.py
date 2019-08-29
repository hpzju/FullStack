import pytest
from app import app
from db import db


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

    request.addfinalizer(teardown_db)

    return app.app_context
