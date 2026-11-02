import gradio as gr
from chatbot import ask_question

def chat(question):
    return ask_question(question)

demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask anything about the document..."
    ),
    outputs=gr.Textbox(lines=10),
    title="📄 AI Document Assistant",
    description="Ask questions about your uploaded PDF."
)

demo.launch()