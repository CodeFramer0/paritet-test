<template>
  <div class="container">
    <h1 class="title">Галерея</h1>
    <UploadForm @uploaded="fetchImages" />
    <ImageList :images="images" @deleted="fetchImages" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import type { Image } from './types/Image'
import UploadForm from './components/UploadForm.vue'
import ImageList from './components/ImageList.vue'

const images = ref<Image[]>([])

const fetchImages = async () => {
  const res = await axios.get<Image[]>('/api/images/', {
    headers: { Authorization: `Token ${import.meta.env.VITE_API_TOKEN}` }
  })
  images.value = res.data
}

onMounted(fetchImages)
</script>

<style lang="scss" scoped>
.container {
  max-width: 960px;
  margin: 0 auto;
  padding: 2rem;
}

.title {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2rem;
  color: #333;
}
</style>
