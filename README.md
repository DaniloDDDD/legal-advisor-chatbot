# legal-advisor-chatbot
Legal Advisor chatbot
This project is a Legal Advisor Chatbot powered by OpenAI's GPT-3.5 model, built using FastAPI, Streamlit, and Langchain. It provides legal advice based on user input through a conversational interface. The chatbot remembers the context of previous conversations using a session ID, ensuring a personalized experience.
Project Structure

The project consists of several Python files and modules that work together to provide the functionality of the chatbot. Below is an overview of the files:

    main.py: The main FastAPI application that exposes an endpoint (/chat) for receiving legal questions and returning AI-generated responses.

    services2.py: Contains the logic for interacting with the OpenAI API and managing the conversation history using Langchain.

    streamlit_app.py: A Streamlit frontend for interacting with the chatbot. It allows users to ask legal questions and receive answers from the AI.

    .env: A file containing environment variables such as the OpenAI API key for accessing the model.

To run this project locally, follow these steps:

    -clone repository
    -create .env: A file containing environment variables such as the OpenAI API key for accessing the model.
    -run the fast API backend with command      uvicorn main:app --host 127.0.0.1 --port 8001
    -run the streamlit frontend with command    streamlit run streamlit_app.py


How It Works:
1. Frontend (Streamlit)
-Users enter a legal question, which is sent to the FastAPI backend through a POST request. The frontend displays the AI-generated response.
2. Backend (FastAPI)
-The FastAPI application defines a POST /chat endpoint that processes the question and sends it to Langchain for generating a response using the OpenAI model.
3. Langchain (Pipeline)
-Langchain is responsible for managing conversation history and generating AI responses using OpenAI’s GPT-3.5 model.
4. Session Management
-The session ID helps maintain context across interactions, allowing the chatbot to remember previous conversations.
