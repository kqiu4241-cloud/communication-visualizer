<template>
  <div class="visualizer">
    <div class="nodes">
      <div class="node source">🔵 {{ source }}</div>
      <div class="path">
        <div class="signal" :class="{ animate: isAnimating }"></div>
      </div>
      <div class="node destination">🟢 {{ destination }}</div>
    </div>

    <div class="controls">
      <input v-model="source" placeholder="源节点 (如 A)" />
      <input v-model="destination" placeholder="目标节点 (如 B)" />
      <button @click="startSimulation" :disabled="isAnimating">开始传输 🚀</button>
    </div>

    <div v-if="result" class="result">
      <h3>📊 通信结果</h3>
      <p>从 {{ result.source }} → {{ result.destination }}</p>
      <p>时延：{{ result.delay_ms }} ms</p>
      <p>带宽：{{ result.bandwidth_mbps }} Mbps</p>
      <p>信噪比：{{ result.snr_db }} dB</p>
      <p>丢包率：{{ result.packet_loss }} %</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const source = ref('A')
const destination = ref('B')
const result = ref(null)
const isAnimating = ref(false)

async function startSimulation() {
  result.value = null
  isAnimating.value = true

  const res = await fetch('http://127.0.0.1:5000/api/simulate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ source: source.value, destination: destination.value })
  })
  result.value = await res.json()

  // 动画结束
  setTimeout(() => (isAnimating.value = false), 1500)
}
</script>

<style scoped>
.visualizer {
  margin-top: 40px;
  text-align: center;
}

.nodes {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 30px;
}

.node {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #223;
  font-size: 20px;
  border: 3px solid #00bcd4;
  box-shadow: 0 0 15px #00bcd4;
}

.path {
  width: 200px;
  height: 4px;
  background: #00bcd4;
  position: relative;
  margin: 0 20px;
  border-radius: 2px;
}

.signal {
  position: absolute;
  left: 0;
  top: -8px;
  width: 20px;
  height: 20px;
  background: #ffeb3b;
  border-radius: 50%;
  transform: translateX(0);
}

.signal.animate {
  animation: move 1.5s linear;
}

@keyframes move {
  0% { transform: translateX(0); }
  100% { transform: translateX(200px); }
}

.controls input {
  padding: 6px;
  margin: 5px;
  border-radius: 5px;
  border: none;
  outline: none;
}

.controls button {
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  background: #00bcd4;
  color: white;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}

.controls button:hover {
  background: #00acc1;
}

.result {
  background: #16213e;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 0 10px #00bcd4;
  display: inline-block;
}
</style>
