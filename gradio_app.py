import gradio as gr
import requests

def predict(text, image, bot_score, engagement):
    files = {"image": open(image, "rb")}
    response = requests.post(
        "http://localhost:8000/predict",
        data={"text": text, "bot_score": bot_score, "engagement_rate": engagement},
        files=files
    )
    return response.json()

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Textbox(label="News Text"),
        gr.Image(type="filepath", label="Upload Image"),
        gr.Slider(0, 5, label="Bot Likelihood Score"),
        gr.Number(label="Engagement Rate (posts/hour)")
    ],
    outputs=gr.Label(label="Prediction"),
    examples=[
        ["BREAKING: President signs new law", "real_image.jpg", 1.2, 300],
        ["ALIENS LAND IN TEXAS", "fake_meme.png", 4.8, 5000]
    ],
    title="Fake News Detector",
    description="Multimodal analysis of news content"
)

demo.launch(server_port=7860)