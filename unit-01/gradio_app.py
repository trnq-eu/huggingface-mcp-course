import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """
    Count the number of occurrences of a letter in a word or text

    Args:
        word (str): the input text to search through
        letter (str): the letter to search for

    Returns:
        int: the number of times the letter appears in the text
    """

    word = word.lower()
    letter = letter.lower()
    count = word.count(letter)
    return count

# gradio interface
demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Letter counter",
    description="Enter text and a letter to count how many times the letter appears in the text."
)

if __name__=="__main__":
    demo.launch(mcp_server=True)