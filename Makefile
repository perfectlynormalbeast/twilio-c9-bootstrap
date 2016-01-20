serve:
	@. venv/bin/activate; \
		echo "Bootstrapping app..."; \
		python bootstrap.py $(account_sid) $(auth_token) $(phone_number_sid); \
		echo "Starting Flask server..."; \
		python run.py
	echo "Terminating any lingering ngrok instances..."
	killall -9 ngrok

install: venv
	@. venv/bin/activate; \
		echo "Resolving Python dependencies..."; \
		pip install --upgrade -r requirements.txt

venv:
	echo "Setting up virtual environment..."
	virtualenv venv

clean:
	echo "Deleting virtual environment..."
	rm -rf venv
