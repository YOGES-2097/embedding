import os
from dotenv import load_dotenv
from google import genai 

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

result = client.models.embed_content(
    model="gemini-embedding-2-preview",
    contents="artificial intelligence"
)

embedding = result.embeddings[0].values

print(f"Success! Dimension size: {len(embedding)}") 
print(f"First 10 values: {embedding[:10]}")