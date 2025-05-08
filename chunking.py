import spacy 
from config import MODEL_FOR_CHUNKING

nlp = spacy.load(MODEL_FOR_CHUNKING)

# принимает текст на входе, выдает по два предложения на чанк
def semanticChunking(text: str, max_sentence=2) -> list:
    
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    chunks = []
    
    for i in range(0, len(sentences), max_sentence):
        chunk = ' '.join(sentences[i : i+max_sentence])
        chunks.append(chunk)

    return chunks
