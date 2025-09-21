import json
import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str) -> str:
    """
    
    Analyze the sentiment of the given text.
    
    Args:
       text (str): Text to analyze

    Returns:
        str: A JSON string containing polarity, subjectivity, and assessment 
        
    """

    blob = TextBlob(text)
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2), # from -1 negative to +1 positive
        "subjectivity": round(sentiment.subjectivity, 2),
        "assessment": "positive" if sentiment.polarity > 0 else "negative"
    
    }

    return json.dumps(result)


demo = gr.Interface(
    fn=sentiment_analysis,
    inputs = gr.Textbox(placeholder="Enter text to analyze..."),
    outputs= gr.Textbox(),
    title = "Text sentiment analysis",
    description = "Analyze the sentiment of text using TextBlob"
)

if __name__=="__main__":
    demo.launch(mcp_server=True)