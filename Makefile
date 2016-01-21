serve:
ifndef account_sid
ifndef auth_token
ifndef phone_number_sid
	@ echo "Usage: make serve account_sid=<account_sid> auth_token=<auth_token> phone_number_sid=<phone_number_sid> [app_route=<app_route>]"
	@ exit 1
endif
endif
endif
	@. venv/bin/activate; \
		echo "Bootstrapping app..."; \
		python bootstrap.py $(account_sid) $(auth_token) $(phone_number_sid) $(app_route); \
		echo "Starting Flask server..."; \
		python run.py

install: venv configure
	@. venv/bin/activate; \
		echo "Resolving Python dependencies..."; \
		pip install --upgrade -r requirements.txt

configure:
	@. venv/bin/activate; \
		python configure.py

venv:
	@ echo "Setting up virtual environment..."
	@ virtualenv venv

clean:
	@ echo "Deleting virtual environment..."
	@ rm -rf venv
