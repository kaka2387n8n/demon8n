# 🎬 YouTube Automation Pipeline - Phiên bản AI Miễn Phí Tốt Nhất

**Quy trình hoàn chỉnh sử dụng AI miễn phí hàng đầu hiện nay**

---

## 🔥 Tổng Quan AI Services Miễn Phí

| Bước | Tác vụ | AI Dùng | Miễn phí | Chất lượng | Ghi chú |
|------|--------|--------|---------|-----------|----------|
| 1 | Cào YouTube | YouTube API | ✅ 10k/ngày | ⭐⭐⭐⭐⭐ | Chính thức từ Google |
| 2 | Rewrite Content | **Claude 3.5 Sonnet** | ✅ 100k token/tháng | ⭐⭐⭐⭐⭐ | Tốt nhất hiện nay (Free tier) |
| 3 | Alternative Rewrite | **Llama 2 (Replicate)** | ✅ Miễn phí | ⭐⭐⭐⭐ | Meta open-source |
| 4 | Voice Generation | **Play.ht** | ✅ 10k char/tháng | ⭐⭐⭐⭐⭐ | Giọng tự nhiên (Free tier) |
| 5 | Alternative Voice | **Bark (Replicate)** | ✅ Miễn phí | ⭐⭐⭐⭐ | AI voice open-source |
| 6 | Video Generation | **Pika 1.0** | ✅ 50 credits/tháng | ⭐⭐⭐⭐ | AI video tốt nhất |
| 7 | Alternative Video | **Runway Gen-3** | ✅ 25 credits/tháng | ⭐⭐⭐⭐⭐ | Nâng cấp mới |
| 8 | Thumbnail AI | **Canva AI** | ✅ Miễn phí | ⭐⭐⭐⭐ | Template & AI design |
| 9 | Alternative Thumbnail | **Leonardo AI** | ✅ 150 tokens/ngày | ⭐⭐⭐⭐ | Image generation |
| 10 | Subtitle Auto | **Whisper (OpenAI)** | ✅ API miễn phí | ⭐⭐⭐⭐⭐ | Accuracy 99% |

---

## 📊 Chi tiết từng Node & Dùng AI nào

### **Node 1: Webhook Trigger** ✅
```
📥 Input: YouTube URL
💾 Output: Video URL
🤖 AI: Không cần
⚙️ Chức năng: Nhận webhook request
```

---

### **Node 2: Fetch YouTube Video** ✅
```
📥 Input: Video ID
💾 Output: Video metadata (title, description, duration, thumbnail)
🤖 AI: YouTube API (miễn phí, 10k quota/ngày)
⚙️ Chức năng: Lấy info video từ YouTube

🔗 API: https://www.googleapis.com/youtube/v3/videos
🆓 Miễn phí: ✅ YES (10,000 quota units/day)
📊 Tốc độ: Nhanh (< 1 giây)
```

---

### **Node 3: Extract Transcript** ✅
```
📥 Input: Video ID
💾 Output: Full transcript text
🤖 AI: OpenAI Whisper API (miễn phí hoặc rất rẻ)
⚙️ Chức năng: Lấy subtitle/transcript video

🔗 2 Cách:

**Cách 1: YouTube Built-in (Recommended)**
- Lấy từ caption YouTube (miễn phí)
- API: youtube.captions
- Chất lượng: ⭐⭐⭐⭐ (nếu video có caption)

**Cách 2: Whisper API (Fallback)**
- Download audio video
- Gửi tới Whisper API
- 🆓 Miễn phí: ✅ $0.02/phút audio (rất rẻ)
- 📊 Chất lượng: ⭐⭐⭐⭐⭐ (99% accuracy)

💡 Recommendation: 
   → Dùng YouTube caption trước (free)
   → Nếu không có → Dùng Whisper (rất rẻ)
```

---

### **Node 4: Rewrite Content with AI** 🌟 **QUAN TRỌNG**
```
📥 Input: Original transcript
💾 Output: Rewritten content (script, blog, social media)

🤖 AI RECOMMENDATIONS:

**1️⃣ Claude 3.5 Sonnet (BEST - FREE)**
   ✅ 100,000 tokens/tháng MIỄN PHÍ
   ✅ Chất lượng: ⭐⭐⭐⭐⭐ (BEST AI hiện nay)
   ✅ Multilingual support
   ✅ Creative writing tuyệt vời
   📊 Token: ~400 tokens/1000 words
   
   → Setup: 
      1. Vào https://console.anthropic.com/
      2. Tạo free account
      3. Lấy API key
      4. Cài thêm: npm install @anthropic-ai/sdk
   
   → Cost: ✅ MIỄN PHÍ (100k tokens/tháng)

**2️⃣ Llama 2 via Replicate (FREE Alternative)**
   ✅ Hoàn toàn MIỄN PHÍ
   ✅ Chất lượng: ⭐⭐⭐⭐ (tốt, nhưng không bằng Claude)
   ✅ Meta open-source model
   
   → Setup:
      1. Vào https://replicate.com/
      2. Sign up miễn phí
      3. Lấy API key
      4. Dùng model: replicate/llama-2-7b-chat
   
   → Cost: ✅ MIỄN PHÍ hoàn toàn

**3️⃣ Mistral 7B (Fallback)**
   ✅ MIỄN PHÍ qua Replicate
   ✅ Chất lượng: ⭐⭐⭐⭐
   
   → Setup: Tương tự Llama 2
   → Model: replicate/mistral-7b
   → Cost: ✅ MIỄN PHÍ

🎯 **STRATEGY LỌC (dùng lần lượt):**
   1. Thử Claude 3.5 Sonnet (100k free/tháng - đủ)
   2. Nếu hết → Dùng Llama 2 (free unlimited)
   3. Nếu cần quality → Dùng Mistral 7B (free unlimited)

💰 **Total Cost: ✅ 0 đồng**
```

---

### **Node 5: Process & Clean Content** ✅
```
📥 Input: Rewritten content
💾 Output: Clean, formatted content
🤖 AI: Không cần (code processing)
⚙️ Chức năng: 
   - Split thành chunks
   - Remove filler words
   - Format markdown
   - Extract keywords
   - Add SEO tags

💡 Dùng n8n built-in nodes hoặc JavaScript code
```

---

### **Node 6: Generate Voiceover** 🌟 **QUAN TRỌNG**
```
📥 Input: Rewritten content/script
💾 Output: MP3/WAV audio file

🤖 AI RECOMMENDATIONS:

**1️⃣ Play.ht (BEST - FREE)**
   ✅ 10,000 characters/tháng MIỄN PHÍ
   ✅ Chất lượng: ⭐⭐⭐⭐⭐ (rất tự nhiên)
   ✅ 100+ giọng nói (tiếng Việt, Anh, v.v.)
   ✅ Tùy chỉnh tốc độ, tone, pitch
   ✅ MP3 format
   
   → Setup:
      1. Vào https://play.ht/
      2. Sign up miễn phí
      3. Lấy API key
      4. Chọn voice ID
   
   → Cost: ✅ 10,000 chars/tháng (free)
   → Tính: ~1 video/tháng (nếu script 10k chars)

**2️⃣ Bark via Replicate (FREE)**
   ✅ Hoàn toàn MIỄN PHÍ
   ✅ Chất lượng: ⭐⭐⭐⭐ (tốt, thiên nhiên)
   ✅ Multi-language
   ✅ Voice cloning (limited)
   
   → Setup:
      1. Vào https://replicate.com/
      2. Model: suno-ai/bark
      3. Điền text → nhận audio
   
   → Cost: ✅ MIỄN PHÍ hoàn toàn

**3️⃣ Coqui TTS (Open-source - Offline)**
   ✅ MIỄN PHÍ, chạy local
   ✅ Chất lượng: ⭐⭐⭐ (tạm được)
   ✅ Không cần API key
   ✅ Có thể offline
   
   → Setup:
      pip install TTS
      from TTS.api import TTS
      tts = TTS("tts_models/en/ljspeech/glow-tts")
   
   → Cost: ✅ MIỄN PHÍ hoàn toàn

🎯 **STRATEGY LỌC (dùng lần lượt):**
   1. Play.ht (10k chars/tháng - tự nhiên nhất)
   2. Nếu hết quota → Bark via Replicate (free unlimited)
   3. Nếu cần quality → Coqui TTS (free, local)

💰 **Total Cost: ✅ 0 đồng** (nếu dùng combo)
```

---

### **Node 7: Generate Video** 🌟 **QUAN TRỌNG**
```
📥 Input: Audio + Images/Text
💾 Output: MP4 video file

🤖 AI RECOMMENDATIONS:

**Option A: Avatar Video (AI Presenter)**

**1️⃣ Pika 1.0 (BEST - FREE)**
   ✅ 50 monthly credits (free tier)
   ✅ Chất lượng: ⭐⭐⭐⭐⭐ (siêu đẹp)
   ✅ Generate video từ script
   ✅ Avatar presenters
   ✅ Background music built-in
   
   → Setup:
      1. Vào https://www.pika.art/
      2. Sign up (free)
      3. Tạo API (beta)
      4. Lấy API key
   
   → Cost: ✅ 50 credits/tháng (free)
   → 1 video = ~5-10 credits

**2️⃣ Runway Gen-3 (Nâng cấp, FREE)**
   ✅ 25 monthly credits (free tier)
   ✅ Chất lượng: ⭐⭐⭐⭐⭐ (tốt hơn Pika)
   ✅ Text-to-video, image-to-video
   ✅ Motion control
   
   → Setup:
      1. Vào https://app.runwayml.com/
      2. Sign up (free)
      3. Lấy API key
   
   → Cost: ✅ 25 credits/tháng (free)

**Option B: DIY Video (Dùng stock footage)**

**3️⃣ FFmpeg (Local) + Free Stock Footage**
   ✅ MIỄN PHÍ, chạy local
   ✅ Combine audio + images/video clips
   ✅ Add transitions, effects
   
   → Setup:
      1. Download FFmpeg
      2. Lấy images từ Unsplash/Pexels (free)
      3. Combine với audio
   
   → Cost: ✅ MIỄN PHÍ hoàn toàn
   → Chất lượng: ⭐⭐⭐ (basic, nhưng OK)

**Option C: Stock Footage (Free sites)**

**4️⃣ Mixkit + Pexels Videos (FREE)**
   ✅ Hàng ngàn video clips free
   ✅ Royalty-free, HD quality
   ✅ Download trực tiếp
   
   → Sites:
      - Mixkit: https://mixkit.co/
      - Pexels: https://www.pexels.com/videos/
      - Pixabay: https://pixabay.com/videos/
   
   → Cost: ✅ MIỄN PHÍ

🎯 **STRATEGY LỌC (recommended):**
   
   **Cách 1: AI Avatar (Cách tốt nhất)**
   1. Dùng Pika 1.0 (50 free credits/tháng)
   2. Nếu hết → Runway Gen-3 (25 free credits/tháng)
   3. Combine audio voiceover + AI video = siêu chuyên nghiệp
   
   **Cách 2: DIY + Stock (Nhanh & rẻ)**
   1. Collect images từ Unsplash/Pexels
   2. Lấy video clips từ Mixkit/Pexels
   3. FFmpeg combine audio + media
   4. Add transitions
   
   **Cách 3: Hybrid (Balanced)**
   1. Dùng Pika AI cho opening (attention-grabbing)
   2. Dùng stock footage cho content part
   3. FFmpeg combine tất cả

💰 **Total Cost: ✅ 0 đồng** (combo free services)
```

---

### **Node 8: Generate Thumbnail** ✅
```
📥 Input: Video title + keywords
💾 Output: PNG thumbnail image

🤖 AI RECOMMENDATIONS:

**1️⃣ Canva AI (BEST - FREE)**
   ✅ Magic Edit (AI powered)
   ✅ 1000+ templates
   ✅ Canva Pro free trial 30 days
   ✅ YouTube thumbnail size templates
   
   → Setup:
      1. Vào https://www.canva.com/
      2. Sign up (free)
      3. Chọn template "YouTube Thumbnail"
      4. Dùng Canva AI Magic Edit
   
   → Cost: ✅ MIỄN PHÍ (free tier đủ)

**2️⃣ Leonardo AI (FREE)**
   ✅ 150 tokens/ngày (free tier)
   ✅ Image generation AI
   ✅ Custom style
   ✅ Nhanh & chất lượng tốt
   
   → Setup:
      1. Vào https://leonardo.ai/
      2. Sign up (free)
      3. Prompt: "YouTube thumbnail with [title]..."
      4. Generate
   
   → Cost: ✅ 150 tokens/ngày (free)
   → Tính: ~3-5 thumbnails/ngày

**3️⃣ Stable Diffusion via Replicate (FREE)**
   ✅ MIỄN PHÍ hoàn toàn
   ✅ Image generation
   ✅ Multiple styles
   
   → Setup:
      1. Vào https://replicate.com/
      2. Model: stability-ai/stable-diffusion
      3. Điền prompt → generate
   
   → Cost: ✅ MIỄN PHÍ

🎯 **STRATEGY LỌC (recommended):**
   1. Canva AI (most user-friendly)
   2. Nếu cần variety → Leonardo AI (150 free/ngày)
   3. Nếu cần batch → Stable Diffusion (unlimited free)

💰 **Total Cost: ✅ 0 đồng**
```

---

### **Node 9: Generate Subtitles** ✅
```
📥 Input: Video file (MP4) hoặc Audio file
💾 Output: SRT/VTT subtitle file

🤖 AI RECOMMENDATIONS:

**1️⃣ OpenAI Whisper (BEST)**
   ✅ 99% accuracy
   ✅ Multi-language
   ✅ Giá rẻ: $0.02/phút audio
   ✅ Open-source model (có offline)
   
   → Setup:
      pip install openai
      audio_file = open("audio.mp3", "rb")
      transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
      )
   
   → Cost: ✅ $0.02/phút (VẤY RẺ)

**2️⃣ Whisper Local (Offline - FREE)**
   ✅ Chạy local, không cần API key
   ✅ 99% accuracy
   ✅ MIỄN PHÍ hoàn toàn
   
   → Setup:
      pip install openai-whisper
      whisper "audio.mp3" --language Vietnamese
   
   → Cost: ✅ MIỄN PHÍ (offline)

**3️⃣ Replicate Whisper (FREE)**
   ✅ MIỄN PHÍ
   ✅ Cloud-based
   ✅ Chất lượng: ⭐⭐⭐⭐⭐
   
   → Setup:
      1. Vào https://replicate.com/
      2. Model: openai/whisper
      3. Upload audio → generate
   
   → Cost: ✅ MIỄN PHÍ

🎯 **STRATEGY LỌC:**
   1. Whisper Local (free, offline)
   2. Nếu cần speed → Replicate Whisper (free)
   3. Nếu không muốn cài local → OpenAI API ($0.02/min)

💰 **Total Cost: ✅ 0 đồng** (dùng local hoặc Replicate)
```

---

### **Node 10: Upload to YouTube** ✅
```
📥 Input: Video file + metadata
💾 Output: YouTube video URL
🤖 AI: Không cần
⚙️ Chức năng: Upload video lên YouTube

🔗 API: YouTube Data API v3 (miễn phí)
🆓 Miễn phí: ✅ YES (10,000 quota units/day)
📊 Chất lượng: ⭐⭐⭐⭐⭐ (chính thức)

→ Setup:
   1. Google Cloud Console
   2. Enable YouTube Data API v3
   3. Create OAuth 2.0 credentials
   4. Get refresh token

→ Cost: ✅ MIỄN PHÍ
```

---

## 💰 TỔNG COST ANALYSIS

### **Scenario 1: Hoàn toàn Miễn Phí (Free Tier)**
```
┌─────────────────────────────────────────────┐
│ NODE                    │ AI              │ Cost |
├─────────────────────────────────────────────┤
│ 1. Webhook              │ n8n             │ FREE │
│ 2. Fetch YouTube        │ YouTube API     │ FREE │
│ 3. Extract Transcript   │ YouTube caption │ FREE │
│ 4. Rewrite Content      │ Claude (100k)   │ FREE │
│ 5. Process Content      │ n8n code        │ FREE │
│ 6. Voiceover           │ Bark (Replicate)│ FREE │
│ 7. Generate Video      │ Pika (50 free)  │ FREE │
│ 8. Thumbnail           │ Canva AI        │ FREE │
│ 9. Subtitles           │ Whisper Local   │ FREE │
│ 10. Upload YouTube     │ YouTube API     │ FREE │
├─────────────────────────────────────────────┤
│ TOTAL/MONTH             │                 │ $0   │
└─────────────────────────────────────────────┘
```

### **Scenario 2: Tối ưu Quality + Free**
```
┌─────────────────────────────────────────────┐
│ NODE                    │ AI              │ Cost |
├─────────────────────────────────────────────┤
│ 1. Webhook              │ n8n             │ FREE │
│ 2. Fetch YouTube        │ YouTube API     │ FREE │
│ 3. Extract Transcript   │ Whisper API     │ $0.02│
│ 4. Rewrite Content      │ Claude (100k)   │ FREE │
│ 5. Process Content      │ n8n code        │ FREE │
│ 6. Voiceover           │ Play.ht (10k)   │ FREE │
│ 7. Generate Video      │ Runway (25 cr)  │ FREE │
│ 8. Thumbnail           │ Leonardo AI     │ FREE │
│ 9. Subtitles           │ Replicate       │ FREE │
│ 10. Upload YouTube     │ YouTube API     │ FREE │
├─────────────────────────────────────────────┤
│ TOTAL/MONTH             │                 │ <$1  │
└─────────────────────────────────────────────┘
```

### **Scenario 3: Premium pero Affordable**
```
┌─────────────────────────────────────────────┐
│ NODE                    │ AI              │ Cost |
├─────────────────────────────────────────────┤
│ 1. Webhook              │ n8n             │ FREE │
│ 2. Fetch YouTube        │ YouTube API     │ FREE │
│ 3. Extract Transcript   │ Whisper API     │ $0.02│
│ 4. Rewrite Content      │ Claude Pro      │ $20  │
│ 5. Process Content      │ n8n code        │ FREE │
│ 6. Voiceover           │ Play.ht Pro     │ $10  │
│ 7. Generate Video      │ Runway Pro      │ $12  │
│ 8. Thumbnail           │ Canva Pro       │ $15  │
│ 9. Subtitles           │ Whisper API     │ $0.02│
│ 10. Upload YouTube     │ YouTube API     │ FREE │
├─────────────────────────────────────────────┤
│ TOTAL/MONTH             │                 │ $57  │
└─────────────────────────────────────────────┘
```

---

## 🎯 RECOMMENDED SETUP (Hoàn toàn Miễn Phí)

### ✅ **Best Free Combination:**

```
1. ✅ Claude 3.5 Sonnet (Free - 100k token/tháng)
   → Rewrite content - CHẤT LƯỢNG TUYỆT VỜI
   
2. ✅ Play.ht Free (10k char/tháng)
   → Voice generation - GIỌNG TƯỚNG TỰ NHIÊN
   → Nếu hết → Bark via Replicate (free unlimited)
   
3. ✅ Pika 1.0 (50 free credits/tháng)
   → AI Video generation - ĐẼP & CHUYÊN NGHIỆP
   → Nếu hết → Runway Gen-3 (25 credits) + FFmpeg
   
4. ✅ Canva AI (Free tier)
   → Thumbnail generation - NHANH & ĐẸP
   → Alternative: Leonardo AI (150 free/ngày)
   
5. ✅ Whisper Local (Offline - 100% free)
   → Subtitle generation - ACCURACY 99%
   
6. ✅ YouTube API (10k quota/ngày)
   → Upload video - CHÍNH THỨC

**💰 TOTAL: $0/tháng**
**⭐ QUALITY: 9/10**
```

---

## 🚀 NEXT STEPS

Bạn muốn tôi:
1. ✅ Tạo workflow JSON với setup này?
2. ✅ Hướng dẫn setup từng API key?
3. ✅ Tạo Python scripts để automation?
4. ✅ Setup n8n nodes cụ thể?

**Lựa chọn nào?** 🎯
