#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
    const baseUrl = 'https://swapi-api.alx-tools.com/api';
    
    // Get the movie data
    request(`${baseUrl}/films/${movieId}`, function (error, response, body) {
        if (error || response.statusCode !== 200) {
            console.error(`Error: Could not fetch movie with ID ${movieId}`);
            process.exit(1);
        }

        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;
        
        // Counter to keep track of completed requests
        let completed = 0;
        
        // Process each character URL in sequence to maintain order
        characterUrls.forEach((charUrl, index) => {
            request(charUrl, function (error, response, body) {
                if (!error && response.statusCode === 200) {
                    const character = JSON.parse(body);
                    // Store character with original index to maintain order
                    characters[index] = character.name;
                }
                completed++;
                
                // Print all characters in order when all requests are done
                if (completed === characterUrls.length) {
                    characters.forEach(name => console.log(name));
                }
            });
        });
    });
}

// Check if movie ID was provided
if (process.argv.length !== 3) {
    console.log('Usage: ./script.js <movie_id>');
    process.exit(1);
}

// Get and validate movie ID
const movieId = parseInt(process.argv[2]);

if (isNaN(movieId)) {
    console.log('Error: Movie ID must be a number');
    process.exit(1);
}

// Array to store characters in correct order
const characters = [];

// Run the main function
getMovieCharacters(movieId);
