echo "Initialising the flaskening";
echo "$(($(ps -fA | grep flask | wc -l) -gt $2))";
echo "$(($(ps -fA | grep chromium | wc -l) -gt $2))";

if (($(ps -fA | grep flask | wc -l) -gt $2));
then
    echo "Killing flask";
    kill $(ps -fA | grep flask | awk '{print $2}');
fi
if (($(ps -fA | grep chromium | wc -l) -gt $2));
then
    echo "Killing chromium";
    kill $(ps -fA | grep chromium | awk '{print $2}');
fi
export FLASK_APP=app
export FLASK_ENV=development
cd /home/pi/displayer
flask run --host=0.0.0.0&
DISPLAY=:0 chromium-browser --kiosk --disable-restore-session-state localhost:5000 &