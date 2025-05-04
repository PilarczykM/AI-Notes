# Module 4: Generative AI - Audio  

## Topics Covered  
- **How Generative AI Models for Audio, Voice, and Music Work**  
- **Use Case 1:** Music generation with Audiocraft  
- **Use Case 2:** Voice cloning with Bark/Suno  
- **Use Case 3:** Text-to-Speech (TTS) with Parler  

## Learning Outcomes  
By the end of this module, you will be able to:  
✅ Explain how **Generative AI models** for audio, voice, and music work, describing fundamental principles and techniques.  
✅ Use **Audiocraft** to generate original music, demonstrating the ability to create AI-powered compositions.  
✅ Apply **Bark/Suno** for **voice cloning**, showcasing the ability to generate realistic voice replicas.  
✅ Utilize **Text-to-Speech (TTS)** technology with **Parler**, transforming text into natural-sounding speech.  
✅ Customize generative models for specific audio and music-related tasks, optimizing them to achieve desired sound effects.  

## Example Projects
### 🛠 Lab Exercises & Applications  
- **Automated Voice Generation:** Convert text into natural-sounding speech, replacing traditional narration.  
- **Multilingual Subtitles & Audio Descriptions:** Automatically generate subtitles in multiple languages, including descriptions for visually impaired users.  
- **Soundtrack & Jingle Creation:** Generate background music, jingles, and sound effects for ads and video productions.  

This module provides a hands-on approach to **creating and optimizing AI-generated audio, voice, and music** for various applications. 🎵🎙️🚀  

## Projects
- **[Lab 1](./src/lab_1/pl/lab_1.ipynb) - Text transcription from audio file**  
  - **Model:** whisper-base
  - **Tools:** openai-whisper
- **[Lab 2](./src/lab_2/pl/lab_2.ipynb) - TTS (Text to Speech)**  
  - **Model:** parler-tts/parler-tts-mini-v1
  - **Tools:** parler-tts transformers soundfile
- **[Lab 3](./src/lab_3/pl/lab_3_transformers.ipynb) - Create music based on description, modify audio with description**  
  - **Model:** nateraw/musicgen-songstarter-v0.2
  - **Tools:** audiocraft transformers
- **[Lab 4](./src/lab_4/pl/lab_4.ipynb) - Read text with accents**  
  - **Model:** From checkpoints*
  - **Tools:** transformers accelerate openvoice MeloTTS
- **[Lab 5](./src/lab_5/pl/lab_5.ipynb) - Podcast**  
  - **Model:** Qwen/Qwen2.5-1.5B-Instruc *
  - **Tools:** langchain-huggingface langchain-text-splitters langchain-community pypdf **kokoro>=0.3.4** soundfile pydub
