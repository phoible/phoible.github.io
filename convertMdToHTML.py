import os
from os import path
import bs4
import re
from ipapy import is_valid_ipa

# Edit the following path
RSTUDIO_PANDOC = '/Applications/RStudio.app/Contents/MacOS/pandoc'


def generate_indexes(file_path, output_path):
    soup = None
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        ul = soup.new_tag('ul')
        new_li = True
        li = None
        li_ul = None
        for h in soup.find_all(re.compile(r'h[1-2]+')):
            if 'class=\'title' not in str(h):
                h_str = str(h.findAll(text=True))
                h['id'] = re.sub('[^a-zA-Z-]+', '', h_str.replace(' ', '-'))
                if h.name == 'h1':
                    if li is not None and li_ul is not None:
                        li.append(li_ul)
                        li_ul = None
                    new_li = True
                    li = soup.new_tag('li')
                    a = soup.new_tag('a', href='#' + h['id'])
                    a.string = h.string
                    li.append(a)
                    ul.append(li)
                if li is not None and h.name == 'h2':
                    if new_li:
                        new_li = False
                        li_ul = soup.new_tag('ul')
                    li_2 = soup.new_tag('li')
                    a = soup.new_tag('a', href='#' + h['id'])
                    a.string = h.string
                    li_2.append(a)
                    li_ul.append(li_2)
                # print(h)
        if li_ul is not None:
            li.append(li_ul)
        # print(ul.prettify())
        div_intro = soup.find('div', {'id': 'introduction'})
        div_intro.insert(0, ul)
    with open(output_path, 'w') as file:
        file.write(soup.prettify())


def extract_content(file_path, output_path):
    div_content = None
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        # beautify tables
        tables = soup.find_all('table')
        ths = soup.find_all('th')
        for table in tables:
            table['cellpadding'] = '0'
            table['cellspacing'] = '0'
            table['border'] = '0'
            table['class'] = 'table table-bordered order-column compact stripe dataTable no-footer'
            table['role'] = 'grid'
        for th in ths:
            th['role'] = 'row'
        div_content = soup.find('div', {'class': 'container-fluid main-container'})
        with open(output_path, 'w') as file:
            file.write(str(div_content))
            # write scripts
            with open('scripts.js') as f2:
                file.write('\n')
                file.write(f2.read())


def change_font(file_path, output_path):
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        codes = soup.find_all('code')
        for code in codes:
            code['class'] = 'charissil'
        div_content = soup.find('div', {'class': 'container-fluid main-container'})
        with open(output_path, 'w') as file:
            file.write(str(div_content))


def change_table_font(file_path, output_path):
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        tds = soup.find_all('td')
        for td in tds:
            if is_valid_ipa(str(td.string).strip()):
                td['class'] = 'charissil'
        div_content = soup.find('div', {'class': 'container-fluid main-container'})
        with open(output_path, 'w') as file:
            file.write(str(div_content))


def main():
    print('Start kniting Rmd to HTML...')
    print('File: _faq.Rmd')
    os.system('Rscript --vanilla knitRmdToHTML.R _faq.Rmd ' + RSTUDIO_PANDOC)
    change_table_font('_faq.html', '_faq.html')
    extract_content('_faq.html', '_faq.html')
    print('Generating FAQ indexes...')
    generate_indexes('_faq.html', 'faq_with_indexes.html')
    print('File: conventions.Rmd')
    os.system('Rscript --vanilla knitRmdToHTML.R conventions.md ' + RSTUDIO_PANDOC)
    change_font('conventions.html','conventions.html')
    extract_content('conventions.html', 'conventions.html')
    print('Converted! Output files: \033[94m faq_with_indexes.html conventions.html')


if __name__ == '__main__':
    main()
