# IMDB TV Show Rating Visualizer

## Where the data comes from
IMDB has non-commercial datasets available [here](https://developer.imdb.com/non-commercial-datasets/)

Data is refreshed daily

## To download the latest datasets
```
cd imdb-vision-backend/datasets
./get_datasets.sh
```
The datasets will be downloaded into the folder

## To create the database
`flask db upgrade head`