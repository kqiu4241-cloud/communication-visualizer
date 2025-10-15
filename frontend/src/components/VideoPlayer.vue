<template>
  <div class="video-page">
    <h1>🎬 流媒体通信演示</h1>
    <video controls autoplay width="720">
      <source src="http://127.0.0.1:5000/api/video" type="video/mp4" />
      您的浏览器不支持视频播放。
    </video>

    <div class="back">
      <button @click="goBack">🔙 返回信号可视化</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
function goBack() {
  router.push('/')
}
</script>

<style scoped>
.video-page {
  text-align: center;
  color: white;
  background: linear-gradient(180deg, #0e153a, #1b2845);
  min-height: 100vh;
  padding-top: 40px;
}

video {
  border: 4px solid #00bcd4;
  border-radius: 12px;
  box-shadow: 0 0 15px #00bcd4;
}

.back button {
  margin-top: 20px;
  padding: 10px 18px;
  border: none;
  border-radius: 6px;
  background: #00bcd4;
  color: white;
  font-weight: bold;
  cursor: pointer;
}

.back button:hover {
  background: #0097a7;
}
</style>
