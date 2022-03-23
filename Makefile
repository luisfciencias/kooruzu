## ------------------------------
## Help menu for Makefile targets
## ------------------------------
help:	  ## shows this help menu
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

analysis: ## main analysis
	python analysis.py

install:  ## install requirements
	pip install -r requirements.txt

split:    ## group by data set by store number
	python split_stores.py
 
