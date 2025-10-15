<template>
  <div class="app-container">
    <h1>📡 实时通信信号传输可视化模拟器</h1>
    <SignalVisualizer />
  </div>
</template>

<script setup>
import SignalVisualizer from './components/SignalVisualizer.vue'
</script>

<style>
.app-container {
  text-align: center;
  padding: 20px;
  background: linear-gradient(180deg, #0e153a, #1b2845);
  min-height: 100vh;
  color: white;
  font-family: 'Segoe UI', sans-serif;
}
</style>
