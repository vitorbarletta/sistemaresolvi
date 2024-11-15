from bs4 import BeautifulSoup

with open('licitacoes_combined.html', 'r', encoding='utf-8') as file:
    conteudo = file.read()

pagina = BeautifulSoup(conteudo, 'lxml')

divs = pagina.find_all('div', style=True)

print(len(divs))


for div in divs:
    links = div.find_all('a')
    linkDownload = []
    for index, link in enumerate(links):
            linksPregao = link.get('href')
            linkDownload.append(linksPregao)
    print(linkDownload[1:])        
            

    tds = div.find_all('td')
    for index,td in enumerate(tds):
        # print(f'INDICE:{index} - CONTEUDO: {td}' )

        if index == 6:
            idEffecti = td.get_text(strip=True)
            print("ID EFFECTI: " + idEffecti)
        
        if index == 8:
            numeroPregao = td.get_text(strip=True)
            print("NUMERO PREGAO: " + numeroPregao)

        if index == 9:
            uasgPregao = td.get_text(strip=True)
            print("UASG: " + uasgPregao)
        
        if index == 10:
            ufPregao = td.get_text(strip=True)
            print("UF: " + ufPregao)

        if index == 16:
            modalidadePregao = td.get_text(strip=True)
            print("MODALIDADE:" + modalidadePregao)

        if index == 19:
            dataPregao = td.get_text(strip=True)
            print("DATA: " + dataPregao)

        if index == 22:
            portalPregao = td.get_text(strip=True)
            print("PORTAL: " + portalPregao)

        if index == 24:
            orgaoPregao = td.get_text(strip=True)
            print("ORGAO: " + orgaoPregao)
        
        
        
        
    print("=" * 10)
