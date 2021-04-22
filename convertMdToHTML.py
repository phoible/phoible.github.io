import os
from os import path
import bs4
import re
from ipapy import is_valid_ipa

# Edit the following path
RSTUDIO_PANDOC = '/Applications/RStudio.app/Contents/MacOS/pandoc'


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
            table['class'] = 'table table-bordered order-column compact stripe dataTable no-footer table-nonfluid'
            table['role'] = 'grid'
        for th in ths:
            th['role'] = 'row'

        ps = soup.find_all('p')
        # fix blockquotes
        for p in ps:
            if '&gt;' in str(p):
                p_temp = str(p).split('&gt;')
                p.clear()
                p.string = p_temp[0].replace('<p>','')
                blockquote = soup.new_tag('blockquote')
                blockquote.append(bs4.BeautifulSoup(p_temp[1][0: len(p_temp) - 6], 'html.parser'))
                p.append(blockquote)
        # fix <em> Spacing
        ems = soup.find_all('em')
        for em in ems:
            temp = str(em).replace('<em>', '').replace('</em>', '').strip()
            em.clear()
            em.append(bs4.BeautifulSoup(temp, 'html.parser'))
        # fix references
        references_div = soup.find('div', {'class':'references'})
        if references_div is not None:
            references_ps = references_div.find_all('p')
            for p in references_ps:
                # fix url
                if 'Online: urlhttp' in str(p):
                    p_temp = p.get_text().split('Online: urlhttp')
                    p.string = p_temp[0]
                    a = soup.new_tag('a')
                    a.string = 'http' + p_temp[1]
                    a['href'] = a.string
                    p.append(a)
                # fix spacing
                if ' ,' in str(p):
                    p.string = re.sub(r' +,', ',', p.get_text())
                if ' .' in str(p):
                    p.string = re.sub(r' +.', '.', p.get_text())
                if p.get_text().endswith(':'):
                    p.string = p.get_text()[0 : len(p.get_text()) - 1] + '.'
        # fix titles size
        h2s = soup.find_all('h2')
        for h2 in h2s:
            h2.name = 'h3'
        h1s = soup.find_all('h1')
        for h1 in h1s:
            h1.name = 'h2'

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
    """
    change the columns with name "phonemes" to charissil font
    """
    with open(file_path) as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        ths = soup.find_all('th')
        for th in ths:
            if th.get_text().lower() == 'phonemes':
                ths_temp = th.parent.find_all('th')
                index = -1
                for th_temp in ths_temp:
                    index += 1
                    if th_temp.get_text().lower() == 'phonemes':
                        break
                table = th.parent.parent.parent
                tbody = table.find('tbody')
                trs = tbody.find_all('tr')
                for tr in trs:
                    td = tr.find_all('td')[index]
                    td['class'] = 'charissil'
        div_content = soup.find('div', {'class': 'container-fluid main-container'})
        with open(output_path, 'w') as file:
            file.write(str(div_content))


def fix_conventions(file_path, output_path):
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
            table['class'] = 'table table-bordered order-column compact stripe dataTable no-footer table-nonfluid'
            table['role'] = 'grid'
        for th in ths:
            th['role'] = 'row'
        tbodys = soup.find_all('tbody')
        for tbody in tbodys:
            counter = 1
            for tr in tbody.find_all('tr'):
                if counter % 2 == 0:
                    tr['class'] = 'even'
                else:
                    tr['class'] = 'odd'
                counter += 1
        # fix titles size
        h2s = soup.find_all('h2')
        for h2 in h2s:
            h2.name = 'h3'
        h1s = soup.find_all('h1')
        for h1 in h1s:
            h1.name = 'h2'
        with open(output_path, 'w') as file:
            file.write(str(soup))


def main():
    print('Start kniting Rmd to HTML...')
    print('File: _faq.Rmd')
    os.system('Rscript --vanilla knitRmdToHTML.R _faq.Rmd ' + RSTUDIO_PANDOC)
    change_table_font('_faq.html', '_faq.html')
    extract_content('_faq.html', 'faq_with_indexes.html')
    print('File: conventions.rst')
    os.system('rst2html5 conventions.rst conventions.html')
    fix_conventions('conventions.html', 'conventions.html')
    print('Converted! Output files: \033[94m faq_with_indexes.html conventions.html')


if __name__ == '__main__':
    main()
