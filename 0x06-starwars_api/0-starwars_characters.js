#!/usr/bin/node

// Import the request module
const request = require('request');

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided as an argument,
// if not, display usage instructions and exit
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the URL to fetch movie data from the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make an HTTP GET request to the Star Wars API to fetch movie data
request(apiUrl, (error, response, body) => {
  // Handle any errors that may occur during the request
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Check if the request was successful (status code 200)
  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data:', response.statusCode);
    process.exit(1);
  }

  // Parse the JSON response body to extract movie data
  const filmData = JSON.parse(body);
  // Extract the list of characters from the movie data
  const characters = filmData.characters;

  // Iterate over each character URL in the list
  characters.forEach(characterUrl => {
    // Make an HTTP GET request to fetch data for each character
    request(characterUrl, (error, response, body) => {
      // Handle any errors that may occur during the request
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Check if the request was successful (status code 200)
      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data:', response.statusCode);
        return;
      }

      // Parse the JSON response body to extract character data
      const characterData = JSON.parse(body);
      // Display the name of the character
      console.log(characterData.name);
    });
  });
});

