<template>
  <div class="image-list">
    <div v-for="image in images" :key="image.id" class="card">
      <img :src="image.image" :alt="image.description" />
      <p>{{ image.description }}</p>
      <button @click="deleteImage(image.id)">Удалить</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Image } from '../types/Image'
import { defineProps, defineEmits } from 'vue'
import axios from 'axios'

const props = defineProps<{ images: Image[] }>()
const emit = defineEmits(['deleted'])

const deleteImage = async (id: number) => {
  await axios.delete(`/api/images/${id}/`, {
    headers: { Authorization: `Token ${import.meta.env.VITE_API_TOKEN}` }
  })
  emit('deleted')
}
</script>

<style lang="scss" scoped>
.image-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.5rem;

  .card {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;

    img {
      width: 100%;
      height: 160px;
      object-fit: cover;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }

    p {
      font-size: 0.9rem;
      color: #555;
      text-align: center;
      margin-bottom: 0.5rem;
    }

    button {
      padding: 0.4rem 1rem;
      background: #dc3545;
      color: #fff;
      font-size: 0.85rem;
      border: none;
      border-radius: 4px;
      transition: background 0.2s;

      &:hover {
        background: #b02a37;
      }
    }
  }
}
</style>
