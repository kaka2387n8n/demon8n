# 📖 Setup Guide

## Prerequisites

- ✅ n8n instance (self-hosted or cloud)
- ✅ YouTube account with creator access
- ✅ OpenAI account with API access
- ✅ ElevenLabs account
- ✅ Python 3.8+ (for scripts)

---

## Step 1: YouTube API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project: "YouTube Automation"
3. Enable YouTube Data API v3
4. Create OAuth 2.0 credentials (Desktop app)
5. Download JSON credentials file
6. Get your YouTube Channel ID
7. Create API Key

---

## Step 2: OpenAI API Setup

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Go to "API keys" → "Create new secret key"
4. Copy and save securely
5. Set up billing

---

## Step 3: ElevenLabs Setup

1. Go to [ElevenLabs](https://elevenlabs.io/)
2. Sign up or log in
3. Go to "Profile" → "API Key"
4. Copy your API key
5. Choose a voice and note Voice ID

---

## Step 4: Configure Environment

```bash
# Clone repo
git clone https://github.com/kaka2387n8n/demon8n.git
cd demon8n

# Copy environment template
cp .env.example .env

# Edit with your keys
nano .env
```

**Fill in .env:**
```bash
YOUTUBE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
YOUTUBE_CHANNEL_ID=UCxxxxxxxxxxxxxx
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
ELEVENLABS_API_KEY=xxxxxxxxxxxxxxxxxxxx
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
```

---

## Step 5: n8n Setup

### Install n8n
```bash
# Using npm
npm install -g n8n

# Start n8n
n8n start

# Access at http://localhost:5678
```

### Import Workflow
1. Open n8n dashboard
2. Click "Workflows" → "Import"
3. Select `workflows/youtube-automation-main.json`
4. Click "Import"

### Configure Credentials
1. Go to Credentials → "+ New"
2. Add credentials for:
   - **YouTube** (OAuth2)
   - **OpenAI** (Header Auth)
   - **ElevenLabs** (Header Auth)

---

## Step 6: Testing

### Test Components
```bash
# Test YouTube API
curl "https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true&key=YOUR_API_KEY"

# Test OpenAI API
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer sk-xxxx" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"Hi"}]}'

# Test ElevenLabs
curl "https://api.elevenlabs.io/v1/voices" \
  -H "xi-api-key: xxxx"
```

### Test Workflow
1. Open workflow in n8n
2. Click "Execute Workflow"
3. Monitor execution
4. Check output of each node

---

## Step 7: Deploy

### Production Setup
```bash
# Install PM2
npm install -g pm2

# Start n8n with PM2
pm2 start "n8n start" --name n8n

# Save PM2 config
pm2 save
```

### Setup Reverse Proxy (Nginx)
```nginx
server {
    listen 443 ssl http2;
    server_name automation.example.com;

    location / {
        proxy_pass http://localhost:5678;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

---

## Troubleshooting

### YouTube API Key Invalid
✅ Verify API key in Google Cloud Console
✅ Check API is enabled
✅ Verify key has correct permissions

### OpenAI Rate Limit
✅ Use gpt-3.5-turbo (faster, cheaper)
✅ Implement queue for batch processing
✅ Reduce max_tokens

### n8n Webhook Not Working
✅ Check webhook URL is public
✅ Verify firewall rules
✅ Check n8n is running
✅ Review n8n logs

---

## Next Steps

1. ✅ Import workflow
2. ✅ Add credentials
3. ✅ Test with sample video
4. ✅ Deploy to production
5. ✅ Monitor and optimize

---

**Setup Complete! 🎉**