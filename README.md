# WeatherDataProject

A Django web server to collate data from ESP8266 weather stations. Provides an API for students to be able to push their data to a central server which can then provide the data for download  for use in analytics.

Currently the API provides two endpoints:

  /students/ for listing all of the students currently registered in the database
  
  /weatherdata/ has both get and post methods for accessing temperature records.
  
