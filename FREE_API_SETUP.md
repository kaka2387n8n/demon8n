# 🆓 Setup Free AI APIs

## 1️⃣ Claude 3.5 Sonnet (FREE - 100k token/tháng)

### Tạo Account
1. Vào https://console.anthropic.com/
2. Click "Sign up"
3. Verify email
4. Dashboard → "API Keys"
5. Click "Create Key"
6. Copy key

### Thêm vào .env
```bash
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

### Test
```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

---

## 2️⃣ Play.ht (FREE - 10k chars/tháng)

### Tạo Account
1. Vào https://play.ht/
2. Click "Sign up"
3. Verify email
4. Dashboard → "API"
5. Copy API Key
6. Chọn voice → Copy Voice ID

### Thêm vào .env
```bash
PLAYHT_API_KEY=your_api_key
PLAYHT_VOICE_ID=s3://voice-cloning-prod/XXXX
```

### Popular Free Voices
- `s3://voice-cloning-prod/voices/english/us/default` (neutral)
- Xem đầy đủ: https://play.ht/voices/

### Test
```bash
curl https://api.play.ht/api/v1/convert \
  -H "AUTHORIZATION: Bearer $PLAYHT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "voice_id": "s3://voice-cloning-prod/..."
  }'
```

---

## 3️⃣ Pika 1.0 (FREE - 50 credits/tháng)

### Tạo Account
1. Vào https://www.pika.art/
2. Sign up with Discord/Google
3. Dashboard → Settings → API (beta)
4. Generate API Key
5. Copy key

### Thêm vào .env
```bash
PIKA_API_KEY=your_pika_key
PIKA_API_URL=https://api.pika.art/v1
```

### Note
- 50 credits/tháng (free tier)
- 1 video ~5-10 credits
- Upgrade: $25/tháng cho 200 credits

---

## 4️⃣ Leonardo AI (FREE - 150 tokens/ngày)

### Tạo Account
1. Vào https://leonardo.ai/
2. Sign up
3. Verify email
4. Dashboard → API Keys
5. Copy API key

### Thêm vào .env
```bash
LEONARDO_API_KEY=your_leonardo_key
```

### Test
```bash
curl https://api.leonardo.ai/v1/generations \
  -H "Authorization: Bearer $LEONARDO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "YouTube thumbnail, bright colors",
    "num_images": 1
  }'
```

---

## 5️⃣ Replicate (FREE - Unlimited)

### Tạo Account
1. Vào https://replicate.com/
2. Sign up
3. Copy API token

### Thêm vào .env
```bash
REPLICATE_API_KEY=your_replicate_key
```

### Popular Free Models
- `Llama 2` - Content rewriting
- `Bark` - Text-to-speech
- `Stable Diffusion` - Image generation
- `Whisper` - Transcription

### Test
```bash
curl https://api.replicate.com/v1/predictions \
  -H "Authorization: Token $REPLICATE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "version": "...",
    "input": {"prompt": "..."}
  }'
```

---

## 6️⃣ YouTube API (FREE - 10k quota/ngày)

### Setup
1. Vào https://console.cloud.google.com/
2. Create Project: "YouTube Automation"
3. Enable "YouTube Data API v3"
4. Create OAuth 2.0 credentials (Desktop)
5. Download JSON
6. Get API Key

### Thêm vào .env
```bash
YOUTUBE_API_KEY=your_api_key
YOUTUBE_CHANNEL_ID=your_channel_id
YOUTUBE_CLIENT_ID=your_client_id.apps.googleusercontent.com
YOUTUBE_CLIENT_SECRET=your_secret
YOUTUBE_REFRESH_TOKEN=your_refresh_token
```

### Get Refresh Token
```bash
# 1. Run auth flow
python get_youtube_token.py

# 2. Browser opens → Authorize
# 3. Copy token → .env
```

---

## 7️⃣ Whisper API (VERY CHEAP - $0.02/min)

### Option 1: Local (FREE, Offline)
```bash
pip install openai-whisper
whisper "audio.mp3" --language Vietnamese
```

### Option 2: OpenAI API (Cheap)
```bash
OPENAI_API_KEY=sk-your_key
# $0.02/minute audio
```

### Option 3: Replicate (FREE)
```bash
# Model: openai/whisper
# Free via Replicate API
```

---

## 📝 Complete .env Template

```bash
# YouTube
YOUTUBE_API_KEY=your_youtube_api_key
YOUTUBE_CHANNEL_ID=UCxxxxxxxxxxxxx
YOUTUBE_CLIENT_ID=xxxxx.apps.googleusercontent.com
YOUTUBE_CLIENT_SECRET=xxxxx
YOUTUBE_REFRESH_TOKEN=xxxxx

# Claude AI (FREE)
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# Play.ht (FREE)
PLAYHT_API_KEY=xxxxx
PLAYHT_VOICE_ID=s3://voice-cloning-prod/xxxxx

# Pika AI (FREE)
PIKA_API_KEY=xxxxx

# Leonardo AI (FREE)
LEONARDO_API_KEY=xxxxx

# Replicate (FREE)
REPLICATE_API_KEY=xxxxx

# OpenAI (for Whisper - optional)
OPENAI_API_KEY=sk-xxxxx
```

---

## ✅ Checklist

- [ ] Claude API key
- [ ] Play.ht API key + Voice ID
- [ ] Pika API key
- [ ] Leonardo API key
- [ ] Replicate API key
- [ ] YouTube API key
- [ ] YouTube OAuth token
- [ ] .env file created
- [ ] All keys tested

---

**All free! No credit card needed (mostly)** 🎉
