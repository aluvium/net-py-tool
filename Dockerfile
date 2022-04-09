FROM python:latest
RUN apt-get update && apt-get install git -y
RUN git clone https://github.com/aluvium/net-py-tool.git
WORKDIR /net-py-tool/
CMD [ "sh" ]
