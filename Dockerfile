FROM ubuntu:latest


RUN apt-get update && apt-get install -y python3

COPY mkdir.py /home/mkdir.py

RUN python3 /home/mkdir.py

RUN echo "CTF{flag}" > /home/dir1_26/dir2_32/flag.txt

RUN useradd -m user

RUN chmod 755 /home

RUN echo 'echo "Bienvenue dans ce CTF. Vous aurez peut-être besoin des commandes ls, cd, find, cat pour trouver le flag : un fichier flag.txt !"' >> /home/user/.bashrc

USER user

WORKDIR /home

CMD ["/bin/bash"]
