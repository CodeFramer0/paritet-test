<template>
  <form class="upload-form" @submit.prevent="handleSubmit">
    <h2>Добавить изображение</h2>

    <input type="file" @change="handleFileChange" />
    <input v-model="description" type="text" placeholder="Описание" />
    <button type="submit" :disabled="loading">
      {{ loading ? "Загрузка..." : "Отправить" }}
    </button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const emit = defineEmits(['uploaded'])
const file = ref<File | null>(null)
const description = ref('')
const loading = ref(false)

const handleFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement
  if (target.files?.[0]) file.value = target.files[0]
}


const handleSubmit = async () => {
  if (!file.value) return
  loading.value = true

  const reader = new FileReader()
  reader.onload = async () => {
    try {
      const base64 = reader.result as string
      await axios.post(
        '/api/images/',
        { image_base64: base64, description: description.value },
        { headers: { Authorization: `Token ${import.meta.env.VITE_API_TOKEN}` } }
      )
      emit('uploaded')
      description.value = ''
      file.value = null
    } catch (e) {
      console.error('Ошибка загрузки', e)
    } finally {
      loading.value = false
    }
  }

  reader.readAsDataURL(file.value)
  
}


</script>

<style lang="scss" scoped>
.upload-form {
  background: #fff;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  max-width: 400px;
  margin: 0 auto 3rem;

  h2 {
    text-align: center;
    margin-bottom: 1rem;
    font-size: 1.25rem;
  }

  input[type="file"],
  input[type="text"] {
    display: block;
    width: 100%;
    margin-bottom: 1rem;
    padding: 0.5rem;
    font-size: 0.9rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    width: 100%;
    padding: 0.5rem;
    background: #007bff;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    transition: background 0.2s;

    &:hover {
      background: #0056b3;
    }

    &:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
  }
}
</style>
