docker build -t fake-news-detector .
docker run -p 8000:8000 --gpus all fake-news-detector