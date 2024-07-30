import json

greeting = {
    "en": "hello",
    "fr": "bonjour",
    "es": "halo",
    "vi": "xin chào"
}

def lambda_handler(event, context):
    # TODO implement
    
    print(event['pathParameters'])
    
    username = event['pathParameters'].get('username')
    lang = event['queryStringParameters'].get('lang', '')

    print(f"username is: {username}")
    print(f"language is: {lang}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('{} {}'.format(greeting[lang], username))
    }
