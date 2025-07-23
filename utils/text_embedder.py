import google.generativeai as genai 
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity

def embed_chunks(chunks):
    embeddings = []
    
    for i, chunk in enumerate(chunks):
         # skip empty chunks
        if not chunk.strip():
            embeddings.append(np.zeros(768))    # or appropriate embedding size
            continue
    
        # limit chunk length
        chunk = chunk[:3000]
        
        try:
            res = genai.embed_content(
                model="models/embedding-001",
                content=chunk,
                task_type="retrieval_document"
            )
            embeddings.append(res["embedding"])
         
        except Exception as e:
            print(f"Embedding failed for chunk {i}: {e}")
            embeddings.append(np.zeros(768))    # fallback zero vector
    
    return np.array(embeddings)

def embed_query(query):
    if not query.strip():
        return np.zeros(768)    # fallback zero vector
    try:
        res = genai.embed_content(
                model="models/embedding-001",
                content=query,
                task_type="retrieval_query"
            )
        return res["embedding"]

    except Exception as e:
        print(f"Embedding failed for query: {e}")
        return np.zeros(768)    # fallback zero vector  

def retrieve_relevant_chunks(query, chunk_embeddings, chunks, top_k=5):
    query_embedding = embed_query(query)
    similarities = cosine_similarity([query_embedding], chunk_embeddings)[0]
    sorted_indices = np.argsort(similarities)[::-1][:top_k]
    return [chunks[i] for i in sorted_indices]
    
   
    
