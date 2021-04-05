import os
from os import path
import bs4
import re

# Edit the following path
RSTUDIO_PANDOC = "/Applications/RStudio.app/Contents/MacOS/pandoc"


def generate_indexes(file_path, output_path):
    soup = None
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), "html.parser")
        ul = soup.new_tag("ul")
        new_li = True
        li = None
        li_ul = None
        for h in soup.find_all(re.compile(r'h[1-2]+')):
            if 'class=\"title' not in str(h):
                h_str = str(h.findAll(text=True))
                h['id'] = re.sub('[^a-zA-Z-]+', '', h_str.replace(" ", "-"))
                if h.name == 'h1':
                    if li is not None and li_ul is not None:
                        li.append(li_ul)
                        li_ul = None
                    new_li = True
                    li = soup.new_tag('li')
                    a = soup.new_tag('a', href="#" + h['id'])
                    a.string = h.string
                    li.append(a)
                    ul.append(li)
                if li is not None and h.name == 'h2':
                    if new_li:
                        new_li = False
                        li_ul = soup.new_tag('ul')
                    li_2 = soup.new_tag('li')
                    a = soup.new_tag('a', href="#" + h['id'])
                    a.string = h.string
                    li_2.append(a)
                    li_ul.append(li_2)
                # print(h)
        if li_ul is not None:
            li.append(li_ul)
        # print(ul.prettify())
        div_intro = soup.find("div", {"id": "introduction"})
        div_intro.insert(0, ul)
    with open(output_path, "w") as file:
        file.write(soup.prettify())


def extract_content(file_path, output_path):
    div_content = None
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), "html.parser")
        div_content = soup.find("div", {"class": "container-fluid main-container"})
        print(div_content)
        with open(output_path, "w") as file:
            file.write(div_content.prettify())


def main():
    print("Start kniting Rmd to HTML...")
    print("File: _faq.Rmd")
    os.system("Rscript --vanilla knitRmdToHTML.R _faq.Rmd " + RSTUDIO_PANDOC)
    extract_content("_faq.html", "_faq.html")
    print("Generating FAQ indexes...")
    generate_indexes("_faq.html", "faq_with_indexes.html")
    print("File: conventions.Rmd")
    os.system("Rscript --vanilla knitRmdToHTML.R conventions.md " + RSTUDIO_PANDOC)
    extract_content("conventions.html", "conventions.html")
    print('Converted! Output files: \033[94m faq_with_indexes.html conventions.html')


if __name__ == "__main__":
    main()
