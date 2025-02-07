import os
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# Initialize Console
console = Console()

# OpenAI API Configuration
token = "Github_PAT" 
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Respond in well-structure format using headings and lists."},
        {"role": "user", "content": "How to render the plain text to markdown using javascript"}
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

# Output formatted markdown in the terminal
markdown_output = response.choices[0].message.content
console.print(Markdown(markdown_output))


