export FLASK_APP=app
export FLASK_ENV=development 
flask run &
DISPLAY=:0 chromium-browser --kiosk localhost:5000