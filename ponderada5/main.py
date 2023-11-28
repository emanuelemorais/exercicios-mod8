import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts.chat import (ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate)
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma


def main():

    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    system_template = """Use the following pieces of context to answer the users question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    """

    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]

    prompt = ChatPromptTemplate.from_messages(messages)
    chain_type_kwargs = {"prompt": prompt}

    # Interface streamlit
    st.title('Chatbot da Manu :)')
    url = st.text_input("Insert the URL:")
    question = st.text_input("Ask a question:")

    if st.button("Submit", type="primary"):

         with st.spinner("Loading..."):

            loader = WebBaseLoader(url) 
            data = loader.load()

            # Divide em chunks
            text_splitter = CharacterTextSplitter( chunk_size=500, chunk_overlap=40)
            docs = text_splitter.split_documents(data)
            
            # Instância da classe que faz as respresentações vetoriais do texto
            embedding_function = OpenAIEmbeddings()
            
            # Cria vetor de documentos
            vectordb = Chroma.from_documents(documents=docs, embedding=embedding_function)

            # Converte um vetor de documentos em um objeto retriever
            retriever = vectordb.as_retriever()
            
            #Instância do modelo 
            llm = ChatOpenAI(model_name='gpt-3.5-turbo')

            # omponente que combina um modelo de linguagem com um sistema de recuperação de documentos para realizar a tarefa de Question Answering.
            qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

            response = qa({"query": question})
            print(response)
            
            st.subheader('Answer:')
            output_container = st.empty()
            
            words = response['result'].split()
            for i in range(len(words)):
                output_container.write(" ".join(words[:i+1]))
                time.sleep(0.1) 

if __name__ == '__main__':
    main()
