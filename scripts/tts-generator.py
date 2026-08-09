#!/usr/bin/env python3
"""
Text-to-Speech Generator - ElevenLabs integration
"""

import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class TTSGenerator:
    def __init__(self, api_key, voice_id):
        self.api_key = api_key
        self.voice_id = voice_id
        self.base_url = "https://api.elevenlabs.io/v1"
    
    def generate(self, text, output_file):
        """Generate speech from text"""
        url = f"{self.base_url}/text-to-speech/{self.voice_id}"
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Voice generated: {output_file}")
            return output_file
        except requests.exceptions.RequestException as e:
            print(f"❌ Error generating voice: {e}")
            return None
    
    def get_voices(self):
        """Get available voices"""
        url = f"{self.base_url}/voices"
        headers = {"xi-api-key": self.api_key}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching voices: {e}")
            return None

if __name__ == "__main__":
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")
    
    if not api_key:
        print("❌ ELEVENLABS_API_KEY not set in .env")
    else:
        tts = TTSGenerator(api_key, voice_id)
        print(f"🎙️ TTS Generator initialized")
        print(f"Voice ID: {voice_id}")
