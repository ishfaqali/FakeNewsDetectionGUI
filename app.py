from fastapi import FastAPI, UploadFile, File
from PIL import Image
import torch
import io
import numpy as np

app = FastAPI()

# Load your trained model
model = torch.load('models/multimodal_model.pt')
model.eval()

@app.post("/predict")
async def predict(
    text: str,
    image: UploadFile = File(...),
    bot_score: float,
    engagement_rate: float
):
    # Process image
    img = Image.open(io.BytesIO(await image.read()))
    img_tensor = preprocess_image(img)  # Your image preprocessing
    
    # Process social features
    social_features = torch.tensor([bot_score, engagement_rate])
    
    # Make prediction
    with torch.no_grad():
        output = model(
            text=process_text(text),
            image=img_tensor,
            social=social_features,
            event=calculate_event_features(text)
        )
    
    return {"prediction": "fake" if output.argmax() == 1 else "real"}