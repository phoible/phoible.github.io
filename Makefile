.PHONY: conventions

conventions:
	mkdir -p conventions; \
	rst2html5 \
	--template=_template.html \
	--stylesheet=css/conventions.css \
	--stylesheet=css/main.css \
	conventions.rst | \
	python _html5_postprocessor.py > \
	conventions/index.html
