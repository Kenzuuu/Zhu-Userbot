FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Kenzhu https://github.com/Kenzuuu/Zhu-Userbot /home/Kenzhu/ \
    && chmod 777 /home/Kenzhu \
    && mkdir /home/Kenzhu/bin/
WORKDIR /home/Kenzhu/
COPY ./sample_config.env ./config.env* /home/Kenzhu/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
