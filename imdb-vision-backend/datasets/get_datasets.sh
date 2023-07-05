#!/bin/sh

# Download the file
curl -o name.basics.tsv.gz https://datasets.imdbws.com/name.basics.tsv.gz
# Unzip it
gzip -df name.basics.tsv.gz
curl -o title.episode.tsv.gz https://datasets.imdbws.com/title.episode.tsv.gz
gzip -df title.episode.tsv.gz
curl -o title.ratings.tsv.gz https://datasets.imdbws.com/title.ratings.tsv.gz
gzip -df title.ratings.tsv.gz