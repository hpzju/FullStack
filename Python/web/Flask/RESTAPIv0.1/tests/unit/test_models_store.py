import pytest
from models.store import StoreModel

name = 'Starbuck'

@pytest.fixture
def store():
    return StoreModel(name)


def test_itemmodel_init(store):
    assert name == store.name
