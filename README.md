The goal of this project is to develop a QA bot that can help retrieve data from a corpus of PDF documents. The core of this system is Llama-Index, which is made for indexing and searching textual content.
1.	Installing Libraries: Pip was used to install necessary libraries, such as llama-index and its parts for basic functioning, OpenAI integration, and embeddings.
2.	Document Loading: A directory containing the PDFs was specified, and the text of the documents was loaded using a SimpleDirectoryReader object.
3.	Indexing: To facilitate effective information retrieval based on document content similarity, a vector store index was built using VectorStoreIndex.from_documents.
4.	OpenAI Service Setup: To authenticate access to OpenAI's services, an OpenAI API key was set in the environment variable OPENAI_API_KEY.
5.	Model Setup: Strong LLM is used due to its superior question-answering abilities, OpenAI's gpt-3.5-turbo was selected. To efficiently represent the document content for retrieval, OpenAI's text-embedding-3-small embedding model was chosen.
6.	Querying: To establish a query engine for continuous answer output, the as query engine method was utilized, with the streaming parameter enabled. This makes interacting with the bot in real time possible.
![Screenshot_1](https://github.com/eshaag202/Multi-PDF-QA-Bot/assets/90109712/8af86729-0ca5-42f0-ab62-037cfd0c120c)
![Screenshot_2](https://github.com/eshaag202/Multi-PDF-QA-Bot/assets/90109712/29529944-d9e3-4363-9f1b-390019536e14)
