export FLASK_APP=app
flask run &
DISPLAY=:0 chromium-browser --kiosk localhost:5000