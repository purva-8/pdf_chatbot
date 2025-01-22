FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8051

ENTRYPOINT ["env", "GOOGLE_API_KEY=AIzaSyDbVSR_kGCNH_qq5BSFYnBhkeIYiZzhfzc"]

CMD ["streamlit", "run", "app/app.py"]