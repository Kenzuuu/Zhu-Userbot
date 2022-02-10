# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━     By Kenzhu    ━━━━━

RUN git clone -b Kenzhu https://github.com/Kenzuuu/Zhu /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Kenzuuu/Zhu-Userbot/Kenzhu/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
