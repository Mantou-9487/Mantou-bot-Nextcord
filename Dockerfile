FROM python:3.10
# Create directory
RUN mkdir /app

#Copy stuff into /app
COPY ./ /app

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main1.py"]
