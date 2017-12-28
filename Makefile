.PHONY: data

data: 
	rm -rf data
	mkdir data
	python scripts/clean-raw-data.py
