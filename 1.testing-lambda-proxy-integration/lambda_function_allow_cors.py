import json

greeting = {
    "en": "hello",
    "fr": "bonjour",
    "es": "halo",
    "vi": "xin chào"
}

def lambda_handler(event, context):
    # TODO implement

    # 1.testing-lambda-proxy-integration
    username = event['queryStringParameters'].get('username', '')
    lang = event['queryStringParameters'].get('lang', '')

    print(f"username is: {username}")
    print(f"language is: {lang}")
    
    return {
        'statusCode': 200,
        'headers': {
            # "Access-Control-Allow-Origin": "duongdx.com"
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps('{} {}'.format(greeting[lang], username))
    }
