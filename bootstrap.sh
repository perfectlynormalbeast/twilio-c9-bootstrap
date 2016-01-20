pip install -r requirements.txt
python bootstrap.py $1 $2 $3
python run.py
killall -9 ngrok
