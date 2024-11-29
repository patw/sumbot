# SumBot
Summarize structured JSON data into LLM produced, semantically rich paragraphs.  Great for embedding!

## Local Installation

```
pip install -r requirements.txt
```

Rename the mode.json.sample to model.json.  This file is used to set the prompt format and ban tokens, the default
is ChatML format so it should work with most recent models.  Set the llama_endpoint to point to your llama.cpp running
in server mode, if it's not on the same container/server as your SumBot service (see below!)

## Downloading an LLM model

Consult with llama.cpp or ollama documentation for downloading and running a model in server mode.

## Running Sumbot API

```
uvicorn main:app --host 0.0.0.0 --port 3002 --reload
```

## Accessing API

http://localhost:3002/docs


## Example output

The Godfather is a 1972 crime drama film directed by Francis Ford Coppola and starring Marlon Brando, Al Pacino, James Caan, and Richard S. Castellano. The movie has an IMDb rating of 9.2 out of 10 based on 1,038,358 votes and a Metacritic score of 100. It was released on March 24, 1972, and won 3 Oscars with a total of 33 wins and 19 nominations. The film's plot revolves around the aging patriarch of an organized crime dynasty transferring control of his empire to his reluctant son, leading to a series of unfortunate events and conflicts within the family. The movie is available in English, Italian, and Latin languages with subtitles. It was produced by Paramount Pictures and has a runtime of 175 minutes. The film's writers include Mario Puzo (screenplay), Francis Ford Coppola (screenplay), and Mario Puzo (novel).

## Example Input

Set entity to "movies"

Use the following JSON:

```
{
    "_id": {
      "$oid": "573a1396f29313caabce4a9a"
    },
    "fullplot": "When the aging head of a famous crime family decides to transfer his position to one of his subalterns, a series of unfortunate events start happening to the family, and a war begins between all the well-known families leading to insolence, deportation, murder and revenge, and ends with the favorable successor being finally chosen.",
    "imdb": {
      "rating": 9.2,
      "votes": 1038358,
      "id": 68646
    },
    "year": 1972,
    "plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    "genres": [
      "Crime",
      "Drama"
    ],
    "rated": "R",
    "metacritic": 100,
    "title": "The Godfather",
    "lastupdated": "2015-09-02 00:08:23.680000000",
    "languages": [
      "English",
      "Italian",
      "Latin"
    ],
    "writers": [
      "Mario Puzo (screenplay)",
      "Francis Ford Coppola (screenplay)",
      "Mario Puzo (novel)"
    ],
    "type": "movie",
    "tomatoes": {
      "website": "http://www.thegodfather.com",
      "viewer": {
        "rating": 4.4,
        "numReviews": 725773,
        "meter": 98
      },
      "dvd": {
        "$date": "2001-10-09T00:00:00.000Z"
      },
      "critic": {
        "rating": 9.2,
        "numReviews": 84,
        "meter": 99
      },
      "lastUpdated": {
        "$date": "2015-09-12T17:15:13.000Z"
      },
      "consensus": "One of Hollywood's greatest critical and commercial successes, The Godfather gets everything right; not only did the movie transcend expectations, it established new benchmarks for American cinema.",
      "rotten": 1,
      "production": "Paramount Pictures",
      "fresh": 83
    },
    "poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_SX677_AL_.jpg",
    "num_mflix_comments": 131,
    "released": {
      "$date": "1972-03-24T00:00:00.000Z"
    },
    "awards": {
      "wins": 33,
      "nominations": 19,
      "text": "Won 3 Oscars. Another 30 wins & 19 nominations."
    },
    "countries": [
      "USA"
    ],
    "cast": [
      "Marlon Brando",
      "Al Pacino",
      "James Caan",
      "Richard S. Castellano"
    ],
    "directors": [
      "Francis Ford Coppola"
    ],
    "runtime": 175
  }
```
