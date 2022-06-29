test:
	py.test tests

release:
	check-manifest
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
