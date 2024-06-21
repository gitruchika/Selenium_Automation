import pytest
from resource_data.test_data import *
db_user = 'admin@123'
db_password = 'P@ssw0rd'

@pytest.mark.parametrize("username, password", [
    ('user1@gmail.com', "Admin@123"),
    ('admin@123', "P@ssw0rd"),
    ('admin@123', "P@ssword123"),
    ('testadmin', "P@ssword"),
])
def test_login(username, password):
    if username == db_user and password == db_password:
        print("login successful")
    else:
        pytest.fail("Invalid login credentials")


@pytest.mark.parametrize("username, password", login_parameters)
def test_login_new(username, password):
    if username == db_user and password == db_password:
        print("login successful")
    else:
        pytest.fail("Invalid login credentials")
