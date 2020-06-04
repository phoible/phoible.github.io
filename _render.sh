Rscript -e "rmarkdown::render('_faq.Rmd', output_format=rmarkdown::md_document(variant='gfm', preserve_yaml=TRUE), output_file='faq.md')"
# git add faq.md images/faq/*.png
