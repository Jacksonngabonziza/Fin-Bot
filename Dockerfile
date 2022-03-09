FROM ubuntu:20.04ssss
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3-pip && python3 -m pip install
 --no-cache --u $he --upgrade pip && pip3 install --no-cache rasa==3.0.5
ADD . /app/
RUN chmod +x /app/start_service.sh
CMD /app/start_services.sh
