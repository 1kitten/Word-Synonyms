# Word-Synonyms
Web-Приложение для получения синонимов слов из переданного списка.

# Установка:
### Склонировать проект командой:
```bash
git clone https://github.com/1kitten/Word-Synonyms
```

### Создание виртуального окружения:<br>
<b>MacOs/Linux</b>
```bash
python3 -m virtualenv -p python3 venv
```

<b>Windows</b>
```bash
python -m venv venv
```

### Активировать виртуальное окружение командой:<br>
<b>MacOs/Linux</b>
```bash
source venv/bin/activate
```
<b>Windows</b>
```bash
.\venv\Scripts\activate
```

### Установка всех необходимых зависимостей:
```bash
pip install -r requirements.txt
```

### Запуск проекта командой:
```bash
python main.py
```

# Инструкция

Под адресу <code> http://127.0.0.1:5000/apidocs/ </code> можно посмотреть Swagger документацию к API.<br>
Для получения <b>УСПЕШНОГО</b> результата, необходимо отправить POST запрос по адресу <code> http://127.0.0.1:5000/api/v1/word_synonyms </code> <br>
Если формат отправляемого JSON не соответствует формату, пользовать получит ошибку вида:
```json
{
  "status": "error",
  "message": "Error message"
}
```
