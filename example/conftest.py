import pytest
from models import MyModel


@pytest.fixture
def mock_object_property(mocker):
    mock = mocker.patch(
        "test_functions.MyObject.property",
        new_callable=mocker.PropertyMock,
        return_value="new_property_value"
    )
    return mock


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


@pytest.fixture
def mock_my_model():
    my_model = MyModel(
        id="my_mock_id",
    )
    return my_model
