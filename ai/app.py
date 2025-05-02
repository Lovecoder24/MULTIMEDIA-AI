import streamlit as st
import os
from ai import generate_text, generate_image, generate_audio, generate_video

def format_text_output(text):
    """Format the text output with better styling similar to ChatGPT"""
    st.markdown("---")
    st.markdown("### 📝 Generated Content")
    
    # Create a container with custom styling
    with st.container():
        st.markdown("""
        <style>
        .chat-output {
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #e1e4e8;
            margin: 10px 0;
            color: #24292e;
            font-size: 16px;
            line-height: 1.6;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .chat-output p {
            margin-bottom: 1em;
        }
        
        .chat-output code {
            background-color: #f6f8fa;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
            font-size: 85%;
        }
        
        .chat-output pre {
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 1em 0;
        }
        
        .chat-output ul, .chat-output ol {
            margin: 1em 0;
            padding-left: 2em;
        }
        
        .chat-output li {
            margin: 0.5em 0;
        }
        
        .chat-output blockquote {
            border-left: 3px solid #e1e4e8;
            color: #6a737d;
            padding-left: 1em;
            margin: 1em 0;
        }
        
        .chat-output h1, .chat-output h2, .chat-output h3 {
            margin: 1.5em 0 0.5em 0;
            font-weight: 600;
        }
        
        .chat-output table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        
        .chat-output th, .chat-output td {
            border: 1px solid #e1e4e8;
            padding: 8px;
            text-align: left;
        }
        
        .chat-output th {
            background-color: #f6f8fa;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Process the text to handle markdown and code blocks
        processed_text = text
        # Replace code blocks with proper formatting
        if '```' in text:
            processed_text = text.replace('```python', '<pre><code class="language-python">').replace('```', '</code></pre>')
        
        # Display the text in a container
        text_container = st.container()
        with text_container:
            st.markdown(f'<div class="chat-output">{processed_text}</div>', unsafe_allow_html=True)
        
        # Add copy button with improved styling
        col1, col2 = st.columns([6, 1])
        with col2:
            if st.button("📋 Copy", use_container_width=True):
                st.toast("✅ Copied to clipboard!", icon="✂️")
                st.markdown(f"""
                    <script>
                        navigator.clipboard.writeText(`{text}`);
                    </script>
                    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="AI Multimedia Generator",
        page_icon="🎨",
        layout="wide"
    )
    
    # Title and Description
    st.title("AI Multimedia Generator 🎨🎤📹")
    st.markdown("""
    <style>
    .main-header {
        font-size: 20px;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="main-header">Generate Text, Images, Audio, and Video using AI</p>', unsafe_allow_html=True)
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # Sidebar for mode selection
        st.markdown("### Generation Mode")
        mode = st.radio("Select Mode", ["Text", "Image", "Audio", "Video"])
        
        # Main prompt input
        st.markdown("### Enter Your Prompt")
        prompt = st.text_area(
            "Be descriptive for better results!",
            height=150,
            placeholder="Example: Write a creative story about a magical forest..."
        )
        
        if st.button(f"🚀 Generate {mode}", use_container_width=True):
            if not prompt:
                st.warning("⚠️ Please enter a prompt first!")
                return
                
            with st.spinner(f"✨ Generating {mode.lower()}... Please wait."):
                try:
                    if mode == "Text":
                        result = generate_text(prompt)
                        with col2:
                            format_text_output(result)
                        
                    elif mode == "Image":
                        result = generate_image(prompt)
                        with col2:
                            st.markdown("### 🖼️ Generated Image")
                            if os.path.exists("output_image.png"):
                                st.image("output_image.png", caption="Generated Image", use_column_width=True)
                            else:
                                st.error("Failed to generate image")
                        
                    elif mode == "Audio":
                        result = generate_audio(prompt)
                        with col2:
                            st.markdown("### 🎵 Generated Audio")
                            if os.path.exists("output_audio.mp3"):
                                st.audio("output_audio.mp3")
                            else:
                                st.error("Failed to generate audio")
                        
                    elif mode == "Video":
                        result = generate_video(prompt)
                        with col2:
                            st.markdown("### 🎬 Generated Video")
                            if os.path.exists("output_video.mp4"):
                                st.video("output_video.mp4")
                            else:
                                st.error("Failed to generate video")
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    # Display API Information in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔧 API Information")
    st.sidebar.markdown("""
    This project uses:
    - 🤖 Replicate API (Llama 2) for Text
    - 🎨 Stability AI for Images
    - 🎤 ElevenLabs for Audio
    - 📹 Replicate API for Video
    """)
    
    # Display Assignment Information
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 Assignment Information")
    st.sidebar.markdown("""
    👤 Created by: LOVE PAUL  
    📚 COURSE: CSC 507  
    🆔 Student ID: CSC/19U/3992
    """)

if __name__ == "__main__":
    main()

