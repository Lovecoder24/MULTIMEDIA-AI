import requests
import json
import time
import os
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), "myev.env")
if not os.path.exists(env_path):
    raise FileNotFoundError(f"Environment file not found at: {env_path}")

load_dotenv(env_path)

# Get API keys
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")  # We'll use Replicate for text, image, and video
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")   # Alternative for image generation

# ==========================
# 1. Generate Text (Replicate - Llama 2)
# ==========================
def generate_text(prompt):
    try:
        headers = {
            "Authorization": f"Token {REPLICATE_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "version": "2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
            "input": {
                "prompt": prompt,
                "max_length": 500,
                "temperature": 0.7,
                "top_p": 0.9,
            }
        }
        # Start the generation
        response = requests.post(
            "https://api.replicate.com/v1/predictions",
            headers=headers,
            json=data
        )
        if response.status_code != 201:
            return f"Error: {response.text}"
        
        # Get the prediction ID
        prediction_id = response.json()["id"]
        
        # Poll for completion
        while True:
            response = requests.get(
                f"https://api.replicate.com/v1/predictions/{prediction_id}",
                headers=headers
            )
            if response.status_code != 200:
                return f"Error checking status: {response.text}"
            
            prediction = response.json()
            if prediction["status"] == "succeeded":
                return prediction["output"]
            elif prediction["status"] == "failed":
                return f"Error: Generation failed"
            
            time.sleep(1)
    except Exception as e:
        return f"Error: {e}"

# ==========================
# 2. Generate Image (Stability AI)
# ==========================
def generate_image(prompt):
    try:
        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "text_prompts": [{"text": prompt}],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            # Save the image
            image_data = response.json()["artifacts"][0]["base64"]
            import base64
            image_path = "output_image.png"
            with open(image_path, "wb") as f:
                f.write(base64.b64decode(image_data))
            return f"Image saved as {image_path}"
        else:
            return f"Error: {response.text}"
    except Exception as e:
        return f"Error: {e}"

# ==========================
# 3. Generate Audio (ElevenLabs)
# ==========================
def generate_audio(text, voice_id="21m00Tcm4TlvDq8ikWAM"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            audio_file = "output_audio.mp3"
            with open(audio_file, "wb") as f:
                f.write(response.content)
            return f"Audio saved as {audio_file}"
        else:
            return f"Error: {response.text}"
    except Exception as e:
        return f"Error: {e}"

# ==========================
# 4. Generate Video (Replicate - Stable Video Diffusion)
# ==========================
def generate_video(prompt):
    try:
        headers = {
            "Authorization": f"Token {REPLICATE_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "version": "435061a1b5a4c1e26740464bf786efdfa9cb3a3ac488595a2de23e143fdb0117",
            "input": {
                "prompt": prompt,
                "motion_bucket_id": 127,
                "cond_aug": 0.02,
                "decoding_t": 14,
                "frames": 25,
                "width": 1024,
                "height": 576
            }
        }
        # Start the generation
        response = requests.post(
            "https://api.replicate.com/v1/predictions",
            headers=headers,
            json=data
        )
        if response.status_code != 201:
            return f"Error: {response.text}"
        
        # Get the prediction ID
        prediction_id = response.json()["id"]
        
        print("Video generation started... This might take a few minutes.")
        
        # Poll for completion
        while True:
            response = requests.get(
                f"https://api.replicate.com/v1/predictions/{prediction_id}",
                headers=headers
            )
            if response.status_code != 200:
                return f"Error checking status: {response.text}"
            
            prediction = response.json()
            if prediction["status"] == "succeeded":
                # Download the video
                video_url = prediction["output"]
                video_response = requests.get(video_url)
                if video_response.status_code == 200:
                    video_file = "output_video.mp4"
                    with open(video_file, "wb") as f:
                        f.write(video_response.content)
                    return f"Video saved as {video_file}"
                else:
                    return f"Error downloading video: {video_response.text}"
            elif prediction["status"] == "failed":
                return f"Error: Video generation failed"
            
            print("Still processing... Please wait.")
            time.sleep(10)  # Check every 10 seconds as video generation takes longer
    except Exception as e:
        return f"Error: {e}"

# ==========================
# Test All API Functions
# ==========================
if __name__ == "__main__":
    print("Generating Text...")
    print(generate_text("Tell me a short joke."))

    print("\nGenerating Image...")
    print(generate_image("A futuristic city with flying cars."))

    print("\nGenerating Audio...")
    print(generate_audio("Hello, welcome to AI-generated audio!"))

    print("\nGenerating Video...")
    print(generate_video("A beautiful sunset over the ocean."))


