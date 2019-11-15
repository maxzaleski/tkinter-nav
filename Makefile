build:
			make clean; python3 setup.py sdist bdist_wheel

publish:
			make build; source venv/bin/activate; twine upload dist/*; make clean

publish-test:
			python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
			rm -rf build dist tkinter_nav.egg-info
