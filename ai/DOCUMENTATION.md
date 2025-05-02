# AI Multimedia Generator - Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup Guide](#setup-guide)
4. [Usage Guide](#usage-guide)
5. [API Integration](#api-integration)
6. [Troubleshooting](#troubleshooting)
7. [Security Notes](#security-notes)

## Introduction
The AI Multimedia Generator is a web application that allows users to generate various types of media content using artificial intelligence. The application provides a user-friendly interface for generating text, images, audio, and video content through different AI APIs.

## Features

### 1. Text Generation
- Uses Replicate's Llama 2 model
- Generates creative and informative text content
- Supports various text formats and styles
- Maximum length: 500 characters

### 2. Image Generation
- Powered by Stability AI
- High-quality image generation (1024x1024)
- Supports detailed image descriptions
- Output format: PNG

### 3. Audio Generation
- Uses ElevenLabs text-to-speech
- Natural-sounding voice synthesis
- Customizable voice settings
- Output format: MP3

### 4. Video Generation
- Powered by Replicate's Stable Video Diffusion
- Generates short video clips (25 frames)
- Resolution: 1024x576
- Output format: MP4

## Setup Guide

### Prerequisites
- Python 3.8 or higher
- Git (for version control)
- API keys for:
  - ElevenLabs
  - Replicate
  - Stability AI

### Installation Steps
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd ai-multimedia-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create environment file:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     ELEVENLABS_API_KEY=your_key_here
     REPLICATE_API_KEY=your_key_here
     STABILITY_API_KEY=your_key_here
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

### Text Generation
1. Select "Text" mode from the sidebar
2. Enter your prompt in the text area
3. Click "Generate Text"
4. View and copy the generated text

### Image Generation
1. Select "Image" mode
2. Enter a detailed image description
3. Click "Generate Image"
4. View and download the generated image

### Audio Generation
1. Select "Audio" mode
2. Enter the text you want to convert to speech
3. Click "Generate Audio"
4. Listen to and download the generated audio

### Video Generation
1. Select "Video" mode
2. Enter a detailed video description
3. Click "Generate Video"
4. View and download the generated video

## API Integration

### ElevenLabs API
- Used for text-to-speech conversion
- Default voice ID: "21m00Tcv4TlvDq8ikWAM"
- Voice settings: stability=0.5, similarity_boost=0.5

### Replicate API
- Used for text and video generation
- Text model: Llama 2
- Video model: Stable Video Diffusion

### Stability AI API
- Used for image generation
- Model: Stable Diffusion XL
- Resolution: 1024x1024
- Steps: 30

### API Limitations and Management
1. **Token Limitations**
   - Each API service has usage limits and quotas
   - Tokens may expire or be exhausted after reaching limits
   - Free tiers typically have lower limits than paid plans

2. **Common Challenges**
   - Token exhaustion is a common issue with AI services
   - Different APIs have different rate limits
   - Some services charge per request or have monthly quotas
   - Token refresh policies vary between providers

3. **Best Practices**
   - Monitor token usage regularly
   - Implement error handling for token exhaustion
   - Consider implementing caching for frequent requests
   - Keep track of API costs and usage patterns

4. **Current Implementation**
   - API keys are stored securely in environment variables
   - Error messages indicate when tokens are exhausted
   - Clear feedback is provided to users about API status
   - Documentation includes information about token requirements

5. **Alternative Solutions**
   - Consider implementing token rotation
   - Use multiple API keys if available
   - Implement fallback mechanisms
   - Cache successful responses when possible

## Troubleshooting

### Common Issues
1. **API Key Errors**
   - Ensure all API keys are correctly set in `.env`
   - Check if API keys are valid and have sufficient credits

2. **Generation Failures**
   - Check internet connection
   - Verify API service status
   - Ensure prompts are appropriate for the selected mode

3. **File Access Issues**
   - Check file permissions
   - Ensure sufficient disk space
   - Verify output directory exists

### Error Messages
- "API Key not found": Check `.env` file
- "Generation failed": Check API status and credits
- "File not found": Check file paths and permissions

## Security Notes

### API Key Security
- Never share your API keys
- Keep `.env` file out of version control
- Use environment variables in production

### Data Privacy
- Generated content is not stored permanently
- API providers may store prompts temporarily
- Review API providers' privacy policies

### Best Practices
1. Regularly rotate API keys
2. Monitor API usage
3. Set appropriate rate limits
4. Keep software dependencies updated

## Support
For additional support or questions, please contact:
- Name: LOVE PAUL
- Course: CSC 507
- Student ID: CSC/19U/3992 