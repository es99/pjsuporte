import boto3


def retornaItems(client, table_name, attribute_name):
    emails = []
    response = client.scan(
        TableName = table_name,
        FilterExpression = f'attribute_exists({attribute_name})',
        ProjectionExpression = attribute_name
    )
    attribute_values = [item[attribute_name] for item in response['Items']]
    lista_emails_tmp = [email['S'] for email in attribute_values]
    for email in lista_emails_tmp:
        if email == '':
            continue
        emails.append(email)
    return emails