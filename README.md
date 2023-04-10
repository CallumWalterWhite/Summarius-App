# Document Vectorization and Semantic Search (WIP)
This is a Python-based project that allows users to upload documents, which are then saved into a vector database. The project uses natural language processing (NLP) techniques to convert each document into a vector representation. These vectors are then used to provide a semantic search, which allows users to search for and retrieve relevant documents based on their content.

# Getting Started

## Pinecone

Pinecone is a vector database service that allows you to store, search, and retrieve high-dimensional vectors efficiently. It is designed to work seamlessly with machine learning applications, allowing you to quickly build and deploy vector-based models.

In Pinecone, vectors are stored as embeddings, which are numerical representations of objects or data points. For example, if you are working with images, you could use a neural network to generate a high-dimensional vector for each image. These vectors can then be stored in Pinecone and used to search for similar images or to perform other vector-based operations.

One of the key benefits of Pinecone is its scalability. Pinecone is designed to handle large-scale vector databases, making it ideal for applications that require fast and efficient search over large collections of data. Additionally, Pinecone offers a range of features such as automatic indexing, query routing, and load balancing, which help to ensure that your vector database is always fast and responsive.

To use Pinecone, you first need to create a Pinecone account and set up a vector index. You can then upload your embeddings to the index using the Pinecone API. Once your vectors are in the index, you can search for similar vectors using a variety of methods, including nearest neighbor search and range search.

## Setup

To get started with this project, you will need to have Python installed on your machine. You will also need to install the following Python packages:

- flask
- numpy
- docx2txt
- sklearn
- nltk
- pinecone

Once you have installed these packages, you can clone this repository to your local machine:

Once you have accessed the application, you can upload documents by clicking on the "Upload Document" button. This will allow you to select a document from your local machine and upload it to the server.

Once the document has been uploaded, it will be converted into a vector representation and saved to the vector database. You can then search for documents using the search bar on the homepage. The search function uses cosine similarity to compare the query vector to the vectors in the database and returns the most relevant documents based on their content.

## Contributing
If you would like to contribute to this project, please submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



