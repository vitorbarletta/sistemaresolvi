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
from selenium import webdriver
import win32com.client as win32
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import win32com.client as win32
import xlwings as xw

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_robo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_robo))

        # PAGE 2
        self.ui.btn_page_config.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_config))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE PASTA
        ########################################################################
        self.ui.page_config_file_button.clicked.connect(self.select_directory)

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE ARQUIVO EFFECTI
        self.ui.page_config_effecti_button.clicked.connect(self.select_effecti_archive)

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE ARQUIVO DE DECLARACAO
        self.ui.page_config_declaracao_button.clicked.connect(self.select_declaracao_archive)

        ## CONFIG BUTTON -> ABRE A ESCOLHA DE ARQUIVO DE PLANILHA DE PROPOSTA
        self.ui.page_config_proposta_button.clicked.connect(self.select_proposta_archive)

        ## CONFIG LOG FIELD -> CAMPO DE LOG PARA A PAGINA DE CONFIGURAÇÃO
        self.ui.page_config_log_field.setReadOnly(True)
        
        ## CONFIG LOG FIELD -> BOTÃO PARA SALVAR AS CONFIGURAÇÕES
        self.ui.page_config_save_button.clicked.connect(self.save_config)

        ## ROBO BUTTON -> BOTÃO PARA INICIAR O PROCESSO
        self.ui.page_robo_start_button.clicked.connect(self.process)
        
        ## ROBO BUTTON -> BOTÃO PARA PARAR O PROCESSO
        self.ui.page_robo_stop_button.clicked.connect(self.stop_process)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    def backDir():
        os.chdir('..')
    
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

    def select_effecti_archive(self):
        selected_effecti_archive, _ = QFileDialog.getOpenFileName(self, "Escolher a planilha Effecti", "", "All Files (*)")
        if selected_effecti_archive:
            self.temp_effecti_archive = selected_effecti_archive
            self.write_config_log("=> Planilha Effecti escolhida com sucesso", "green")
        else:
            self.write_config_log("=> Erro na escolha da Planilha Effecti", "red")
        print(self.temp_effecti_archive)

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

        if self.temp_directory:
            self.directory = self.temp_directory
            self.write_config_log(f"Pasta salva: {self.directory}", "green")
        
        if self.temp_effecti_archive:
            self.effecti_archive = self.temp_effecti_archive
            self.write_config_log(f"Arquivo HTML salvo: {self.effecti_archive}", "green")
        
        if self.temp_declaracao_archive:
            self.declaracao_archive = self.temp_declaracao_archive
            self.write_config_log(f"Declaração salva: {self.declaracao_archive}", "green")
        
        if self.temp_proposta_archive:
            self.proposta_archive = self.temp_proposta_archive
            self.write_config_log(f"Proposta salva: {self.proposta_archive}", "green")
        
        self.temp_directory = None
        self.temp_effecti_archive = None
        self.temp_declaracao_archive = None
        self.temp_proposta_archive = None

    def process(self):
        self.write_robo_log("Robô iniciado...", "white")
        self.running = True
        def run_process():
            try:
                try:
                    input_file = self.effecti_archive
                    output_file = os.path.join(os.getcwd(), 'licitacoes_combined.html') 

                    with open(input_file, 'r', encoding='utf-8') as file:
                        content = file.read()

                    soup = BeautifulSoup(content, 'html.parser')

                    combined_div = soup.new_tag('div')

                    for html in soup.find_all('html'):
                        for div in html.find_all('div'):
                            combined_div.append(div)

                    new_html = soup.new_tag('html')
                    new_head = soup.new_tag('head')
                    new_body = soup.new_tag('body')

                    new_body.append(combined_div)

                    new_head.append(soup.new_tag('title'))
                    new_head.title.string = "Effecti | Tecnologia Para Licitantes"

                    new_html.append(new_head)
                    new_html.append(new_body)

                    with open(output_file, 'w', encoding='utf-8') as file:
                        file.write(str(new_html))

                    self.write_robo_log(f"O conteúdo combinado foi salvo em '{output_file}'", "green")
                except:
                    self.write_robo_log("Erro na combinação de HTML", "red")



                with open('licitacoes_combined.html', 'r', encoding='utf-8') as file:
                    conteudo = file.read()

                pagina = BeautifulSoup(conteudo, 'lxml')

                divs = pagina.find_all('div', style=True)

                self.write_robo_log(f'{len(divs)} editais encontrados', "white")

                for div in divs:
                    try:
                        self.write_robo_log("=> Iniciando novo edital", "white")

                        links = div.find_all('a')
                        linkDownload = []
                        for index, link in enumerate(links):
                                linksPregao = link.get('href')
                                linkDownload.append(linksPregao)
                        linkDownloadFiltrado =  linkDownload[1:]      

                        tds = div.find_all('td')
                        for index,td in enumerate(tds):

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

                        datasplit = (dataPregao.split(' ')[0]).split('/')[:2]
                        dataPregao = ' '.join(datasplit)
                        hora_split = (dataPregao.split(' ')[1]).split(':')[:2]
                        horaPregao = ' '.join(hora_split)


                        caracteres_proibidos = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

                        numeroPregao_limpo = ''.join(caracter for caracter in numeroPregao if caracter not in caracteres_proibidos)
                        portalPregao_limpo = ''.join(caracter for caracter in portalPregao if caracter not in caracteres_proibidos)
                        orgaoPregao_limpo = ''.join(caracter for caracter in orgaoPregao if caracter not in caracteres_proibidos)
                        uasgPregao_limpo =''.join(caracter for caracter in uasgPregao if caracter not in caracteres_proibidos)
                        
                        
                        
                        nome_pasta = "{} - {} - {}H - {} {} - UASG {}".format(idEffecti,dataPregao,horaPregao,portalPregao_limpo,numeroPregao_limpo,uasgPregao_limpo)

                        try:
                            os.chdir(self.directory)
                            print(os.getcwd())
                            os.mkdir(nome_pasta)
                            self.write_robo_log("Pasta criada com sucesso", "green")
                        except: 
                            self.write_robo_log("Erro na criação de pasta", "red")

                        try:
                            os.chdir(nome_pasta)
                            pathOriginal = os.getcwd()
                            os.mkdir("DADOS DO PROCESSO") #ok
                            os.mkdir("PROPOSTA DE PREÇO") #ok
                            os.mkdir("DECLARAÇÕES E ANEXOS") #ok
                            os.mkdir("DOCUMENTOS DE HABILITAÇÃO") #ok
                            self.write_robo_log("Subpastas criadas com sucesso", "green")
                            
                        except:
                            self.write_robo_log("Erro na criação das subpastas", "red")

                        try:
                            os.chdir("DADOS DO PROCESSO")
                            print("Iniciando processo...")
                            
                            self.write_robo_log("=> DADOS DO PROCESSO", "white")
                            
                            print("Configurando opções do Chrome...")
                            chrome_options = Options()
                            chrome_options.add_argument('--headless=new')
                            chrome_options.add_experimental_option("detach", True)
                            chrome_prefs = {
                                "download.default_directory": os.getcwd(),
                                "download.prompt_for_download": False,
                                "directory_upgrade": True,
                                "safebrowsing.enabled": True 
                            }
                            chrome_options.add_experimental_option("prefs", chrome_prefs)

                            servico = Service(ChromeDriverManager().install())
                            navegador = webdriver.Chrome(service=servico, options=chrome_options)

                            navegador.set_window_size(1200, 1020)

                            for url in linkDownloadFiltrado:
                                navegador.get(url)
                                time.sleep(4)

                            navegador.delete_all_cookies()
                            navegador.quit()    
                            self.write_robo_log("Download dos editais concluído", "green")
                        except:
                            self.write_robo_log("Erro nos dados do processo", "red")

                        os.chdir(pathOriginal)
                        print(os.getcwd())

                        try:
                            os.chdir("DECLARAÇÕES E ANEXOS")
                            self.write_robo_log("=> DECLARAÇÕES E ANEXOS", "white")
                            caminho_modificado = os.getcwd()
                            declaracaoWord = os.path.join(caminho_modificado,"DECLARACOES - MG.docx")
                            declaracaoPDF = os.path.join(caminho_modificado,"DECLARACOES - MG.pdf")
                            shutil.copy(self.declaracao_archive, os.getcwd())

                            print(declaracaoWord)
                            print(declaracaoPDF)

                            declaracao = Document("DECLARACOES - MG.docx")

                            declaracao.core_properties.author = orgaoPregao
                            declaracao.core_properties.subject = numeroPregao
                            declaracao.save("DECLARACOES - MG.docx")
                            self.write_robo_log("Declaração alterada com sucesso", "green")

                        except Exception as e:
                            self.write_robo_log(f"Erro na alteração das declarações: {str(e)}", "red")

                        try:
                            word = win32.gencache.EnsureDispatch('Word.Application')
                            doc = word.Documents.Open(declaracaoWord)
                            doc.SaveAs(declaracaoPDF, FileFormat=17)  # 17 é o formato para PDF
                            doc.Close()
                            word.Quit()
                            self.write_robo_log("Sucesso na conversão de PDF", "green")
                        except Exception as e:
                            self.write_robo_log(f"Erro na conversão de PDF: {str(e)}", "red")

                        os.chdir(pathOriginal)
                        
                        try:
                            print(os.getcwd())
                            self.write_robo_log("=> PROPOSTA DE PREÇO", "white")
                            os.chdir("PROPOSTA DE PREÇO")
                            shutil.copy(self.proposta_archive, os.getcwd())

                            arquivo_excel = ("PLANILHA PROPOSTA R2 OFICIAL.xlsx")
                            app = xw.App(visible=False)
                            workbook = app.books.open(arquivo_excel)
                            aba_ativaPreco = workbook.sheets[0]  # Seleciona a primeira aba

                            # Modificando as células
                            aba_ativaPreco.range("B11").value = orgaoPregao
                            aba_ativaPreco.range("C13").value = numeroPregao

                            # Salvando a planilha sem perder a logo
                            workbook.save(arquivo_excel)
                            workbook.close()
                            app.quit()

                            print(os.getcwd())
                            self.write_robo_log("Dados da planilha de precificação alterados", "green")
                            
                        except Exception as e:
                            self.write_robo_log(f"{str(e)}", "red")

                    except Exception as e:
                            self.write_robo_log(f"Erro no edital: {str(e)}", "red")
                os.remove(output_file)
                self.write_config_log("Robô finalizado", "white")
            
            except:
                self.write_robo_log("Erro no robô", "red")
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
