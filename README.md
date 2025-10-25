# Real-time Translation & Voice Re-Dubbing App

A Python application that transcribes audio, translates it to different languages, and generates natural-sounding speech using AI.

## Features

- 🎤 **Audio Transcription**: Convert speech to text using OpenAI Whisper API
- 🌍 **Translation**: Translate to 100+ languages using Google Translate
- 🗣️ **Voice Synthesis**: Generate natural-sounding speech with ElevenLabs
- 🔊 **Audio Playback**: Automatic playback of synthesized audio
- 🧩 **Modular Design**: Easy to extend with new features (e.g., live microphone input)

## Quick Start

### 1. Prerequisites

You need API keys for:
- **OpenAI API** (for Whisper transcription) - Get it at https://platform.openai.com/api-keys
- **ElevenLabs API** (for voice synthesis) - Get it at https://elevenlabs.io

### 2. Set Up API Keys

The API keys are already configured as environment secrets in Replit.

### 3. Basic Usage

```python
from audio_translator import audio_translate_pipeline

# Translate an audio file from English to Spanish
result = audio_translate_pipeline(
    file_path="your_audio.mp3",
    target_lang="es",
    voice="21m00Tcm4TlvDq8ikWAM"
)

print(f"Original: {result['original_text']}")
print(f"Translated: {result['translated_text']}")
print(f"Audio saved to: {result['output_audio_path']}")
```

## Supported Languages

Common language codes:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `zh-CN` - Chinese (Simplified)
- And 100+ more!

## ElevenLabs Voices

Popular pre-configured voices:

| Voice ID | Name | Gender | Accent |
|----------|------|--------|--------|
| `21m00Tcm4TlvDq8ikWAM` | Rachel | Female | American |
| `ErXwobaYiN019PkySvjV` | Antoni | Male | American |
| `EXAVITQu4vr4xnSDxMaL` | Bella | Female | American |
| `TxGEqnHWrfWFTfGW9XjX` | Josh | Male | American |
| `MF3mGyEYCl7XYWbV9V6O` | Elli | Female | American |

You can find more voices at: https://elevenlabs.io/voice-library

## Advanced Usage

### Using the AudioTranslator Class

```python
from audio_translator import AudioTranslator

translator = AudioTranslator()

# Step-by-step pipeline
original_text = translator.transcribe_audio("input.mp3")
translated_text = translator.translate_text(original_text, "fr")
output_path = translator.text_to_speech(translated_text, voice_id="21m00Tcm4TlvDq8ikWAM")
translator.play_audio(output_path)
```

### Translate to Multiple Languages

```python
from audio_translator import AudioTranslator

translator = AudioTranslator()
languages = ["es", "fr", "de", "it"]

for lang in languages:
    result = translator.audio_translate_pipeline(
        file_path="input.mp3",
        target_lang=lang,
        voice="21m00Tcm4TlvDq8ikWAM",
        play_audio=False
    )
    print(f"{lang}: {result['translated_text']}")
```

## File Structure

```
.
├── audio_translator.py    # Main pipeline implementation
├── example_usage.py       # Usage examples
├── README.md              # This file
├── replit.md              # Project documentation
└── temp_audio/            # Generated audio files (auto-created)
```

## How It Works

### Pipeline Steps

1. **Transcription**: Audio file → OpenAI Whisper API → Text
2. **Translation**: Original text → Google Translate → Translated text
3. **Synthesis**: Translated text → ElevenLabs API → Audio file
4. **Playback**: Audio file → Local playback

### Architecture

The app is designed with modularity in mind:

- `AudioTranslator` class handles all operations
- Each step (transcribe, translate, synthesize, play) is a separate method
- Easy to extend with new features like:
  - Live microphone input
  - Batch processing
  - Different translation services
  - Custom voice models

## Supported Audio Formats

**Input**: WAV, MP3, M4A, FLAC, OGG (anything OpenAI Whisper supports)
**Output**: MP3 (44.1kHz, 128kbps)

## Error Handling

The app includes comprehensive error handling:

```python
try:
    result = audio_translate_pipeline("file.mp3", "es")
except FileNotFoundError:
    print("Audio file not found!")
except Exception as e:
    print(f"Error: {e}")
```

## Future Enhancements

Potential features to add:
- 🎙️ Live microphone input for real-time translation
- 📁 Batch processing for multiple files
- 🔄 Additional translation services (DeepL, Azure)
- 💾 Save output files with custom naming
- 🌐 Web interface with Flask/FastAPI
- ⚡ Streaming audio generation

## Dependencies

- `openai` - Whisper API for transcription
- `elevenlabs` - Text-to-speech synthesis
- `deep-translator` - Google Translate integration
- `pydub` - Audio file processing
- `playsound3` - Audio playback
- `requests` - HTTP requests

## Troubleshooting

### Audio doesn't play automatically
The audio file is still saved to `temp_audio/` directory. You can play it manually.

### "API key not found" error
Make sure your environment secrets are properly configured with `OPENAI_API_KEY` and `ELEVENLABS_API_KEY`.

### "File not found" error
Check that your audio file path is correct and the file exists.

### Translation quality issues
Try different target languages or check the original transcription for accuracy.

## License

This project is open source and available for educational and commercial use.

## Support

For issues or questions:
1. Check the example scripts in `example_usage.py`
2. Review the inline documentation in `audio_translator.py`
3. Consult API documentation:
   - OpenAI: https://platform.openai.com/docs
   - ElevenLabs: https://elevenlabs.io/docs
