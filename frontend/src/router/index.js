import { createRouter, createWebHistory } from 'vue-router'
import SignalVisualizer from '../components/SignalVisualizer.vue'
import VideoPlayer from '../components/VideoPlayer.vue'

const routes = [
  { path: '/', component: SignalVisualizer },
  { path: '/video', component: VideoPlayer }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
