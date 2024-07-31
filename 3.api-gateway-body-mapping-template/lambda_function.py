import json

def lambda_handler(event, context):
    # TODO implement
    print(event)

    input_1 = int(event['input']['input_1'])
    input_2 = int(event['input']['input_2'])

    match event['operation']:
        case 'add':
            result = input_1 + input_2
        case 'subtract':
            result = input_1 - input_2
        case 'multiply':
            result = input_1 * input_2
        case 'divide':
            result = input_1 / input_2
        case _:
            print("The language doesn't matter, what matters is solving problems.")
            result = 0

    return {
        'statusCode': 200,
        'body': json.dumps('result is {}'.format(result))
    }

'''
# comment

# document:
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

# Testing:
curl --location 'https://domain/dev/math/add' \
--header 'Content-Type: application/json' \
--data '{
    "input_1": 5,
    "input_2": 10
}'
'''
