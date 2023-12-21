/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../static/**/*.js'
],
  theme: {
    extend: {
      backgroundImage:{
        "main": "url('/static/img/torreATInside.jpg')",
        "main2": "url('/static/img/panelesFV.jpg')",
        "contact" : "url('/static/img/Electronic.jpg')",

      }
    },
    fontFamily: {
      "exo": ['"exo 2"'],
      "rale": ['"Raleway"'],
    },
  },
  plugins: [],
}