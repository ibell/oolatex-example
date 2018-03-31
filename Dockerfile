FROM ubuntu:17.10

RUN apt-get update -qq \
  && apt-get install -y  \
  libarchive-zip-perl libfile-which-perl libimage-size-perl  \
  libio-string-perl libjson-xs-perl libtext-unidecode-perl \
  libparse-recdescent-perl liburi-perl libuuid-tiny-perl libwww-perl \
  libxml2 libxml-libxml-perl libxslt1.1 libxml-libxslt-perl  \
  texlive texlive-latex-extra imagemagick libimage-magick-perl git g++ \
  make

RUN git clone https://github.com/brucemiller/LaTeXML.git \
  && cd LaTeXML \
  && perl Makefile.PL \
  && make \
  && make install

RUN mkdir oo
