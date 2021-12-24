# Docker

Docker File Example

```
┌──(kali㉿kali)-[~/tmp21/S3Scanner]
└─$ cat Dockerfile                                                                                 130 ⨯
FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install boto3
RUN pip install .
ENTRYPOINT ["python", "-m", "S3Scanner"]   
```



```
docker build . -t s3scanner:latest
docker run --rm s3scanner:latest scan --bucket my-buket
```
