# AI-CHATBOT-WITH-NLP

"COMPANY*: CODTECH IT SOLUTIONS

NAME: AYESHA SHAIKH

INTERN ID: CTIS4434

"DOMAIN*: PYTHON

"DURATION*: 4 WEEKS

MENTOR: NEELA SANTOSH

PROJECT OVERVIEW:

This project is a simple chatbot developed using Python and basic Natural Language Processing (NLP) techniques. The main purpose of the chatbot is to interact with users, understand their questions, and provide appropriate responses based on a predefined set of question–answer pairs. It demonstrates how computers can process human language and simulate conversation in a simple and effective way.

The chatbot works using a dataset that contains many common questions and their corresponding answers. These include greetings like “hello” and “hi,” general questions such as “who are you,” technical questions related to artificial intelligence and programming, fun interactions like jokes, and exit commands. This dataset acts as the knowledge base of the chatbot. Whenever a user types a message, the chatbot compares it with these stored questions to find the most similar one.

A very important part of the project is text preprocessing. Before comparing the user’s input with stored questions, the chatbot cleans and prepares the text. First, it converts the input into lowercase so that there is no difference between uppercase and lowercase letters. Then it breaks the sentence into smaller parts called tokens, which are usually individual words. After that, it uses a process called lemmatization. Lemmatization converts words into their base form. For example, words like “running,” “runs,” and “ran” are converted to the root word “run.” This helps the chatbot understand different forms of the same word more easily.

After preprocessing, the chatbot uses a technique called TF-IDF (Term Frequency–Inverse Document Frequency). This method converts text into numerical values so that the computer can compare sentences mathematically. TF-IDF gives more importance to meaningful words and less importance to common words like “is,” “the,” or “and.” Each question and the user’s input are converted into numerical vectors using this method.

Once the text is converted into vectors, the chatbot calculates cosine similarity. Cosine similarity measures how similar two sentences are by calculating the angle between their vectors. If the angle is small, the similarity is high. The chatbot finds which stored question has the highest similarity score with the user’s input. It then returns the answer linked to that question.

The chatbot also uses a similarity threshold. If the similarity score is too low, it means the chatbot cannot understand the user’s input properly. In this case, it gives a default response such as “Sorry, I didn’t understand that.” This prevents the chatbot from giving incorrect answers.

The chatbot runs inside a continuous loop, allowing users to keep chatting until they type an exit word like “bye.” Overall, this project is a good example of how basic NLP techniques can be used to build a simple conversational system. It helps learners understand key concepts like text preprocessing, vectorization, and similarity matching while providing a foundation for building more advanced AI chatbots in the future.

OUTPUT

<img width="650" height="368" alt="Image" src="https://github.com/user-attachments/assets/6de38828-571b-4749-986d-a802794ab1ea" />
