import os
import glob
import docx2txt
import spacy
import numpy as np
from client import PineconeClient
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import torch
from transformers import BartForConditionalGeneration, BartTokenizer

max_features = 1024
def upload_file(file_path):
    data = []
    docIds = []
    filePath = []
    try:
        text = docx2txt.process(file_path)
        data.append(text)
        filename = re.search(r"[^/\\]*$", file_path).group(0)
        docIds.append(re.sub(r'\s+', '', filename))
        filePath.append(file_path)
        vectorizer = TfidfVectorizer(max_features=max_features)
        document_vectors = vectorizer.fit_transform(data)
        pineconeClient = PineconeClient('reporting')
        vectors = []
        for i in range(0, len(docIds)):
            vectors.append(
                {
                    "id": docIds[i],
                    "values": document_vectors.toarray()[i].tolist(),
                    "metadata": {"path": filePath[i]}
                }
            )
        pineconeClient.upsert_vectors(vectors, "doc")
    except Exception as e:
        print(e)

def fit_model():
    doc_dir = "uploads"
    data = []
    for file_path in glob.glob(os.path.join(doc_dir, "*.docx")):
        try:
            print(file_path)
            text = docx2txt.process(file_path)
            data.append(text)
        except Exception as e:
            print(e)
    print(len(data))
    max_features = 1024
    vectorizer = TfidfVectorizer(max_features=max_features)
    vectorizer.fit(data)
    return vectorizer

def get_summary(prompt):
    pineconeClient = PineconeClient('reporting')
    vectorizer = fit_model()
    query_vector = vectorizer.transform([prompt])
    v = query_vector.toarray()[0].tolist()
    response = pineconeClient.query_vectors(v, "doc")
    match = response['matches'][0]
    file_path = match['metadata']['path']
    text = docx2txt.process(file_path)
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    inputs = tokenizer(text, return_tensors='pt',truncation=True, max_length=max_features)
    summary_ids = model.generate(inputs['input_ids'])
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary