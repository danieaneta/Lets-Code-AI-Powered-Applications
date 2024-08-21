import base64
import requests
from dotenv import load_dotenv
import os 


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class OpenAI_Detection():
    def __init__(self, image):
        self.image = image

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def Run_Detection(self):
        base64_image = self.encode_image(self.image)

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "What’s in this image?"
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                    }
                ]
                }
            ],
            "max_tokens": 300
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        return response.json()


if __name__ == "__main__":
    OpenAI_Detection('images/test.jpg').Run_Detection()