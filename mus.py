from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/") #home page
def home():
    return render_template('home.html')
   
@app.route("/overview") #Overview page
def overview():
    return render_template('overview.html')

@app.route("/gallery") #Gallery page
def gallery():
    return render_template('gallery.html')

@app.route("/rooms") #rooms page
def rooms():
    return render_template('rooms.html')

@app.route("/membership") #Membership page
def membership():
    return render_template('membership.html')


@app.route('/booking', methods=['GET', 'POST'])
def booking_form():
    if request.method == 'POST':
        check_in_date = request.form.get('check_in_date')
        check_out_date = request.form.get('check_out_date')
        num_guests = request.form.get('num_guests')
        num_rooms = request.form.get('num_rooms')
        # You can process the form data here, e.g., save it to a database

    return render_template('booking_form.html')

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/contact')
def contact():
    # Contact information
    phone_number = '0971234567'
    email = 'sunnyside@example.com'

    # Map configuration (using Folium)
    import folium
    latitude = 15.3923  # Replace with the actual latitude of your hotel
    longitude = 28.3285  # Replace with the actual longitude of your hotel
    map = folium.Map(location=[latitude, longitude], zoom_start=15)

    return render_template('contact.html', phone=phone_number, email=email, map=map._repr_html_())


if __name__ == '__main__':
    app.run(debug=True)
