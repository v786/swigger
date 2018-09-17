import requests

def getCord(location):
  address = location
  api_key = "<AIzaSyCmK4Y5QwyeU6TsrBVJxsJVyIYN7oZz14w"
  api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
  api_response_dict = api_response.json()

  if api_response_dict['status'] == 'OK':
      latitude = api_response_dict['results'][0]['geometry']['location']['lat']
      longitude = api_response_dict['results'][0]['geometry']['location']['lng']
      key = [latitude, longitude]
      return key