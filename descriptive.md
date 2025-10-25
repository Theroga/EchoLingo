# Audio Translation & Voice Re-Dubbing App

## Project Overview

A Python-based application that provides a complete pipeline for translating and re-dubbing audio files in different languages. The app transcribes speech, translates it, and generates natural-sounding voice synthesis using AI.


## Purpose

Enable users to:
1. Take pre-recorded audio files (WAV, MP3, etc.)
2. Automatically transcribe speech to text
3. Translate to any target language
4. Generate natural-sounding speech in the target language
5. Play back the translated audio

## Recent Changes

Initial Implementation
- ✅ Set up Python 3.11 environment
- ✅ Integrated OpenAI API for Whisper transcription// changed to google cloud to speech text.
- ✅ Integrated ElevenLabs API for voice synthesis
- ✅ Implemented Google Translate via deep-translator (compatible alternative to googletrans)
- ✅ Created modular AudioTranslator class with complete pipeline
- ✅ Added comprehensive error handling and logging
- ✅ Created example usage scripts and documentation
- ✅ Installed dependencies: openai, elevenlabs, deep-translator, pydub, playsound3

## Project Architecture

### Core Components

**audio_translator.py** - Main implementation
- `AudioTranslator` class: Handles complete translation pipeline
- `transcribe_audio()`: OpenAI Whisper API integration
- `translate_text()`: Google Translate via deep-translator
- `text_to_speech()`: ElevenLabs voice synthesis
- `play_audio()`: Local audio playback
- `audio_translate_pipeline()`: Complete workflow orchestration

**example_usage.py** - Usage examples
- Basic single-file translation
- Multi-language translation
- Different voice options
- Error handling patterns

### Dependencies

**Python Libraries**:
- `openai>=2.6.1` - Whisper API for transcription
- `elevenlabs>=2.20.1` - Text-to-speech synthesis
- `deep-translator>=1.11.4` - Translation service (Google Translate)
- `pydub>=0.25.1` - Audio file handling
- `playsound3>=3.2.8` - Audio playback
- `requests>=2.32.5` - HTTP requests

**System Dependencies**:
- `ffmpeg` - Audio format conversion and processing

### API Integrations

1. **OpenAI API (Whisper)**
   - Purpose: Speech-to-text transcription
   - Model: whisper-1
   - Environment: `OPENAI_API_KEY`

2. **ElevenLabs API**
   - Purpose: Text-to-speech synthesis
   - Model: eleven_multilingual_v2
   - Environment: `ELEVENLABS_API_KEY`

3. **Google Translate**
   - Purpose: Text translation
   - Provider: deep-translator library (free, no API key required)
   - Supports: 100+ languages

## User Preferences

### Development Workflow
- Modular, well-commented code
- Clear separation of pipeline steps
- Comprehensive error handling
- Extensible architecture for future features

### Code Style
- Type hints for function parameters
- Docstrings for all public methods
- Clear variable naming
- Print statements for pipeline progress

## Technical Decisions

### Translation Library Choice
**Decision**: Use `deep-translator` instead of `googletrans`
**Reason**: 
- `googletrans==4.0.0rc1` has dependency conflict with OpenAI library (httpx version mismatch)
- `deep-translator` is actively maintained (2024)
- Works with modern OpenAI library versions
- Provides same Google Translate functionality without API key

### Audio Playback Library
**Decision**: Use `playsound3` instead of `playsound`
**Reason**:
- Original `playsound` has build issues with Python 3.11
- `playsound3` is actively maintained (October 2025)
- Cross-platform support
- Background playback capabilities

### Voice Synthesis Service
**Decision**: Use ElevenLabs for TTS
**Reason**:
- High-quality, natural-sounding voices
- Multilingual support
- Simple API integration
- Good voice variety

## Directory Structure

```
.
├── audio_translator.py      # Main pipeline implementation
├── example_usage.py          # Usage examples and demos
├── README.md                 # User-facing documentation
├── replit.md                 # This file - project memory
├── .gitignore               # Git ignore rules
├── temp_audio/              # Generated audio outputs (auto-created)
└── pyproject.toml           # Python dependencies (auto-managed)
```

## Supported Features

### Current (MVP)
- ✅ Audio file input (WAV, MP3, M4A, FLAC, OGG)
- ✅ Speech-to-text transcription
- ✅ Multi-language translation (100+ languages)
- ✅ Text-to-speech synthesis
- ✅ Local audio playback
- ✅ Modular pipeline function
- ✅ Multiple voice options
- ✅ Error handling and logging

### Planned (Future Enhancements)
- 🔄 Live microphone input for real-time translation
- 🔄 Batch processing for multiple files
- 🔄 Additional translation services (DeepL, Azure)
- 🔄 Web interface (Flask/FastAPI)
- 🔄 Streaming audio generation
- 🔄 Custom voice training
- 🔄 CLI interface with argparse

## Language Support

Common language codes:
- English: `en`
- Spanish: `es`
- French: `fr`
- German: `de`
- Italian: `it`
- Portuguese: `pt`
- Russian: `ru`
- Japanese: `ja`
- Chinese: `zh-CN`
- And 100+ more via Google Translate

## Voice Options (ElevenLabs)

Pre-configured voices:
- Rachel (Female, American): `21m00Tcm4TlvDq8ikWAM`
- Antoni (Male, American): `ErXwobaYiN019PkySvjV`
- Bella (Female, American): `EXAVITQu4vr4xnSDxMaL`
- Josh (Male, American): `TxGEqnHWrfWFTfGW9XjX`
- Elli (Female, American): `MF3mGyEYCl7XYWbV9V6O`

## Environment Variables

Required secrets (configured in Replit):
- `OPENAI_API_KEY` - OpenAI API key for Whisper
- `ELEVENLABS_API_KEY` - ElevenLabs API key for TTS

## Usage Examples

### Basic Usage
```python
from audio_translator import audio_translate_pipeline

result = audio_translate_pipeline(
    file_path="audio.mp3",
    target_lang="es",
    voice="21m00Tcm4TlvDq8ikWAM"
)
```

### Advanced Usage
```python
from audio_translator import AudioTranslator

translator = AudioTranslator()
result = translator.audio_translate_pipeline(
    file_path="audio.mp3",
    target_lang="fr",
    voice="ErXwobaYiN019PkySvjV",
    play_audio=False
)
```

## Known Issues & Limitations

1. **Audio Playback**: May not work in all environments (server-based). Files are saved to `temp_audio/` for manual playback.
2. **API Rate Limits**: OpenAI and ElevenLabs have usage limits based on subscription tier.
3. **Translation Accuracy**: Depends on Google Translate quality; may vary by language pair.
4. **Audio Format**: Input must be in a format supported by OpenAI Whisper.

## Performance Considerations

- Transcription speed: ~10-30 seconds for 1-minute audio
- Translation speed: Nearly instant
- Voice synthesis: ~5-15 seconds depending on text length
- Total pipeline: ~30-60 seconds for 1-minute audio

## Future Development Notes

### Easy Additions
1. **Live Microphone Input**: Use `pyaudio` or `sounddevice` for recording
2. **Batch Processing**: Add loop over directory of files
3. **CLI Interface**: Use `argparse` for command-line usage
4. **Web Interface**: Flask app with file upload

### Architectural Considerations
- Pipeline is modular - each step can be swapped independently
- Easy to add new translation services
- Voice synthesis can be replaced with other providers
- Transcription could use other models (Azure, Google Cloud)

## Maintenance Log

Reason |
--------|
Initial setup | Project creation |
Chose deep-translator | Dependency compatibility |
Chose playsound3 | Build compatibility |
Added ffmpeg | Audio processing support |
