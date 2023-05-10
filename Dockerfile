FROM python:3.10

EXPOSE 8501
CMD mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["Home.py"]