
import gradio as gr

def chat(text):
    return "UI Response: " + text

iface = gr.Interface(fn=chat, inputs="text", outputs="text")
iface.launch()
