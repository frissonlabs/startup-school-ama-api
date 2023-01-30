
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import cohere_api
import openai_api
from utils import get_context, get_prompt  # Python 3.6+ only

load_dotenv()

import os

QUESTION_CHAR_LIMIT = os.getenv('QUESTION_CHAR_LIMIT') or "255"

class Query(BaseModel):
	question: str
	embedding: str
	
app = FastAPI(
	title="Startup School AMA API",
	description="An API for all Startup School AMA Python-based endpoints",
	version="0.1.0",
	docs_url='/api',
	openapi_url='/api/openapi.json',
	redoc_url=None
)

origins = [os.getenv('APP_URL')]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["POST", "GET"],
	allow_headers=["*"],
)

@app.get("/")
async def root():
	return {"message": "Hello World"}

# @app.get("/api/ask")
# async def ask(question: str, embedding: str = "openai"):
# 	print(question)
# 	if embedding == "openai":
# 		embedded_query = openai_api.get_embedding(question)
# 		context = get_context(openai_api.get_pinecone_index(), embedded_query)
# 	elif embedding == "cohere":
# 		embedded_query = cohere_api.get_embedding(question)
# 		context = get_context(cohere_api.get_pinecone_index(), embedded_query)
# 	prompt = get_prompt(question, context)
# 	answer = openai_api.ask(prompt)
# 	return {
# 		"answer": answer
# 	}

# Use POST instead of GET to avoid URL length limit of 2048 characters, in case we need to support longer questions in the future
@app.post("/api/ask")
async def ask(query: Query):
	if(query.embedding != "openai" and query.embedding != "cohere"):
		return {
			"answer": "Invalid embedding."
		}

	if(query.question == None or len(query.question) == 0):
		return {
			"answer": "Question is empty."
		}

	if len(query.question) >= int(QUESTION_CHAR_LIMIT):
		return {
			"answer": "Question is too long. Please keep it under " + QUESTION_CHAR_LIMIT + " characters."
		}

	if query.embedding == "openai":
		embedded_query = openai_api.get_embedding(query.question)
		context = get_context(openai_api.get_pinecone_index(), embedded_query)
	elif query.embedding == "cohere":
		embedded_query = cohere_api.get_embedding(query.question)
		context = get_context(cohere_api.get_pinecone_index(), embedded_query)
	prompt = get_prompt(query.question, context)
	answer = openai_api.ask(prompt)
	return {
		"answer": answer
	}
