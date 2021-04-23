# PHOIBLE website
This is the development repository for the website http://phoible.github.io/, which provides documentation of the development and usage of the PHOIBLE database.

## About PHOIBLE
PHOIBLE is a database of phonological inventories and distinctive features, encompassing more than 1600 languages (and growing). PHOIBLE data is published in browsable form online at [PHOIBLE Online](http://phoible.org), which corresponds with the most recent year-numbered [release](https://github.com/phoible/phoible/releases) of the [development repository](https://github.com/phoible/phoible).

### Convert Conventions and FAQ source files to HTML
- Install package BS4 `pip install bs4`.
- Use `Sys.getenv("RSTUDIO_PANDOC")` in RStudio to find the RSTUDIO_PANDOC path. Edit the path in `convertMdToHTML.py RSTUDIO_PANDOC = "YOUR_PATH"`.
- Run `python convertMdToHTML.py`.
