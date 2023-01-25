import openai

# Set your API key
openai.api_key = "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"

# Define the prompt and the model to use
# prompt is nothing but a question which you are asking from chatgpt and based on your prompt it will give the answer
prompt = "how is the weather in america today"
model = "text-davinci-002"

# Call the create method
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

# Print the generated text
print(response['choices'][0]['text'])

