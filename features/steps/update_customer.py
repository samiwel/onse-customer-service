from behave import when


@when('I update customer with ID "{customer_id}" with name "{name}"')
def update_customer(context, customer_id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.put(
        f'/customers/{customer_id}',
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 200, f"got {response.status_code}"
    context.name = ' '.join([
        response.get_json()['firstName'],
        response.get_json()['surname']]
    )
