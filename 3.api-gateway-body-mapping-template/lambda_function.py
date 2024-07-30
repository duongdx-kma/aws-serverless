import json

def lambda_handler(event, context):
    # TODO implement

    input_1 =  event['input_1']
    input_2 =  event['input_2']

    match event['operation']:
        case 'add':
            result = input_1 + input_2
        case 'subtract':
            result = input_1 - input_2
        case 'multiply':
            result = input_1 * input_2
        case 'divide':
            result = input_1 / input_2

    return {
        'statusCode': 200,
        'body': json.dumps('result is {}'.format(result))
    }
