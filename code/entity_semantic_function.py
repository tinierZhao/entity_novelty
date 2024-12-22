from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

local_path = r'D:\123pan\Downloads\scibert_scivocab_uncased'
# 加载本地模型和分词器
tokenizer = AutoTokenizer.from_pretrained(local_path)
model = AutoModel.from_pretrained(local_path)


def get_static_entity_embedding(entity):
    inputs = tokenizer(entity, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state

    subword_embeddings = embeddings[0][1:-1]

    if len(subword_embeddings) > 1:
        entity_embedding = subword_embeddings.mean(dim=0)
    else:
        entity_embedding = subword_embeddings[0]

    return entity_embedding
