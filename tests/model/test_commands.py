from unittest.mock import MagicMock

import pytest

from customer_service.model import commands
from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_get_customer_when_customer_does_not_exist(customer_repository):
    with pytest.raises(CustomerNotFound):
        commands.get_customer(customer_id=99999,
                              customer_repository=customer_repository)


def test_get_customer(customer_repository):
    customer = Customer(customer_id=1234, first_name='Gene', surname='Kim')
    customer_repository.store(customer)

    result = commands.get_customer(customer_id=1234,
                                   customer_repository=customer_repository)

    assert result is customer


def test_create_customer(customer_repository):
    customer = Customer(first_name='Nicole', surname='Forsgren')

    commands.create_customer(customer=customer,
                             customer_repository=customer_repository)

    stored_customer = customer_repository.fetch_by_id(customer.customer_id)

    assert stored_customer.first_name == 'Nicole'
    assert stored_customer.surname == 'Forsgren'


def test_update_customer_name(customer_repository):

    mock_fetch_by_id = MagicMock()
    mock_fetch_by_id.return_value = Customer(customer_id=5,
                                             first_name="Susan",
                                             surname="Davies")

    customer_repository.fetch_by_id = mock_fetch_by_id

    mock_store = MagicMock()
    customer_repository.store = mock_store

    commands.update_customer(customer_id=5,
                             first_name="Bob",
                             surname="Jones",
                             customer_repository=customer_repository)

    mock_fetch_by_id.assert_called_once_with(5)

    store_argument = mock_store.call_args_list[0][0][0]
    assert store_argument.first_name == "Bob"
    assert store_argument.surname == "Jones"
