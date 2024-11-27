import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
import os
from openpyxl import load_workbook
import time
import shutil
from docx import Document
from docx2pdf import convert
import threading
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
import win32com.client as win32
import xlwings as xw
import xml.etree.ElementTree as ET
import requests
import pandas as pd
import sys

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        # PAGE 1
        self.ui.btn_page_robo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_robo))

        # PAGE 2
        self.ui.btn_page_config.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_config))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE PASTA
        ########################################################################
        self.ui.page_config_file_button.clicked.connect(self.select_directory)

        self.ui.page_config_documentos_button.clicked.connect(self.select_documentos)

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE ARQUIVO EFFECTI
        # self.ui.page_config_effecti_button.clicked.connect(self.select_effecti_archive)

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE ARQUIVO DE DECLARACAO
        self.ui.page_config_declaracao_button.clicked.connect(self.select_declaracao_archive)

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE ARQUIVO DE PLANILHA DE PROPOSTA
        self.ui.page_config_proposta_button.clicked.connect(self.select_proposta_archive)

        ## CONFIG LOG FIELD -> CAMPO DE LOG PARA A PAGINA DE CONFIGURAÇÃO
        self.ui.page_config_log_field.setReadOnly(True)
        
        ## CONFIG LOG FIELD -> BOTÃO PARA SALVAR AS CONFIGURAÇÕES
        self.ui.page_config_save_button.clicked.connect(self.save_config)

        self.ui.page_config_planilhaID_button.clicked.connect(self.select_planilhaID_archive)

        ## ROBO BUTTON -> BOTÃO PARA INICIAR O PROCESSO
        self.ui.page_robo_start_button.clicked.connect(self.process)
        
        ## ROBO BUTTON -> BOTÃO PARA PARAR O PROCESSO
        self.ui.page_robo_stop_button.clicked.connect(self.stop_process)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    def updateLabelContent(self, element, text, style):
        label = getattr(self.ui, element, None)
        if label is None:
            print(f"Erro: Atributo '{element}' não encontrado em 'self.ui'")
            return
        label.setText(text)
        label.setStyleSheet(style)

    def select_planilhaID_archive(self):
        selected_planilhaID_archive, _ = QFileDialog.getOpenFileName(self, "Escolher a proposta", "", "All Files (*)")
        if selected_planilhaID_archive:
            self.temp_planilhaID_archive = selected_planilhaID_archive
            self.write_config_log("=> Planilha de ID escolhida com sucesso", "green")
        else:
            self.write_config_log("=> Erro na escolha da Planilha de ID", "red")
        print(self.temp_planilhaID_archive)

    def write_robo_log(self, text, color):
        self.ui.page_robo_log_field.setTextColor(QColor(color))
        self.ui.page_robo_log_field.append(text)

    def write_config_log(self, text, color):
        self.ui.page_config_log_field.setTextColor(QColor(color))
        self.ui.page_config_log_field.append(text)

    def select_directory(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "Escolher pasta para salvar", "")
        if selected_directory:
            self.temp_directory = selected_directory
            self.write_config_log("=> Pasta escolhida com sucesso", "green")
        else:
            self.write_config_log("=> Erro na escolha de pasta", "red")
        print(self.temp_directory)

    # def select_effecti_archive(self):
    #     selected_effecti_archive, _ = QFileDialog.getOpenFileName(self, "Escolher a planilha Effecti", "", "All Files (*)")
    #     if selected_effecti_archive:
    #         self.temp_effecti_archive = selected_effecti_archive
    #         self.write_config_log("=> Planilha Effecti escolhida com sucesso", "green")
    #     else:
    #         self.write_config_log("=> Erro na escolha da Planilha Effecti", "red")
    #     print(self.temp_effecti_archive)
    
    def select_documentos(self):
        selected_documentos, _ = QFileDialog.getOpenFileName(self, "Escolher a planilha Effecti", "", "All Files (*)")
        if selected_documentos:
            self.temp_documentos = selected_documentos
            self.write_config_log("=> Documentos escolhidos com sucesso", "green")
        else:
            self.write_config_log("=> Erro na escolha dos Documentos", "red")

    def select_declaracao_archive(self):
        selected_declaracao_archive, _ = QFileDialog.getOpenFileName(self, "Escolher arquivo de declaração", "", "All Files (*)")
        if selected_declaracao_archive:
            self.temp_declaracao_archive = selected_declaracao_archive
            self.write_config_log("=> Declaração escolhida com sucesso", "green")
        else:
            self.write_config_log("=> Erro na escolha da declaração", "red")

        print(self.temp_declaracao_archive)

    def select_proposta_archive(self):
        selected_proposta_archive, _ = QFileDialog.getOpenFileName(self, "Escolher a proposta", "", "All Files (*)")
        if selected_proposta_archive:
            self.temp_proposta_archive = selected_proposta_archive
            self.write_config_log("=> Proposta escolhida com sucesso", "green")
        else:
            self.write_config_log("=> Erro na escolha da proposta", "red")
        print(self.temp_proposta_archive)

    def save_config(self):

        self.ui.page_config_log_field.clear()

        if self.temp_planilhaID_archive:
            self.planilhaID_archive = self.temp_planilhaID_archive
            self.write_config_log(f"Planilha de ID salva: {self.planilhaID_archive}", "green")

        if self.temp_directory:
            self.directory = self.temp_directory
            self.write_config_log(f"Pasta salva: {self.directory}", "green")
        
        # if self.temp_effecti_archive:
        #     self.effecti_archive = self.temp_effecti_archive
        #     self.write_config_log(f"Arquivo HTML salvo: {self.effecti_archive}", "green")
        
        if self.temp_declaracao_archive:
            self.declaracao_archive = self.temp_declaracao_archive
            self.write_config_log(f"Declaração salva: {self.declaracao_archive}", "green")
        
        if self.temp_proposta_archive:
            self.proposta_archive = self.temp_proposta_archive
            self.write_config_log(f"Proposta salva: {self.proposta_archive}", "green")

        if self.temp_documentos:
            self.documentos = self.temp_documentos
            self.write_config_log(f"Documentos salvos: {self.documentos}", "green")
        
        self.temp_directory = None
        self.temp_effecti_archive = None
        self.temp_declaracao_archive = None
        self.temp_proposta_archive = None
        self.temp_documentos = None

    def process(self):
        self.write_robo_log("Robô iniciado...", "white")
        self.running = True
        def run_process():
            try:
                df = pd.read_excel(self.planilhaID_archive)

                self.write_robo_log(f"{df.shape[0]} editais encontrados", "white")

                for index, row in df.iterrows():
                    self.updateLabelContent("pastaStatus", "", "color: white")
                    self.updateLabelContent("documentosStatus", "", "color: white")
                    self.updateLabelContent("downloadStatus", "", "color: white")
                    self.updateLabelContent("declaracaoStatus", "", "color: white")
                    self.updateLabelContent("pdfStatus", "", "color: white")
                    self.updateLabelContent("loginxmlStatus", "", "color: white")
                    self.updateLabelContent("planilhaStatus", "", "color: white")
                    self.updateLabelContent("itensStatus", "", "color: white")


                    idEffecti = row.iloc[0]
                    idEffecti = str(idEffecti)
                    arrayItens = row.iloc[1]
                    arrayItens = str(arrayItens)  # Força a conversão para string
                    arrayItens = [int(item) for item in arrayItens.split('-') if item.isdigit()]


                    urlLogin = "https://mdw.minha.effecti.com.br/users/login"

                    payloadLogin = {
                        "username": "rafaelleite@r2brasil.group",
                        "password": "Empresa@2024"
                    }

                    headersLogin = {
                        "Content-Type": "application/json"
                    }

                    responseLogin = requests.post(urlLogin, json=payloadLogin, headers=headersLogin)

                    if responseLogin.status_code == 200:
                        data = responseLogin.json()
                        token = data.get("token")

                        headers = {
                            "Authorization": f"Bearer {token}",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                            "Accept": "application/json, text/plain, */*"
                        }

                        urlXML = f"https://mdw.minha.effecti.com.br/aviso/edital/{idEffecti}/xml"
                        responseXML = requests.get(urlXML, headers=headers)

                        if responseXML.status_code == 200:
                            xml_content = responseXML.text
                        else:
                            print(f"Erro ao baixar XML: {responseXML.status_code}")

                        urlHTML = f"https://mdw.minha.effecti.com.br/aviso/edital/{idEffecti}/html"
                        responseHTML = requests.get(urlHTML, headers=headers)

                        if responseHTML.status_code == 200:
                            html_content = responseHTML.text
                        else:
                            print(f"Erro ao baixar HTML: {responseHTML.status_code}")

                        self.updateLabelContent("loginxmlStatus", "✔", "color: green;font-size: 18px;")

                    else:
                        self.write_robo_log(f"Erro ao fazer login: {responseLogin.status_code}", "red")
                        print(responseLogin.json())
                        self.updateLabelContent("loginxmlStatus", "❌", "color: red;font-size: 18px;")


                    pagina = BeautifulSoup(html_content, 'lxml')

                    links = pagina.find_all('a')
                    linkDownload = []
                    for index, link in enumerate(links):
                            linksPregao = link.get('href')
                            linkDownload.append(linksPregao)
                    linkDownloadFiltrado =  linkDownload[1:]  

                    tds = pagina.find_all('td')
                    for index,td in enumerate(tds):
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

                    datasplit = (dataPregao.split(' ')[0]).split('/')[:2]
                    dataPregao = ' '.join(datasplit)
                    hora_split = (dataPregao.split(' ')[1]).split(':')[:2]
                    horaPregao = ' '.join(hora_split)

                    caracteres_proibidos = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

                    numeroPregao_limpo = ''.join(caracter for caracter in numeroPregao if caracter not in caracteres_proibidos)
                    portalPregao_limpo = ''.join(caracter for caracter in portalPregao if caracter not in caracteres_proibidos)
                    portalPregao_limpo = portalPregao_limpo.upper()
                    uasgPregao_limpo =''.join(caracter for caracter in uasgPregao if caracter not in caracteres_proibidos)

                    
                    nome_pasta = "{} - {} - {}H - {} {} - UASG {}".format(idEffecti,dataPregao,horaPregao,portalPregao_limpo,numeroPregao_limpo,uasgPregao_limpo)

                    self.updateLabelContent("nomeEdital", f"{nome_pasta}", "color: #fff; background: #000; padding: 5px; border-radius: 5px; font-size: 20px")

                    try:
                        os.chdir(self.directory)
                        os.mkdir(nome_pasta)
                        os.chdir(nome_pasta)
                        pathOriginal = os.getcwd()
                        os.mkdir("DADOS DO PROCESSO") #ok
                        os.mkdir("PROPOSTA DE PREÇO") #ok
                        os.mkdir("DECLARAÇÕES E ANEXOS") #ok
                        os.mkdir("DOCUMENTOS DE HABILITAÇÃO") #ok

                        self.updateLabelContent("pastaStatus", "✔", "color: green;font-size: 18px;")
                    except Exception as e: 
                        self.updateLabelContent("pastaStatus", "❌", "color: red;font-size: 18px;")
                        self.write_robo_log(f"Erro na criação das pastas: {e}", "red")

                    try:
                        os.chdir("DOCUMENTOS DE HABILITAÇÃO")
                        shutil.copy(self.documentos, os.getcwd())
                        self.updateLabelContent("documentosStatus", "✔", "color: green;font-size: 18px;")
                    except Exception as e:
                        self.updateLabelContent("documentosStatus", "❌", "color: red;font-size: 18px;")
                        self.write_robo_log(f"Erro na cópia dos documentos: {e}", "red")

                    os.chdir(pathOriginal)

                    try:
                        os.chdir("DADOS DO PROCESSO")                    
                        for idx, url in enumerate(linkDownloadFiltrado, start=1):
                            response = requests.get(url)
                            if response.status_code == 200:
                                filename = f"edital_{idx}.pdf"
                                with open(filename, "wb") as file:
                                    file.write(response.content)
                            else:
                                self.write_robo_log(f"Erro ao baixar {url}. Código de status: {response.status_code}", "red")

                        self.updateLabelContent("downloadStatus", "✔", "color: green;font-size: 18px;")
                    except Exception as e:
                        self.updateLabelContent("downloadStatus", "❌", "color: red;font-size: 18px;")
                        self.write_robo_log(f"Erro no download dos editais: {e}", "red")

                    os.chdir(pathOriginal)

                    try:
                        os.chdir("DECLARAÇÕES E ANEXOS")
                        caminho_modificado = os.getcwd()
                        nomeDeclaracao, extensao = os.path.splitext(os.path.basename(self.declaracao_archive))

                        declaracaoWord = os.path.join(caminho_modificado,nomeDeclaracao + '.docx')
                        declaracaoPDF = os.path.join(caminho_modificado,nomeDeclaracao + '.pdf')
                        shutil.copy(self.declaracao_archive, os.getcwd())

                        declaracao = Document(nomeDeclaracao + '.docx')

                        declaracao.core_properties.author = orgaoPregao
                        declaracao.core_properties.subject = numeroPregao
                        self.updateLabelContent("declaracaoStatus", "✔", "color: green;font-size: 18px;")
                        declaracao.save(nomeDeclaracao + '.docx')

                    except Exception as e:
                        self.write_robo_log(f"Erro na alteração das declarações: {str(e)}", "red")
                        self.updateLabelContent("declaracaoStatus", "❌", "color: red;font-size: 18px;")

                    try:
                        cache_dir = os.path.join(os.path.dirname(win32.__file__), "gen_py")
                        if os.path.exists(cache_dir):
                            shutil.rmtree(cache_dir)
                        print("Cache COM limpo com sucesso.")
                    except Exception as e:
                        print(f"Erro ao limpar o cache COM: {str(e)}")


                    try:
                        word = win32.Dispatch('Word.Application')
                        doc = word.Documents.Open(declaracaoWord)
                        doc.SaveAs(declaracaoPDF, FileFormat=17) 
                        doc.Close()
                        word.Quit()
                        self.updateLabelContent("pdfStatus", "✔", "color: green;font-size: 18px;")
                    except Exception as e:
                        self.write_robo_log(f"Erro na conversão de PDF: {str(e)}", "red")
                        self.updateLabelContent("pdfStatus", "❌", "color: red;font-size: 18px;")

                    

                    os.chdir(pathOriginal)
                    
                    try:
                        os.chdir("PROPOSTA DE PREÇO")
                        shutil.copy(self.proposta_archive, os.getcwd())

                        try:
                            try:
                                root = ET.fromstring(xml_content)
                            except ET.ParseError as e:
                                print(f"Erro ao processar o XML: {e}")
                                self.updateLabelContent("loginxmlStatus", "❌", "color: red;font-size: 18px;")
                                exit()

                            caminho_planilha = os.path.basename(self.proposta_archive)

                            app = xw.App(visible=False)
                            workbook = app.books.open(caminho_planilha)
                            sheet = workbook.sheets[0]
                            sheet.range("B11").value = orgaoPregao
                            sheet.range("C13").value = numeroPregao

                            self.updateLabelContent("planilhaStatus", "✔", "color: green;font-size: 18px;")

                            try:
                                linha_inicial = 21
                                linha_primeiro_item = linha_inicial

                                for item in root.findall(".//item"):
                                    codigo = int(item.find('codigo').text)
                                    unidade = item.find('unidade').text
                                    quantidade = int(item.find('quantidade').text)
                                    objeto = item.find('objeto').text

                                    if codigo in arrayItens:
                                        sheet[f"A{linha_inicial}"].value = codigo
                                        sheet[f"B{linha_inicial}"].value = objeto
                                        sheet[f"C{linha_inicial}"].value = unidade
                                        sheet[f"E{linha_inicial}"].value = quantidade
                                        sheet[f"G{linha_inicial}"].formula = f"=F{linha_inicial}*E{linha_inicial}"

                                        intervalo = f"A{linha_inicial}:G{linha_inicial}"
                                        for cell in sheet.range(intervalo):
                                            for border_id in range(7, 13):
                                                cell.api.Borders(border_id).LineStyle = 1
                                                cell.api.Borders(border_id).Weight = 2
                                        linha_inicial += 1

                                linha_total = linha_inicial
                                range_total = f"A{linha_total}:F{linha_total}"
                                sheet.range(range_total).merge()
                                sheet[f"A{linha_total}"].value = "Total:"
                                sheet[f"A{linha_total}"].font.bold = True
                                sheet[f"A{linha_total}"].api.HorizontalAlignment = -4152

                                sheet[f"G{linha_total}"].formula = f"=SUM(G{linha_primeiro_item}:G{linha_inicial - 1})"
                                sheet[f"G{linha_total}"].font.bold = True

                                self.updateLabelContent("itensStatus", "✔", "color: green;font-size: 18px;")
                            except Exception as e:
                                self.write_robo_log(f"Erro em colocar os itens {e}", "red")
                                self.updateLabelContent("itensStatus", "❌", "color: red;font-size: 18px;")
                            finally:
                                workbook.save(caminho_planilha)
                                workbook.close()
                                app.quit()

                        except Exception as e: 
                            self.write_robo_log("Erro na alteraçao de dados da planilha", "red")
                        
                        self.write_robo_log(f"{nome_pasta} concluído com sucesso", "green")
                        
                    except Exception as e:
                        self.write_robo_log(f"{str(e)}", "red")
                        self.write_robo_log(f"{nome_pasta} concluído com falhas", "red")
                    except Exception as e:
                        self.write_robo_log(f"Erro no edital: {str(e)}", "red")
                self.write_robo_log("Robô finalizado", "white")
                
            except Exception as e:
                self.write_robo_log(f"Erro no robô: {e}", "red")
        self.process_thread = threading.Thread(target=run_process)
        self.process_thread.start()

    def stop_process(self):
        self.running = False
        if self.process_thread is not None:
            self.process_thread.join()
            self.write_robo_log("Processo finalizado.", "green")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
