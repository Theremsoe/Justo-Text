clean:
	@git clean -dfX;

virtualenv:
	@python3 -m venv venv;

install:
	@( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	\ );

reinstall: clean virtualenv install
