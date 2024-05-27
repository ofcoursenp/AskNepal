from transformers import BertTokenizer, BertModel, AutoTokenizer
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Load the BERT tokenizer and model
tokenizer = tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

model = BertModel.from_pretrained('bert-base-uncased')

# Example sentences (already preprocessed)

tokens1 = ["[CLS]", "i", "like", "coding", "in", "python", ".", "with","Yur mom", "[SEP]"]
tokens2 = ["[CLS]", "python", "is", "my", "favorite", "programming", "language", ".", "[SEP]"]

# Convert tokens to input IDs
input_ids1 = torch.tensor(tokenizer.convert_tokens_to_ids(tokens1)).unsqueeze(0)  # Batch size 1
input_ids2 = torch.tensor(tokenizer.convert_tokens_to_ids(tokens2)).unsqueeze(0)  # Batch size 1

# Obtain the BERT embeddings
with torch.no_grad():
    outputs1 = model(input_ids1)
    outputs2 = model(input_ids2)
embeddings1 = outputs1.last_hidden_state[:, 0, :]  # [CLS] token
embeddings2 = outputs2.last_hidden_state[:, 0, :]  # [CLS] token

# Calculate similarity
similarity_score = cosine_similarity(embeddings1, embeddings2)
print("Similarity Score:", similarity_score)