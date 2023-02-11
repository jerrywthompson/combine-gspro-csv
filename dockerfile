FROM python:3.10

WORKDIR /app
COPY . .

#RUN pip install -r requirements.txt


RUN : \
    && pip install --upgrade pip \
    && apt-get update \
    && pip install pandas \
    && pip install configparser \
    && mkdir -p /etc/sudoers.d \
    && apt-get clean
#    && rm -rf /var/lib/apt/lists/* \

#ENV DISPLAY :0
#RUN python3.8 -m venv /venv
#ENV PATH=/venv/bin:$PATH
#RUN python createRecipeWebpage/main.py


RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
#    mkdir -p /etc/sudoers && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer
ENV DISPLAY=:0

#    && pip install -r ${appPath}requirements.txt \
#    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
#        software-properties-common \
#    && add-apt-repository -y ppa:deadsnakes \
#    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \



ENTRYPOINT [ "python", "app.py" ]

