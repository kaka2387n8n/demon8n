# 🏗️ Architecture Overview

## System Design

```
YouTube Video
     ↓
Extract Metadata + Transcript
     ↓
AI Rewriting (OpenAI)
     ↓
Text-to-Speech (ElevenLabs)
     ↓
Video Editing (FFmpeg)
     ↓
Metadata Preparation
     ↓
YouTube Upload
     ↓
Monitoring & Logging
```

---

## Component Breakdown

### 1. INPUT LAYER
- Webhook Trigger (receive YouTube URL)
- Scheduled Job (daily/weekly)
- Manual Trigger (UI)

### 2. DATA EXTRACTION LAYER
- **YouTube API**
  - Video Metadata (title, description, duration)
  - Channel Info (name, subscribers)
  - Engagement Metrics (likes, views, comments)

- **Transcript Extraction**
  - Auto-generated captions
  - Manual captions
  - Multi-language support

### 3. CONTENT PROCESSING LAYER
- **Text Preprocessing**
  - Chunking (split into ~500 words)
  - Cleaning (remove filler words)
  - Sentiment Analysis
  - Keyword Extraction

- **AI Content Rewriting**
  - Style options: blog, script, social media, educational
  - Language options: English, Spanish, French, etc.
  - Tone: professional, casual, technical
  - SEO optimization

- **Quality Assurance**
  - Grammar check
  - Plagiarism detection
  - Length verification
  - Fact checking (optional)

### 4. MEDIA GENERATION LAYER
- **Text-to-Speech**
  - ElevenLabs/Google Cloud TTS
  - Voice selection (50+ natural voices)
  - Language & accent customization
  - Audio quality (MP3, WAV)

- **Video Generation**
  - Avatar video (AI presenter)
  - Stock footage integration
  - Animation & transitions
  - Background music & effects

- **Subtitle Generation**
  - Auto-generated from audio
  - Multi-language subtitles
  - Styling & positioning

- **Thumbnail Generation**
  - AI-generated based on content
  - Custom template selection
  - Text overlay optimization

### 5. METADATA PREPARATION LAYER
- SEO Optimization (keywords, tags, description)
- Category Selection
- Privacy Settings (public/private/unlisted)
- Scheduling (publish time optimization)
- Playlist Assignment

### 6. UPLOAD & PUBLISHING LAYER
- YouTube API Upload (OAuth2)
- Video Processing Status Tracking
- CDN Optimization
- Thumbnail Set
- Subtitle Upload
- Playlist Management

### 7. MONITORING & ANALYTICS LAYER
- Workflow Execution Tracking
- Error Handling & Retry Logic
- Performance Metrics
- Video Analytics (views, watch time, engagement)
- Cost Tracking (API usage)
- Notifications (Slack, Email, Discord)

---

## Technology Stack

### Orchestration
- **n8n** - Workflow automation
- **Node.js** - Backend processing

### APIs
- **YouTube Data API v3**
- **OpenAI API**
- **ElevenLabs API**
- **Google Cloud TTS**

### Video Processing
- **FFmpeg** - Video encoding/editing
- **RunwayML** - AI video generation
- **Synthesia** - Avatar creation

### Database
- **PostgreSQL** - Primary database
- **MongoDB** - NoSQL alternative
- **Redis** - Caching & queue

### Storage
- **AWS S3** - Cloud storage
- **Google Cloud Storage**

---

## Data Flow

```json
{
  "Input": "YouTube URL",
  "Processing": [
    "Extract metadata",
    "Get transcript",
    "AI rewrite",
    "Generate voice",
    "Create video",
    "Prepare metadata"
  ],
  "Output": "YouTube video (draft/published)"
}
```

---

## Error Handling

1. **Retry Logic**
   - Exponential backoff (1s, 2s, 4s, 8s, 16s)
   - Max 5 retries per operation

2. **Fallback Mechanisms**
   - Use alternative TTS if primary fails
   - Use cached transcript if API unavailable
   - Skip video generation if RunwayML fails

3. **Notifications**
   - Slack alerts on critical errors
   - Email summary of failed workflows
   - Dashboard visualization

---

## Performance Optimization

1. **Parallel Processing**
   - Extract metadata & transcript simultaneously
   - Generate multiple voiceover versions
   - Process video while awaiting audio

2. **Caching**
   - Cache video metadata (24 hours)
   - Cache transcript (permanent)
   - Cache AI results (permanent)

3. **Rate Limiting**
   - OpenAI: 3 requests/minute
   - YouTube: 10,000 quota units/day
   - ElevenLabs: Based on plan

---

## Security

1. **API Key Management**
   - n8n Credentials (encrypted)
   - Environment variables
   - Key rotation policies

2. **Data Privacy**
   - Encrypt in transit (HTTPS)
   - Encrypt at rest
   - GDPR compliance

3. **Access Control**
   - OAuth2 for YouTube
   - API key authentication
   - Role-based access in n8n
