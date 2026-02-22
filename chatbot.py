import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
# Lemmatizer
lemmer = nltk.stem.WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    return [lemmer.lemmatize(token) for token in tokens]

# -------------------------------
#  Dataset (Q&A Pairs)
# -------------------------------
qa_pairs = {
    # Greetings
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there!",
    "hey": "Hey! Need any help?",
    "good morning": "Good morning! How can I help?",
    "good evening": "Good evening! How can I assist?",

    # General
    "how are you": "I am doing well, thank you!",
    "who are you": "I am a chatbot created using NLP.",
    "what is your name": "I am an AI chatbot.",
    "what can you do": "I can answer questions related to AI, programming, and general topics.",

    # AI / ML
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "define artificial intelligence": "AI enables machines to think and learn like humans.",
    "what is machine learning": "Machine learning is a subset of AI that learns from data.",
    "what is deep learning": "Deep learning uses neural networks to mimic the human brain.",
    "what is nlp": "Natural Language Processing helps computers understand human language.",

    # Programming
    "what is python": "Python is a high-level, easy-to-learn programming language.",
    "what is java": "Java is an object-oriented programming language used widely.",
    "what is programming": "Programming is the process of writing instructions for computers.",

    # College / Location
    "what is viit": "VIIT is Vishwakarma Institute of Information Technology in Pune.",
    "where is pune": "Pune is a major city in Maharashtra, India.",

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "are you real": "I am a virtual AI assistant.",
    "do you like humans": "Yes, I enjoy helping humans!",

    # Help
    "can you help me": "Of course! Ask me anything.",
    "what help can you provide": "I can help with AI, coding, and general questions.",

    # Exit
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you soon!",
    "see you": "Take care!"
}

# -------------------------------
#  Chatbot Logic
# -------------------------------
def generate_response(user_input):
    questions = list(qa_pairs.keys())
    answers = list(qa_pairs.values())

    vectorizer = TfidfVectorizer(tokenizer=preprocess, token_pattern=None)
    tfidf = vectorizer.fit_transform(questions + [user_input])

    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    index = similarity.argmax()
    score = similarity[0][index]

    if score < 0.2:
        return "Sorry, I didn't understand that."
    else:
        return answers[index]

# -------------------------------
# 💬 Chat Loop
# -------------------------------
print(" Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["bye", "goodbye", "see you"]:
        print(" Chatbot:", qa_pairs["bye"])
        break

    response = generate_response(user_input)
    print(" Chatbot:", response)