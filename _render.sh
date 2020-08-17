Rscript -e "rmarkdown::render('_faq.Rmd', output_format=rmarkdown::md_document(variant='gfm', preserve_yaml=TRUE), output_file='faq.md')"
#Rscript -e "rmarkdown::render('_faq.Rmd', output_file='faq.html')"
# git add faq.md images/faq/*.png
