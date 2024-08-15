import boto3
import json

from botocore.exceptions import ClientError

client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "anthropic.claude-3-haiku-20240307-v1:0"

prompt = "What is EC2?"

native_request = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.5,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        }
    ],
}

request = json.dumps(native_request)

try:
    response = client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

model_response = json.loads(response["body"].read())

response_text = model_response["content"][0]["text"]
print(response_text)


