from sentence_transformers import SentenceTransformer
from config import MODEL_FOR_VECTORIZATION

model = SentenceTransformer(MODEL_FOR_VECTORIZATION)

# texts - массив из преложений (чанков). вернет массив, где в каждом будет уже вектрорихированный чанк
def vectorization(texts):
    
    embeddings = model.encode(texts)
    
    return embeddings





