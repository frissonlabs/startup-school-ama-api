import os

import cohere
import pinecone
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(cohere_api_key)

def get_embedding(text: str):
	"""Get embedding from Cohere API"""
	return co.embed(
		texts=[text],
		model='large',
		truncate='LEFT'
	).embeddings[0]

def get_pinecone_index():
	"""Get Pinecone index"""
	api_key = os.getenv('PINECONE_COHERE_API_KEY')
	# get this from Pinecone dashboard

	pinecone.init(
		api_key=api_key,
		environment="us-east1-gcp"
	)

	index = pinecone.Index("cohere")
	return index
