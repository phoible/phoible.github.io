#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
library(rmarkdown)

if (length(args) < 2) {
  stop("Please provide arguments of (1)input .Rmd file (2)RStudio pandoc path.", call.=FALSE)
}
Sys.setenv(RSTUDIO_PANDOC = args[2])

render(args[1], 'html_document')
