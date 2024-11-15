from bs4 import BeautifulSoup

# Define o nome do arquivo HTML de entrada e saída
input_file = 'licitacoes (2).html'
output_file = 'licitacoes_combined.html'

# Lê o conteúdo do arquivo HTML de entrada
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Usa BeautifulSoup para analisar o HTML
soup = BeautifulSoup(content, 'html.parser')

# Cria uma nova div para armazenar todas as divs combinadas
combined_div = soup.new_tag('div')

# Encontra todas as tags <html> e extrai as <div> de cada uma
for html in soup.find_all('html'):
    for div in html.find_all('div'):
        combined_div.append(div)

# Cria um novo HTML com as divs combinadas
new_html = soup.new_tag('html')
new_head = soup.new_tag('head')
new_body = soup.new_tag('body')

# Adiciona a nova div combinada ao corpo
new_body.append(combined_div)

# Adiciona cabeçalho padrão
new_head.append(soup.new_tag('title'))
new_head.title.string = "Effecti | Tecnologia Para Licitantes"

# Monta o novo HTML
new_html.append(new_head)
new_html.append(new_body)

# Salva o novo conteúdo HTML em um arquivo
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(str(new_html))

print(f"O conteúdo combinado foi salvo em '{output_file}'")
