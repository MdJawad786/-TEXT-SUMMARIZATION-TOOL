
import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="📝 Text Summarization Tool", layout="wide")
st.markdown("""
    <style>
    @keyframes gradientAnimation {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background: linear-gradient(-45deg, #ffecd2, #fcb69f, #a1c4fd, #c2e9fb);
        background-size: 400% 400%;
        animation: gradientAnimation 12s ease infinite;
    }
    </style>
""", unsafe_allow_html=True)
from summarizer import summarize_text
from sample_texts import sample_articles




# Title and description
st.markdown("<h1 style='color:blue;'>📝 Text Summarization Tool</h1>", unsafe_allow_html=True)
st.markdown("### Summarize long articles using NLP techniques")
st.markdown("---")

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This tool uses 3 simple NLP techniques:
    
    1. **Tokenization** - Breaking text into sentences and words
    2. **Word Frequency** - Counting important words
    3. **Sentence Scoring** - Finding key sentences
    """)
    
    st.markdown("---")
    st.header("How to Use")
    st.write("""
    1. Choose a sample article OR paste your own text
    2. Select number of sentences for summary
    3. Click 'Generate Summary' button
    """)
    
    st.markdown("---")
    st.header("Tips")
    st.write("""
    - Use 2-3 sentences for short summaries
    - Use 4-5 sentences for longer articles
    - The tool works best with articles of 5+ sentences
    """)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Text")
    
    # Sample articles
    sample_articles = {
        "Select a sample...": "",
        "About Dogs": """Dogs are wonderful pets and loyal companions. They provide unconditional love to their owners. Dogs need regular exercise and a healthy diet. Training your dog is important for good behavior. Dogs can learn many tricks and commands. They are very intelligent animals. Dogs have been humans' best friends for thousands of years. Taking care of a dog is a big responsibility.""",
        
        "About Internet": """The internet has changed how we communicate with each other. People can now send messages instantly across the world. Social media platforms connect billions of users globally. Online shopping has made buying products more convenient. Students can access educational resources from anywhere. However, internet addiction is becoming a serious problem. Many people spend too much time on their phones. Cybersecurity is also a major concern today. Hackers can steal personal information online. Despite the risks, the internet remains an essential tool. It has revolutionized business, education, and entertainment.""",
        
        "About Electric Vehicles": """Electric vehicles are becoming more popular every year. Major car manufacturers are investing heavily in electric technology. EVs produce zero direct emissions, making them environmentally friendly. The main advantage of electric cars is lower operating costs. Electricity is cheaper than gasoline in most countries. Electric motors require less maintenance than traditional engines. However, the initial purchase price is still high. Battery technology continues to improve rapidly. Modern EVs can travel over 300 miles on a single charge. Charging infrastructure is expanding in cities worldwide. Governments offer incentives to encourage EV adoption. Some people worry about charging time compared to refueling gas cars. Despite challenges, electric vehicles represent the future of transportation. Climate change concerns are driving the shift to electric mobility."""
    }
    
    # Sample selection
    st.markdown("""
    <style>
    /* Make the selectbox label blue and bigger */
    label[data-testid="stWidgetLabel"] > div {
        color: #007BFF !important;  /* bright blue */
        font-size: 20px !important; /* larger font */
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)
    selected_sample = st.selectbox("Choose a sample article:", list(sample_articles.keys()))
    
    # Text input area
    if selected_sample != "Select a sample...":
        default_text = sample_articles[selected_sample]
    else:
        default_text = ""
    
    input_text = st.text_area(
        "Or paste your own text here:",
        value=default_text,
        height=300,
        placeholder="Enter or paste your article here..."
    )
    
    # Number of sentences slider
    num_sentences = st.slider(
        "Number of sentences in summary:",
        min_value=1,
        max_value=10,
        value=3,
        help="Select how many sentences you want in the summary"
    )
    
    # Generate button
    generate_button = st.button("Generate Summary", type="primary", use_container_width=True)

with col2:
    st.subheader("Summary Output")
    
    if generate_button:
        if input_text.strip():
            with st.spinner("Generating summary..."):
                summary, total_sentences = summarize_text(input_text, num_sentences)
                
                # Display summary
                st.success("Summary generated successfully!")
                st.markdown("#### Summary:")
                st.info(summary)
                
                # Statistics
                st.markdown("#### 📊 Statistics:")
                col_stat1, col_stat2, col_stat3 = st.columns(3)
                
                with col_stat1:
                    st.metric("Original Sentences", total_sentences)
                
                with col_stat2:
                    st.metric("Summary Sentences", num_sentences)
                
                with col_stat3:
                    compression = (num_sentences / total_sentences) * 100
                    st.metric("Compression", f"{compression:.1f}%")
                
                # Word count
                original_words = len(input_text.split())
                summary_words = len(summary.split())
                
                st.markdown("---")
                col_word1, col_word2 = st.columns(2)
                with col_word1:
                    st.metric("Original Words", original_words)
                with col_word2:
                    st.metric("Summary Words", summary_words)
        
        else:
            st.error("Please enter some text to summarize!")
    
    else:
        st.info("Enter text and click 'Generate Summary' to see results")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Simple NLP Text Summarization</p>
</div>
""", unsafe_allow_html=True)