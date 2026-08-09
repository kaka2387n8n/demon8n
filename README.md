# 🎬 YouTube Content Automation Pipeline

**AI-Powered Workflow for Scraping, Rewriting, and Regenerating YouTube Videos**

Automatically:
1. 🔗 Scrape YouTube video content (metadata, transcripts)
2. ✍️ Rewrite content using AI (OpenAI/Claude)
3. 🎙️ Generate voiceovers (ElevenLabs)
4. 🎨 Create new videos (editing, thumbnails)
5. 📤 Upload to YouTube (automated publishing)

---

## 🚀 Quick Start

### Prerequisites
- n8n (self-hosted or cloud)
- YouTube API key
- OpenAI API key
- ElevenLabs API key

### Installation

1. **Clone/Fork this repo**
   ```bash
   git clone https://github.com/kaka2387n8n/demon8n.git
   cd demon8n
   ```

2. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Import workflow into n8n**
   - Go to n8n dashboard
   - Click "Import Workflow"
   - Select `workflows/youtube-automation-main.json`
   - Configure credentials
   - Deploy!

---

## 📋 Workflow Steps

### 1. Webhook Trigger
Receive YouTube video URL
```json
{
  "videoId": "dQw4w9WgXcQ",
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

### 2. Extract Metadata
Get video title, description, channel name

### 3. Process Transcript
Extract and chunk video transcript

### 4. Rewrite with AI
Use OpenAI to rewrite content

### 5. Generate Voiceover
Convert text to speech (ElevenLabs)

### 6. Prepare Metadata
Generate SEO-optimized title, description, tags

### 7. Log Results
Track workflow execution

---

## 🔧 Configuration

### YouTube API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project
3. Enable YouTube Data API v3
4. Create OAuth 2.0 credentials
5. Get API key and refresh token

### OpenAI API Setup
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create API key
3. Add to `.env` file

### ElevenLabs Setup
1. Create account at [ElevenLabs](https://elevenlabs.io/)
2. Get API key
3. Choose voice ID
4. Add to `.env` file

---

## 📊 Use Cases

✅ **Content Repurposing** - Turn 1 video into multiple versions
✅ **Multi-language Support** - Translate and regenerate
✅ **Batch Processing** - Process hundreds of videos
✅ **SEO Optimization** - AI-generated metadata
✅ **Social Media Clips** - Create short-form content
✅ **Archive Management** - Organize and enhance old content

---

## 📁 Project Structure

```
demon8n/
├── workflows/
│   └── youtube-automation-main.json     # Main n8n workflow
├── scripts/
│   ├── video-editor.py
│   ├── tts-generator.py
│   └── requirements.txt
├── config/
│   └── credentials.template.json
├── .env.example
├── README.md
├── ARCHITECTURE.md
└── SETUP_GUIDE.md
```

---

## 🔌 API Integration

- **YouTube API** - Video data & upload
- **OpenAI** - Content rewriting
- **ElevenLabs** - Voice generation
- **Google Cloud** - Alternative TTS

---

## 📈 Performance

- ⚡ Process 10+ videos/hour
- 💾 Optimize for cost efficiency
- 🔄 Automatic retry on failure
- 📊 Real-time monitoring

---

## 🐛 Troubleshooting

### YouTube API Key Invalid
- Verify API key in Google Cloud Console
- Check YouTube Data API v3 is enabled
- Verify key permissions

### OpenAI Rate Limit
- Use gpt-3.5-turbo instead (faster, cheaper)
- Implement queue for batch processing
- Reduce max_tokens

### Voice Upload Fails
- Verify OAuth2 refresh token
- Check YouTube account permissions
- Ensure video metadata is complete

---

## 📝 Next Steps

1. Import workflow into n8n
2. Add API credentials
3. Test with sample video
4. Deploy to production
5. Monitor and optimize

---

## 📞 Support

Questions? Issues?
- 📖 See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed setup
- 🏗️ See [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- 🐛 Report bugs via GitHub Issues

---

**Made with ❤️ by AI Automation Experts**