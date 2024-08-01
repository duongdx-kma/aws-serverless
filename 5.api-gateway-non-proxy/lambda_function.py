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
    username = event['queryParams'].get('username', '')
    lang = event['queryParams'].get('lang', '')

    return {
        'statusCode': 200,
        'body': json.dumps('{} {}'.format(greeting[lang], username)),
        'function_version': context.function_version,
        'function_name': context.function_name,
        'api_stage': event['stage']
    }


aws lambda add-permission \
--function-name "arn:aws:lambda:ap-southeast-1:240993297305:function:demoFunction2:${stageVariables.aliass}" \
--source-arn "arn:aws:execute-api:ap-southeast-1:240993297305:1fm7n3wszg/*/GET/testing" \
--principal apigateway.amazonaws.com \
--statement-id 55a439fc-f5fb-404d-b984-5ca6a4605bc1 \
--action lambda:InvokeFunction