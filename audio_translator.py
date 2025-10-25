"""
Real-time Translation & Voice Re-Dubbing App

This module provides a complete pipeline for:
1. Transcribing audio files using OpenAI Whisper API
2. Translating transcribed text to target language
3. Converting translated text to speech using ElevenLabs API
4. Playing the synthesized audio

The design is modular to allow easy future upgrades (e.g., live microphone input).
"""

import os
import tempfile
from pathlib import Path
from typing import Optional

from openai import OpenAI
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from deep_translator import GoogleTranslator
from pydub import AudioSegment
from playsound3 import playsound


class AudioTranslator:
    """
    A modular class for audio translation and voice re-dubbing.
    
    This class handles the complete pipeline from audio input to synthesized
    speech output in a different language.
    """
    
    def __init__(self):
        """Initialize the AudioTranslator with API clients."""
        # Initialize OpenAI client for Whisper API
        # The newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        self.openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        # Initialize ElevenLabs client for text-to-speech
        self.elevenlabs_client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))
        
        # Create output directory for temporary audio files
        self.output_dir = Path("temp_audio")
        self.output_dir.mkdir(exist_ok=True)
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """
        Step 1: Transcribe audio file to text using OpenAI Whisper API.
        
        Args:
            audio_file_path: Path to the audio file (WAV, MP3, etc.)
        
        Returns:
            Transcribed text from the audio
        
        Raises:
            FileNotFoundError: If the audio file doesn't exist
            Exception: If transcription fails
        """
        print(f"\n[Step 1/4] Transcribing audio file: {audio_file_path}")
        
        # Validate file exists
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file not found: {audio_file_path}")
        
        try:
            # Open the audio file and send to Whisper API
            with open(audio_file_path, "rb") as audio_file:
                response = self.openai_client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            
            transcribed_text = response.text
            print(f"✓ Transcription successful!")
            print(f"  Original text: {transcribed_text}")
            
            return transcribed_text
        
        except Exception as e:
            raise Exception(f"Failed to transcribe audio: {str(e)}")
    
    def translate_text(self, text: str, target_language: str = "es") -> str:
        """
        Step 2: Translate text to target language using Google Translate.
        
        Args:
            text: Text to translate
            target_language: Target language code (e.g., 'es' for Spanish, 'fr' for French)
                           Common codes: en, es, fr, de, it, pt, ru, ja, zh-CN
        
        Returns:
            Translated text
        
        Raises:
            Exception: If translation fails
        """
        print(f"\n[Step 2/4] Translating text to '{target_language}'")
        
        try:
            # Use deep-translator's GoogleTranslator for free translation
            translator = GoogleTranslator(source='auto', target=target_language)
            translated_text = translator.translate(text)
            
            print(f"✓ Translation successful!")
            print(f"  Translated text: {translated_text}")
            
            return translated_text
        
        except Exception as e:
            raise Exception(f"Failed to translate text: {str(e)}")
    
    def text_to_speech(
        self, 
        text: str, 
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Default: Rachel (ElevenLabs)
        output_filename: str = "output.mp3"
    ) -> str:
        """
        Step 3: Convert text to speech using ElevenLabs API.
        
        Args:
            text: Text to convert to speech
            voice_id: ElevenLabs voice ID. Popular options:
                     - "21m00Tcm4TlvDq8ikWAM" (Rachel - female, American)
                     - "AZnzlk1XvdvUeBnXmlld" (Domi - female, American)
                     - "EXAVITQu4vr4xnSDxMaL" (Bella - female, American)
                     - "ErXwobaYiN019PkySvjV" (Antoni - male, American)
                     - "MF3mGyEYCl7XYWbV9V6O" (Elli - female, American)
                     - "TxGEqnHWrfWFTfGW9XjX" (Josh - male, American)
            output_filename: Name for the output audio file
        
        Returns:
            Path to the generated audio file
        
        Raises:
            Exception: If text-to-speech conversion fails
        """
        print(f"\n[Step 3/4] Converting text to speech with voice: {voice_id}")
        
        try:
            # Generate speech using ElevenLabs API
            response = self.elevenlabs_client.text_to_speech.convert(
                voice_id=voice_id,
                optimize_streaming_latency=0,
                output_format="mp3_44100_128",
                text=text,
                model_id="eleven_multilingual_v2",  # Supports multiple languages
                voice_settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.75,
                    style=0.0,
                    use_speaker_boost=True,
                )
            )
            
            # Save the audio to a file
            output_path = self.output_dir / output_filename
            
            # Write the audio stream to file
            with open(output_path, "wb") as f:
                for chunk in response:
                    if chunk:
                        f.write(chunk)
            
            print(f"✓ Text-to-speech conversion successful!")
            print(f"  Audio saved to: {output_path}")
            
            return str(output_path)
        
        except Exception as e:
            raise Exception(f"Failed to convert text to speech: {str(e)}")
    
    def play_audio(self, audio_file_path: str) -> None:
        """
        Step 4: Play the audio file locally.
        
        Args:
            audio_file_path: Path to the audio file to play
        
        Raises:
            Exception: If audio playback fails
        """
        print(f"\n[Step 4/4] Playing audio file: {audio_file_path}")
        
        try:
            # Play the audio file
            playsound(audio_file_path)
            print(f"✓ Audio playback complete!")
        
        except Exception as e:
            print(f"⚠ Could not play audio automatically: {str(e)}")
            print(f"  You can manually play the file at: {audio_file_path}")
    
    def audio_translate_pipeline(
        self,
        file_path: str,
        target_lang: str = "es",
        voice: str = "21m00Tcm4TlvDq8ikWAM",
        play_audio: bool = True
    ) -> dict:
        """
        Complete pipeline: Audio → Transcription → Translation → Speech → Play
        
        This is the main function that orchestrates the entire workflow.
        
        Args:
            file_path: Path to the input audio file (WAV, MP3, etc.)
            target_lang: Target language code (e.g., 'es', 'fr', 'de')
            voice: ElevenLabs voice ID for speech synthesis
            play_audio: Whether to play the audio after generation
        
        Returns:
            Dictionary containing:
                - original_text: Transcribed text from input audio
                - translated_text: Text translated to target language
                - output_audio_path: Path to generated audio file
        
        Example:
            translator = AudioTranslator()
            result = translator.audio_translate_pipeline(
                file_path="sample.mp3",
                target_lang="es",
                voice="21m00Tcm4TlvDq8ikWAM"
            )
            print(f"Original: {result['original_text']}")
            print(f"Translated: {result['translated_text']}")
        """
        print("=" * 70)
        print("AUDIO TRANSLATION & RE-DUBBING PIPELINE")
        print("=" * 70)
        
        try:
            # Step 1: Transcribe the audio to text
            original_text = self.transcribe_audio(file_path)
            
            # Step 2: Translate the text to target language
            translated_text = self.translate_text(original_text, target_lang)
            
            # Step 3: Convert translated text to speech
            output_audio_path = self.text_to_speech(
                text=translated_text,
                voice_id=voice,
                output_filename=f"translated_{target_lang}.mp3"
            )
            
            # Step 4: Play the audio (optional)
            if play_audio:
                self.play_audio(output_audio_path)
            
            print("\n" + "=" * 70)
            print("PIPELINE COMPLETED SUCCESSFULLY!")
            print("=" * 70)
            
            # Return results
            return {
                "original_text": original_text,
                "translated_text": translated_text,
                "output_audio_path": output_audio_path
            }
        
        except Exception as e:
            print(f"\n✗ Pipeline failed: {str(e)}")
            raise


# Convenience function for quick usage
def audio_translate_pipeline(
    file_path: str,
    target_lang: str = "es",
    voice: str = "21m00Tcm4TlvDq8ikWAM"
) -> dict:
    """
    Quick access function for the audio translation pipeline.
    
    Args:
        file_path: Path to the input audio file
        target_lang: Target language code (default: 'es' for Spanish)
        voice: ElevenLabs voice ID (default: Rachel)
    
    Returns:
        Dictionary with original_text, translated_text, and output_audio_path
    
    Example:
        result = audio_translate_pipeline("my_audio.mp3", "fr", "21m00Tcm4TlvDq8ikWAM")
    """
    translator = AudioTranslator()
    return translator.audio_translate_pipeline(file_path, target_lang, voice)


if __name__ == "__main__":
    """
    Example usage and testing.
    
    To use this script:
    1. Place an audio file (WAV or MP3) in the project directory
    2. Update the file_path below
    3. Run: python audio_translator.py
    """
    
    # Example: Translate an audio file from English to Spanish
    # Uncomment and update the file path to test
    
    # result = audio_translate_pipeline(
    #     file_path="sample_audio.mp3",  # Your audio file
    #     target_lang="es",              # Spanish
    #     voice="21m00Tcm4TlvDq8ikWAM"   # Rachel voice
    # )
    
    print("\n" + "=" * 70)
    print("Audio Translation & Re-Dubbing App - Ready!")
    print("=" * 70)
    print("\nTo use this app, call the audio_translate_pipeline function:")
    print("\nExample:")
    print('  result = audio_translate_pipeline(')
    print('      file_path="your_audio.mp3",')
    print('      target_lang="es",  # Spanish')
    print('      voice="21m00Tcm4TlvDq8ikWAM"  # Rachel voice')
    print('  )')
    print("\nSupported languages: en, es, fr, de, it, pt, ru, ja, zh-CN, and more")
    print("\nPopular ElevenLabs voices:")
    print("  - 21m00Tcm4TlvDq8ikWAM (Rachel - female, American)")
    print("  - ErXwobaYiN019PkySvjV (Antoni - male, American)")
    print("  - EXAVITQu4vr4xnSDxMaL (Bella - female, American)")
    print("  - TxGEqnHWrfWFTfGW9XjX (Josh - male, American)")
    print("=" * 70)
