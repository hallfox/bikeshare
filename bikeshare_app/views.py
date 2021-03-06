from bikeshare_app import app
from bikeshare_app.models import User

# Index page
# Lets just show what bikes are available and have a link to checkout a bike
@app.route("/")
def index():
    return User.objects.first().name

# Admin page
# Display bike availabilities again. Ability to alter database info
@app.route("/admin")
def admin():
    return "Admin page"

# Bike request endpoint
@app.route("/request_bike/<user_email>/<int:bike_id>")
def request_bike():
    return "Bike request"
