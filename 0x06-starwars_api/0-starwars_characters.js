#!/usr/bin/node
const axios = require('axios');

if (process.argv.length < 3) {
  console.error("Usage: ./script.js <Movie ID>");
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data
axios.get(baseUrl)
  .then(response => {
    const movieData = response.data;

    if (!movieData.title) {
      console.error("Movie not found.");
      process.exit(1);
    }

    console.log(`Characters in '${movieData.title}':`);

    // Fetch and print each character's name
    const characterPromises = movieData.characters.map(url => axios.get(url));
    return Promise.all(characterPromises);
  })
  .then(characterResponses => {
    characterResponses.forEach(res => {
      console.log(res.data.name);
    });
  })
  .catch(error => {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  });
