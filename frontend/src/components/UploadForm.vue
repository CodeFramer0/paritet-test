<template>
  <form @submit.prevent="handleSubmit" class="upload-form">
    <h2>Загрузить изображение</h2>

    <input type="file" @change="handleFileChange" />
    <input v-model="description" type="text" required placeholder="Описание" />

    <button type="submit">Отправить</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const emit = defineEmits<{
  (e: 'uploaded', image: { id: number; image: string; description: string }): void
}>()

const description = ref('')
const file = ref<File | null>(null)

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files[0]) {
    file.value = target.files[0]
  }
}

const handleSubmit = async () => {
  if (!file.value) return

  const reader = new FileReader()
  reader.onload = async () => {
    const base64 = reader.result as string

    const res = await axios.post(
      '/api/images/',
      {
        image: base64,
        description: description.value
      },
      {
        headers: {
          Authorization: `Token ${import.meta.env.VITE_API_TOKEN}`
        }
      }
    )

    emit('uploaded', res.data)

    description.value = ''
    file.value = null
  }

  reader.readAsDataURL(file.value)
}
</script>

<style scoped>
.upload-form {
  background: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  max-width: 400px;
  margin: 2rem auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
