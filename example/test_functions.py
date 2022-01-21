"""Please note this file name cannot be changed"""

from models import MyModel, MyObject
import requests

# mock query
def test_sqlalchemy_query_property_get_mock(
        mock_my_model,
        mock_get_sqlalchemy,
):
    # SQLAlchemy returns a list for an "all" query
    mock_get_sqlalchemy.all.return_value = [mock_my_model]
    response = MyModel.query.all()

    assert response == [mock_my_model]


# mock property
def test_mocked_property(mock_object_property):
    test_object = MyObject()
    assert test_object.property == "new_property_value"


# mock model
def test_sqlalchemy_model_mock(mock_my_model):
    my_model = mock_my_model
    assert my_model.id == "my_mock_id"

# mock get request
def test_get_request(requests_mock):
    requests_mock.get('http://test2.com', text='data')
    assert 'data' == requests.get('http://test2.com').text


# mock post request
def test_post_request(requests_mock):
    requests_mock.post(
        "https://api.twitter.com/oauth2/token",
        json={"token_type": "bearer", "access_token": "token"},
    )

    response = requests.post(
        'https://api.twitter.com/oauth2/token',
        data={"grant_type": "client_credentials"},
    )

    assert response.json()['token_type'] == "bearer"
    assert response.json()['access_token'] == "token"
