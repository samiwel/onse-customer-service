def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(customer, customer_repository):
    customer_repository.store(customer)


def update_customer(customer_id, first_name, surname, customer_repository):
    updated_customer = customer_repository.fetch_by_id(customer_id)
    updated_customer.first_name = first_name
    updated_customer.surname = surname
    customer_repository.store(updated_customer)
