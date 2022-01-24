import boto3
import os
import pytest
from moto import mock_s3
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


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        conn = boto3.client("s3", region_name="us-east-1")
        yield conn
