import torch
from transformers import pipeline
from config import MODEL_TO_CLASSIFIER, LABBELS_TO_CLASSIFIER

# классификатор zero-shot
classifier = pipeline('zero_shot_classification', model=MODEL_TO_CLASSIFIER)

# классы
labels = LABBELS_TO_CLASSIFIER

# принимает запрос, вернет самый веротный класс, а также на сколько в нем уверен
def classifyQuery(query: list) -> tuple:
    
    results = classifier(query, candidate_labels=labels)
    return results['labels'][0], results['score'][0]

