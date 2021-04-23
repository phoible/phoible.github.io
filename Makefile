.PHONY: conventions

conventions:
	mkdir -p conventions; \
	rst2html5.py \
	--no-generator \
	--no-datestamp \
	--no-section-numbering \
	--stylesheet-path=css/conventions.css,css/main.css \
	--link-stylesheet \
	conventions.rst \
	conventions/index.html
