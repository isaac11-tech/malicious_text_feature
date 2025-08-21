#bilding the image

docker build -t malicious_text_feature_project

#ran the image
docker run -d -p 8000:8000 --name myapp_container malicious_text_feature_project



