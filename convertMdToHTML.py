import os
from os import path
# Edit the following path
RSTUDIO_PANDOC = "/Applications/RStudio.app/Contents/MacOS/pandoc"

print("Start kniting Rmd to HTML...")
print("File: _faq.Rmd")
os.system("Rscript --vanilla knitRmdToHTML.R _faq.Rmd " + RSTUDIO_PANDOC)
print("File: conventions.Rmd")
os.system("Rscript --vanilla knitRmdToHTML.R conventions.md " + RSTUDIO_PANDOC)
