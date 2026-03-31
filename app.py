from flask import Flask, render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Sample static data
sample_data = {
    "food": [
        {"name": "Campus Canteen", "contact": "9876543210", "lat": 13.0115, "lon": 80.2340}
    ],
    "rooms": [
        {"name": "PG Hostel", "contact": "9000000000"}
    ],
    "hospital": [
        {"name": "City Hospital", "contact": "108", "lat": 13.0090, "lon": 80.2320}
    ],
    "police": [
        {"name": "Police Station", "contact": "100", "lat": 13.0080, "lon": 80.2310}
    ],
    "bus": [
        {"name": "Bus Stand", "contact": "1234567890", "lat": 13.0130, "lon": 80.2360}
    ]
}

def get_location(college):
    geolocator = Nominatim(user_agent="smart_app")

    try:
        location = geolocator.geocode(college + ", Tamil Nadu")
        if location:
            return location.latitude, location.longitude
    except:
        pass

    return None, None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():
    college = request.form.get('college')

    lat, lon = get_location(college)

    return render_template(
        'dashboard.html',
        data=sample_data,
        lat=lat if lat else 13.0827,
        lon=lon if lon else 80.2707,
        college=college
    )


if __name__ == '__main__':
    app.run(debug=True)