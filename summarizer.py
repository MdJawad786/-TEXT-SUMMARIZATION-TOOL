import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Download required data (only needed once)
@st.cache_resource
def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except:
        nltk.download('punkt')
        nltk.download('stopwords')

download_nltk_data()


def summarize_text(text, num_sentences=3):
    """
    Summarize text using simple NLP techniques
    """
    # TECHNIQUE 1: TOKENIZATION
    sentences = sent_tokenize(text)
    
    if len(sentences) <= num_sentences:
        return text, len(sentences)
    
    words = word_tokenize(text.lower())
    
    # TECHNIQUE 2: WORD FREQUENCY
    stop_words = set(stopwords.words('english'))
    
    word_count = {}
    for word in words:
        if word.isalpha() and word not in stop_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    # TECHNIQUE 3: SENTENCE SCORING
    sentence_scores = {}
    
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        score = 0
        
        for word in sentence_words:
            if word in word_count:
                score += word_count[word]
        
        sentence_scores[sentence] = score
    
    # Find top sentences
    ranked_sentences = sorted(sentence_scores.items(), 
                             key=lambda x: x[1], 
                             reverse=True)
    
    top_sentences = [sent for sent, score in ranked_sentences[:num_sentences]]
    
    # Put sentences back in original order
    summary = []
    for sentence in sentences:
        if sentence in top_sentences:
            summary.append(sentence)
    
    return ' '.join(summary), len(sentences)