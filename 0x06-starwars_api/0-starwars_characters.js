#!/usr/bin/node
const fetch = require('node-fetch');

async function getMovieCharacters(movieId) {
    // Base URL for the Star Wars API
    const baseUrl = 'https://swapi-api.alx-tools.com/api';
    
    try {
        // Get the movie data
        const movieResponse = await fetch(`${baseUrl}/films/${movieId}`);
        
        if (!movieResponse.ok) {
            throw new Error(`Error: Could not fetch movie with ID ${movieId}`);
        }
        
        const movieData = await movieResponse.json();
        const characterUrls = movieData.characters;
        
        // Fetch and print each character
        for (const charUrl of characterUrls) {
            const charResponse = await fetch(charUrl);
            
            if (charResponse.ok) {
                const character = await charResponse.json();
                console.log(character.name);
            }
        }
    } catch (error) {
        console.error(error.message);
        process.exit(1);
    }
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

// Run the main function
getMovieCharacters(movieId);