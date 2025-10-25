"""
Example Usage Script for Audio Translation & Re-Dubbing App

This script demonstrates how to use the audio translation pipeline
with different languages and voices.
"""

from audio_translator import audio_translate_pipeline, AudioTranslator


def example_basic_usage():
    """
    Basic example: Translate an audio file to Spanish
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Usage - English to Spanish")
    print("=" * 70)
    
    # Simple one-line usage
    result = audio_translate_pipeline(
        file_path="sample_audio.mp3",  # Replace with your audio file
        target_lang="es",               # Spanish
        voice="21m00Tcm4TlvDq8ikWAM"    # Rachel voice
    )
    
    print(f"\nOriginal: {result['original_text']}")
    print(f"Spanish: {result['translated_text']}")
    print(f"Output saved to: {result['output_audio_path']}")


def example_multiple_languages():
    """
    Advanced example: Translate the same audio to multiple languages
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Translate to Multiple Languages")
    print("=" * 70)
    
    translator = AudioTranslator()
    audio_file = "sample_audio.mp3"  # Replace with your audio file
    
    # Define target languages
    languages = {
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese"
    }
    
    results = {}
    
    for lang_code, lang_name in languages.items():
        print(f"\n--- Translating to {lang_name} ---")
        
        result = translator.audio_translate_pipeline(
            file_path=audio_file,
            target_lang=lang_code,
            voice="21m00Tcm4TlvDq8ikWAM",
            play_audio=False  # Don't auto-play each one
        )
        
        results[lang_name] = result
        print(f"{lang_name}: {result['translated_text']}")
    
    return results


def example_different_voices():
    """
    Example: Use different ElevenLabs voices
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Different Voices")
    print("=" * 70)
    
    translator = AudioTranslator()
    audio_file = "sample_audio.mp3"  # Replace with your audio file
    
    # Different voices for different translations
    voices = {
        "Rachel (Female)": "21m00Tcm4TlvDq8ikWAM",
        "Antoni (Male)": "ErXwobaYiN019PkySvjV",
        "Bella (Female)": "EXAVITQu4vr4xnSDxMaL",
        "Josh (Male)": "TxGEqnHWrfWFTfGW9XjX"
    }
    
    for voice_name, voice_id in voices.items():
        print(f"\n--- Using voice: {voice_name} ---")
        
        result = translator.audio_translate_pipeline(
            file_path=audio_file,
            target_lang="es",
            voice=voice_id,
            play_audio=False
        )
        
        print(f"Output: {result['output_audio_path']}")


def example_error_handling():
    """
    Example: Proper error handling
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Error Handling")
    print("=" * 70)
    
    translator = AudioTranslator()
    
    try:
        result = translator.audio_translate_pipeline(
            file_path="nonexistent_file.mp3",
            target_lang="es",
            voice="21m00Tcm4TlvDq8ikWAM"
        )
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Pipeline error: {e}")


def main():
    """
    Main function to run examples.
    
    Uncomment the examples you want to run.
    """
    print("\n" + "=" * 70)
    print("AUDIO TRANSLATION & RE-DUBBING - EXAMPLES")
    print("=" * 70)
    print("\nBefore running these examples:")
    print("1. Make sure you have an audio file (WAV or MP3)")
    print("2. Update 'sample_audio.mp3' with your file path")
    print("3. Ensure OPENAI_API_KEY and ELEVENLABS_API_KEY are set")
    print("\nUncomment the examples below to run them:")
    print("=" * 70)
    
    # Uncomment to run examples:
    
    # example_basic_usage()
    # example_multiple_languages()
    # example_different_voices()
    # example_error_handling()
    
    print("\n✓ Ready to use! Edit this file to run examples.")


if __name__ == "__main__":
    main()
