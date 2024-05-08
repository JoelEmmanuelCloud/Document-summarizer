# summarization.py

import boto3
import os
import json
from document_processing import process_document
from prompts import summary_prompt
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the Bedrock client with loaded credentials
bedrock = boto3.client(
    'bedrock-runtime',
    'us-east-1',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

def get_completion(prompt, max_tokens_to_sample=1000):
    """Get completion from Bedrock model."""
    # Ensure the prompt ends with "Assistant:" turn
    prompt += '\n\nAssistant:'

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": max_tokens_to_sample,
        "temperature": 0,  # Set temperature to 0 for precision
        "top_k": 50,
        "top_p": 0.95,
        "stop_sequences": ["\n\nHuman:", "\n\nAssistant:"],
    })

    # Define necessary information for calling the Bedrock model
    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    # Call the Bedrock model with the request body
    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType)

    # Decode the response body bytes to string and strip whitespace
    response_body = response.get('body').read().decode('utf-8').strip()
    print("Response Body:", response_body)

    # Check if the response body is not empty
    if response_body:
        completion = json.loads(response_body).get('completion')
        return completion
    else:
        return None

def summarize_document(document_text, prompt):
    """Summarize an individual document."""
    # Add an optional system prompt before the user's input
    prompt_with_context = f'\n\nSystem: Please summarize the following document in a concise and clear manner. Provide only the summary, without any additional information about the document.\n\n'
    full_prompt = '\n\n'.join([prompt_with_context, f'Human: {prompt}\n\n', document_text])
    response = get_completion(full_prompt)
    return response

def summarize_folder(folder_path):
    """Summarize documents in a folder."""
    final_summaries = []
    answers = {}  # Dictionary to store answers for each folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            document_text = process_document(file_path)
            summary = summarize_document(document_text, summary_prompt)
            final_summaries.append(summary)

    return final_summaries, answers
