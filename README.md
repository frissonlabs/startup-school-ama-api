# Startup School Ask Me Anything Bot - API

Tested with Python 3.9.15

Dependencies:

FastAPI (API framework)
Pinecone (managed vector database for embeddings)
OpenAI (for generating embeddings and forming answers given a query and context)
Cohere (for generating embeddings)

## Environment Variables

```
OPENAI_API_KEY
OPENAI_ORGANIZATION_KEY
COHERE_API_KEY
PINECONE_OPENAI_API_KEY
PINECONE_COHERE_API_KEY // If using a secondary Pinecone account
QUESTION_CHAR_LIMIT //  Defaults to 255
APP_URL
```
