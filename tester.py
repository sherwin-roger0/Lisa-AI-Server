
from geopy.geocoders import Nominatim

# Create a geolocator object
geolocator = Nominatim(user_agent="address_finder")

latitude = 13.0952866  # Replace with your desired latitude
longitude = 80.2072911  # Replace with your desired longitudede

# Combine the latitude and longitude into a single string
location = f"{latitude}, {longitude}"

# Use geolocator to get the location information
try:
    location_info = geolocator.reverse(location, exactly_one=True)
    
    # Extract country, city, and state from location information
    address_components = location_info.raw['address']
    
    country = address_components.get('country', 'N/A')
    city = address_components.get('city', 'N/A')
    state = address_components.get('state', 'N/A')
    
    print("Country:", country)
    print("City:", city)
    print("State:", state)
    print(address_components)
    
except Exception as e:
    print("Error:", str(e))

