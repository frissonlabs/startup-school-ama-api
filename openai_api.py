import os

import openai
import pinecone
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.getenv('OPENAI_ORGANIZATION_KEY')
# get this from top-right dropdown on OpenAI under organization > settings

openai.api_key = os.getenv('OPENAI_API_KEY')
# get API key from top-right dropdown on OpenAI website

COMPLETIONS_MODEL = "text-davinci-003"

def get_embedding(text: str):
	"""Get embedding from OpenAI API"""
	result = openai.Embedding.create(
		input=text, engine="text-embedding-ada-002"
	)
	return result["data"][0]["embedding"]

def get_pinecone_index():
	"""Get Pinecone index"""
	api_key = os.getenv('PINECONE_OPENAI_API_KEY')
	# get this from Pinecone dashboard

	pinecone.init(
		api_key=api_key,
		environment="us-east1-gcp"
	)

	index = pinecone.Index("openai")
	return index

def ask(prompt: str):
	answer = openai.Completion.create(
		prompt=prompt,
		temperature=0,
		max_tokens=400,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0,
		model=COMPLETIONS_MODEL
	)["choices"][0]["text"].strip(" \n")
	return answer