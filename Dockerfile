FROM python:3.7.0

WORKDIR /usr/src/app

COPY skeleton-project/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "hello, world!" > the-file.txt

EXPOSE 5000

CMD [ "python", "skeleton-project/api/app.py" ]