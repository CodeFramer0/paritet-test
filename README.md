# ParitetTest

Веб-приложение с возможностью загружать, просматривать и удалять изображения с описанием.  
Фронтенд реализован на **Vue 3 + TypeScript + SCSS**, бэкенд — на **Django REST Framework**.

---

## 📦 Backend (DRF)

### Доступные эндпоинты:

1. **Создание изображения**

   - `POST /api/images/`
   - Тело запроса:
     ```json
     {
       "image_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUg...",
       "description": "Описание изображения"
     }
     ```

2. **Получение списка изображений**

   - `GET /api/images/`
   - Пример ответа:
     ```json
     [
       {
         "id": 1,
         "image": "http://localhost/media/images/image1.png",
         "description": "Описание изображения"
       }
     ]
     ```

3. **Удаление изображения**
   - `DELETE /api/images/{id}/`

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-user/ParitetTest.git
cd ParitetTest
```

### 2. Создать `.env` файл

```bash
cp backend/.env.template backend/.env
```

### 3. Запустить проект

```bash
docker compose up --build
```

---

## 🌐 Доступ

- **DRF API:** [http://localhost/api/images/](http://localhost/api/images/)
- **Vue фронтенд:** [http://localhost/](http://localhost/)

---

## 🛠️ Технологии

- Vue 3, TypeScript, SCSS
- Vite
- Django 4+, Django REST Framework
- Docker + Compose
