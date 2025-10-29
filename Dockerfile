FROM python:3.11-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV MY_ENV=test_27.10
EXPOSE 8000

# Запуск сервера Django (для разработки)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]