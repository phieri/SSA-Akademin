FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get --quiet update && \
    apt-get --quiet --assume-yes install \
	language-pack-sv
