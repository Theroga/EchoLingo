"""
Main entry point for Audio Translation & Voice Re-Dubbing App

This script demonstrates that the application is ready to use.
To actually use the app, see example_usage.py or import audio_translate_pipeline.
"""

import os
import sys

def check_environment():
    """Check if all required environment variables are set."""
    print("=" * 70)
    print("AUDIO TRANSLATION & RE-DUBBING APP")
    print("=" * 70)
    print("\n[Environment Check]")
    
    required_keys = ["OPENAI_API_KEY", "ELEVENLABS_API_KEY"]
    missing_keys = []
    
    for key in required_keys:
        if os.environ.get(key):
            print(f"✓ {key} is set")
        else:
            print(f"✗ {key} is missing")
            missing_keys.append(key)
    
    if missing_keys:
        print(f"\n⚠ Warning: Missing API keys: {', '.join(missing_keys)}")
        print("Please set them in Replit Secrets to use the app.")
        return False
    
    print("\n✓ All environment variables are configured!")
    return True


def check_dependencies():
    """Check if all required packages are installed."""
    print("\n[Dependency Check]")
    
    packages = {
        "openai": "OpenAI API client",
        "elevenlabs": "ElevenLabs TTS client",
        "deep_translator": "Translation service",
        "pydub": "Audio processing",
        "playsound3": "Audio playback"
    }
    
    all_installed = True
    
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✓ {package} - {description}")
        except ImportError:
            print(f"✗ {package} - {description} (NOT INSTALLED)")
            all_installed = False
    
    if not all_installed:
        print("\n⚠ Some packages are missing. Run: uv add <package-name>")
        return False
    
    print("\n✓ All dependencies are installed!")
    return True


def show_usage():
    """Display usage instructions."""
    print("\n" + "=" * 70)
    print("HOW TO USE THIS APP")
    print("=" * 70)
    
    print("\n1. BASIC USAGE (Python):")
    print("   " + "-" * 66)
    print("   from audio_translator import audio_translate_pipeline")
    print()
    print("   result = audio_translate_pipeline(")
    print('       file_path="your_audio.mp3",  # Your audio file')
    print('       target_lang="es",             # Target language (Spanish)')
    print('       voice="21m00Tcm4TlvDq8ikWAM" # ElevenLabs voice ID')
    print("   )")
    print()
    print("   print(f\"Original: {result['original_text']}\")")
    print("   print(f\"Translated: {result['translated_text']}\")")
    
    print("\n2. SUPPORTED LANGUAGES:")
    print("   " + "-" * 66)
    print("   es=Spanish, fr=French, de=German, it=Italian, pt=Portuguese,")
    print("   ru=Russian, ja=Japanese, zh-CN=Chinese, and 100+ more!")
    
    print("\n3. VOICE OPTIONS:")
    print("   " + "-" * 66)
    print("   21m00Tcm4TlvDq8ikWAM - Rachel (Female, American)")
    print("   ErXwobaYiN019PkySvjV - Antoni (Male, American)")
    print("   EXAVITQu4vr4xnSDxMaL - Bella (Female, American)")
    print("   TxGEqnHWrfWFTfGW9XjX - Josh (Male, American)")
    
    print("\n4. MORE EXAMPLES:")
    print("   " + "-" * 66)
    print("   See example_usage.py for detailed examples including:")
    print("   - Multi-language translation")
    print("   - Different voice options")
    print("   - Error handling")
    print("   - Advanced usage patterns")
    
    print("\n5. DOCUMENTATION:")
    print("   " + "-" * 66)
    print("   - README.md: Complete user guide")
    print("   - audio_translator.py: Full API documentation")
    print("   - replit.md: Project memory and architecture")
    
    print("\n" + "=" * 70)
    print("✓ App is ready to use!")
    print("=" * 70)


def main():
    """Main function."""
    try:
        env_ok = check_environment()
        deps_ok = check_dependencies()
        
        if env_ok and deps_ok:
            print("\n" + "=" * 70)
            print("✓✓✓ SYSTEM READY ✓✓✓")
            print("=" * 70)
        else:
            print("\n" + "=" * 70)
            print("⚠ SETUP INCOMPLETE")
            print("=" * 70)
            print("\nPlease complete the setup before using the app.")
        
        show_usage()
        
        return 0
    
    except Exception as e:
        print(f"\n✗ Error during startup: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
