import pytest
# Simulating that we are testing DB CRUD operations 

@pytest.fixture(autouse=True, scope='module')
def open_DB():
    print('\nOpenning DB')


def test_insert():
    print('\nInserting ....')


def test_update():
    print('\nUpddating ....')


def test_delete():
    print('\nDeleting ....')

@pytest.fixture(autouse=True, scope='module')
def close_DB():
    yield
    print("\nClosing DB")