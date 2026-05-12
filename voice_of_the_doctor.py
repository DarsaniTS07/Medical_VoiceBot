import os
from dotenv import load_dotenv
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

# Load environment variables from .env file
load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_gtts(input_text, output_filepath):
    """Convert text to speech using Google TTS (free)"""
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    return output_filepath


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    """Convert text to speech using ElevenLabs (requires API key with permissions)"""
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="pNInz6obpgDQGcFmaJgB",
        model_id="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    return output_filepath