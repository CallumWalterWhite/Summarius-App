# Document Vectorization and Semantic Search
This is a Python-based project that allows users to upload documents, which are then saved into a vector database. The project uses natural language processing (NLP) techniques to convert each document into a vector representation. These vectors are then used to provide a semantic search, which allows users to search for and retrieve relevant documents based on their content.

# Getting Started
To get started with this project, you will need to have Python installed on your machine. You will also need to install the following Python packages:

- flask
- numpy
- pandas
- sklearn
- nltk
Once you have installed these packages, you can clone this repository to your local machine:

shell
Copy code
$ git clone https://github.com/<username>/document-vectorization-and-semantic-search.git
Usage
To use this project, you will first need to start the Flask application by running the following command in your terminal:

ruby
Copy code
$ python app.py
This will start the application on your local machine. You can then navigate to http://localhost:5000 in your web browser to access the application.

Once you have accessed the application, you can upload documents by clicking on the "Upload Document" button. This will allow you to select a document from your local machine and upload it to the server.

Once the document has been uploaded, it will be converted into a vector representation and saved to the vector database. You can then search for documents using the search bar on the homepage. The search function uses cosine similarity to compare the query vector to the vectors in the database and returns the most relevant documents based on their content.

## Contributing
If you would like to contribute to this project, please submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



