import xml.etree.ElementTree as ET
import xlwings as xw

# Lê o arquivo XML
with open('5736831.xml', 'r', encoding='utf-8') as file:
    xml_data = file.read()

# Lista de códigos para filtrar
itensArray = [2, 45, 72, 30, 31, 43, 47, 85, 86, 87, 88]

# Parse do XML
try:
    root = ET.fromstring(xml_data)
except ET.ParseError as e:
    print(f"Erro ao processar o XML: {e}")
    exit()

# Caminho da planilha
caminho_planilha = 'PLANILHA PROPOSTA R2 OFICIAL.xlsx'

try:
    # Abre a planilha no Excel
    app = xw.App(visible=True)  # Torna visível para depuração
    workbook = app.books.open(caminho_planilha)
    sheet = workbook.sheets[0]  # Ajuste a aba conforme necessário

    # Linha inicial para escrever os dados
    linha_inicial = 21
    linha_primeiro_item = linha_inicial

    # Itera pelos itens do XML
    for item in root.findall(".//item"):  # Procura por todos os elementos <item>
        try:
            # Extrai os dados
            codigo = int(item.find('codigo').text)
            unidade = item.find('unidade').text
            quantidade = int(item.find('quantidade').text)
            objeto = item.find('objeto').text

            # Verifica se o código está na lista
            if codigo in itensArray:
                print(f"ACHOU UM ITEM: Código={codigo}, Unidade={unidade}, Quantidade={quantidade}, Objeto={objeto}")
                sheet[f"A{linha_inicial}"].value = codigo
                sheet[f"B{linha_inicial}"].value = objeto
                sheet[f"C{linha_inicial}"].value = unidade
                sheet[f"E{linha_inicial}"].value = quantidade
                sheet[f"G{linha_inicial}"].formula = f"=F{linha_inicial}*E{linha_inicial}"

                intervalo = f"A{linha_inicial}:G{linha_inicial}"
                for cell in sheet.range(intervalo):
                    for border_id in range(7, 13):  # IDs 7 a 12 correspondem às bordas
                        cell.api.Borders(border_id).LineStyle = 1  # Linha contínua
                        cell.api.Borders(border_id).Weight = 2    # Espessura média (xlThin)
                linha_inicial += 1
        except Exception as e:
            print(f"Erro ao processar item: {ET.tostring(item, encoding='unicode')} - Erro: {e}")

    # Adiciona texto "Total:" mesclado e estilizado ao final
    linha_total = linha_inicial  # Linha após os itens inseridos
    range_total = f"A{linha_total}:F{linha_total}"
    sheet.range(range_total).merge()  # Mescla as células de A até F
    sheet[f"A{linha_total}"].value = "Total:"
    sheet[f"A{linha_total}"].font.bold = True  # Negrito
    sheet[f"A{linha_total}"].api.HorizontalAlignment = -4152  # Alinhado à direita (xlRight)

    sheet[f"G{linha_total}"].formula = f"=SUM(G{linha_primeiro_item}:G{linha_inicial - 1})"
    sheet[f"G{linha_total}"].font.bold = True  # Negrito para o total

    # Salva a planilha
    workbook.save()
    print("Dados adicionados com sucesso!")
except Exception as e:
    print(f"Erro ao manipular a planilha: {e}")
finally:
    # Fecha a planilha e o Excel
    workbook.close()
    app.quit()
