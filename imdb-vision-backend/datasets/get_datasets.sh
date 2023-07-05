#!/bin/sh

# Download the file
curl -o title.basics.tsv.gz https://datasets.imdbws.com/title.basics.tsv.gz
# Unzip it
gzip -df title.basics.tsv.gz
curl -o title.episode.tsv.gz https://datasets.imdbws.com/title.episode.tsv.gz
gzip -df title.episode.tsv.gz
curl -o title.ratings.tsv.gz https://datasets.imdbws.com/title.ratings.tsv.gz
gzip -df title.ratings.tsv.gz