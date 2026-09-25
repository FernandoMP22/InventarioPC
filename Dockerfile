FROM python:3.13

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc \
    unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg

RUN curl https://packages.microsoft.com/config/debian/12/prod.list \
    -o /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY backend ./backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]