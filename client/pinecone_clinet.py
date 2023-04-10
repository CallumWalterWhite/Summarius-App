import pinecone
import os

class PineconeClient():
    def __init__(self, index=None, dimension=None):        
        api_key = os.environ.get('APIKEY')
        environment = os.environ.get('ENV')
        pinecone.init(api_key=api_key, environment=environment)
        if index is not None and dimension is not None:
            pinecone.create_index(index, dimension=dimension)
            self.index = index = pinecone.Index(index)
        if index is not None and dimension is None:
            self.index = index = pinecone.Index(index)

    def upsert_vectors(self, vectors, namespace):
        self.index.upsert(
            vectors=vectors,
            namespace=namespace
        )
    
    def query_vectors(self, query_vectors, namespace):
        response = self.index.query(
            namespace=namespace,
            top_k=1,
            include_values=True,
            include_metadata=True,
            vector=query_vectors
        )
        return response
        
    def get_index(self):
        return self.index