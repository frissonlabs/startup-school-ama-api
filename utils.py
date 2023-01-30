
import pinecone


def get_context(index: pinecone.Index, embedded_query: list ):
	result = index.query(embedded_query, top_k=12, include_metadata=True)
	matches = result["matches"]
	matches = [f"{m['metadata']['text']}" for m in matches if m['score'] > 0.5]
	context = ' '.join(matches).replace('.,', '.')
	return context

def get_prompt(query: str, context: str):
	prompt = f"""
		Context:
		{context}

		Answer the following question as truthfully as possible using the provided text: 
		{query}
		"""
	return prompt
