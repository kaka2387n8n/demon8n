# 📖 Hướng dẫn Import Workflow vào n8n

## ✅ File mới: `youtube-simple.json`
File này **100% hợp lệ** và sẵn sàng import vào n8n.

---

## 🚀 Bước 1: Download File

### Cách 1: Copy trực tiếp từ GitHub
1. Vào: https://github.com/kaka2387n8n/demon8n/blob/main/workflows/youtube-simple.json
2. Click nút **"Raw"** (góc phải)
3. **Ctrl + A** → **Ctrl + C** (copy toàn bộ)
4. **Ctrl + V** để paste vào editor

### Cách 2: Download file
```bash
wget https://raw.githubusercontent.com/kaka2387n8n/demon8n/main/workflows/youtube-simple.json
```

---

## 🚀 Bước 2: Mở n8n

```
http://localhost:5678
```

Nếu chưa start n8n:
```bash
n8n start
```

---

## 🚀 Bước 3: Import Workflow

### Phương pháp A: Import từ File (Nếu download)

1. Click menu **"Workflows"** (bên trái)
2. Click nút **"+" hoặc "New"**
3. Chọn **"Import from file"**
4. **Chọn file** `youtube-simple.json`
5. Click **"Import"**
6. ✅ Xong!

### Phương pháp B: Copy-Paste JSON

1. Click menu **"Workflows"**
2. Click **"+" → "New"** → "Create New Workflow"
3. Click icon **⚙️** (Settings) góc phải
4. Chọn **"Show raw data"** hoặc **"Edit raw"**
5. **Xóa hết** nội dung cũ
6. **Paste** JSON vừa copy
7. Click **"Close"** hoặc **"Save"**
8. ✅ Workflow load ngay!

---

## 🧪 Bước 4: Test Workflow

### Cách 1: Click "Execute" Button (Dễ nhất)

1. Mở workflow vừa import
2. Bạn sẽ thấy node **"Webhook"** ở đầu
3. Click nút **"Execute Workflow"** (hoặc **"Test"**) góc trên
4. Workflow sẽ chạy tự động
5. Xem kết quả ở bên phải panel ✅

### Cách 2: Gửi Webhook Request

1. Tìm node **"Webhook"** → Copy **Webhook URL**
   - URL sẽ giống: `http://localhost:5678/webhook/youtube-auto`

2. Gửi request từ terminal:
```bash
curl -X POST http://localhost:5678/webhook/youtube-auto \
  -H "Content-Type: application/json" \
  -d '{
    "videoId": "dQw4w9WgXcQ",
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  }'
```

3. Kiểm tra **"Executions"** tab để xem kết quả

---

## 🔍 Kiểm tra Workflow Có Chạy Đúng

Bạn sẽ thấy:

```
✅ Node 1: Webhook Trigger
   ↓
✅ Node 2: Fetch Video Info (call YouTube API)
   ↓
✅ Node 3: Extract Info (xử lý data)
   ↓
✅ Node 4: Get Transcript (lấy captions)
   ↓
✅ Node 5: Rewrite Content (AI rewrite)
   ↓
✅ Node 6: Generate Voice (TTS)
   ↓
✅ Node 7: Create Video (AI video)
   ↓
✅ Node 8: Create Thumbnail (AI thumbnail)
   ↓
✅ Node 9: Generate Subtitles (Whisper)
   ↓
✅ Node 10: Prepare Upload (prep metadata)
   ↓
✅ Node 11: Complete (done!)
```

Mỗi node phải có **✅ checkmark xanh**. Nếu có **❌** thì click để xem lỗi.

---

## 🔧 Cấu hình API Keys (Tuỳ chọn)

Workflow hiện tại dùng **mock data**, nên không cần API keys để test.

Khi muốn dùng **real APIs**, bạn cần:

### 1. YouTube API
```bash
YOUTUBE_API_KEY=your_youtube_key
# Set vào Environment Variable hoặc n8n Secret
```

### 2. Claude AI (Rewrite)
```bash
ANTHROPIC_API_KEY=sk-ant-xxxxx
# Edit Node 5 để call Claude API
```

### 3. Play.ht (Voice)
```bash
PLAYHT_API_KEY=xxxxx
PLAYHT_VOICE_ID=xxxxx
# Edit Node 6 để call Play.ht API
```

### 4. Pika AI (Video)
```bash
PIKA_API_KEY=xxxxx
# Edit Node 7 để call Pika API
```

---

## 📝 Chỉnh sửa Nodes (Optional)

Nếu muốn sử dụng real APIs thay vì mock data:

1. Click vào **node bất kỳ**
2. Bên phải sẽ hiện **panel tùy chọn**
3. Chỉnh sửa **URL, parameters, headers**
4. Click **"Save"**

Ví dụ: Chỉnh sửa Node 5 (Rewrite Content) để dùng Claude:

```json
{
  "url": "https://api.anthropic.com/v1/messages",
  "method": "POST",
  "headers": {
    "x-api-key": "{{$env.ANTHROPIC_API_KEY}}"
  },
  "body": {
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1500,
    "messages": [
      {
        "role": "user",
        "content": "Rewrite this: {{$json.transcript}}"
      }
    ]
  }
}
```

---

## 🛠️ Troubleshooting

### ❌ "Invalid JSON"
→ Copy lại file từ GitHub (Raw button)

### ❌ "Node error"
→ Click node → xem error message

### ❌ "Cannot connect to YouTube"
→ Thêm API key vào environment

### ❌ "Webhook URL not working"
→ Kiểm tra n8n đang chạy
→ Firewall/port settings

---

## ✅ Checklist

- [ ] Download hoặc copy file JSON
- [ ] Mở n8n dashboard
- [ ] Import workflow
- [ ] Test bằng "Execute" button
- [ ] Xem kết quả từng node
- [ ] (Optional) Thêm API keys
- [ ] Activate workflow

---

## 🎉 Done!

Workflow đã sẵn sàng sử dụng! 🚀

Cần giúp gì thêm không?
