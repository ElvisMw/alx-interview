#!/usr/bin/node

const request = require('request');

// Parse movie ID from command-line arguments
const movieID = process.argv[2];

// Construct URL for movie information
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

// Make HTTP GET request to fetch movie information
request(movieURL, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie information:', error);
    return;
  }

  // Parse JSON response
  const movieData = JSON.parse(body);

  // Extract list of characters associated with the movie
  const characters = movieData.characters;

  // Iterate over the characters and display their names
  characters.forEach(characterURL => {
    request(characterURL, (error, response, body) => {
      if (error) {
        console.error('Error fetching character information:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
