import sys
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 8 #8KB

import socket
import tqdm
import os

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QPushButton)

class MainWindow(QMainWindow):
    # save settings alongside *py file
    settings = QSettings("temp.ini", QSettings.IniFormat)
     
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initSignals()
        self.restore_settings()
        self.setWindowTitle('Spice-E-Bot Recipe Configurator')
        
    def initUI(self):
        # standar UI stuff
        self.setWindowTitle('Spice-E-Bot Recipe Configurator')

        self.setObjectName('MainWindow')
        self.setWindowTitle('Program Title')
        self.setGeometry(600, 400, 700, 300)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        # create some widgets
        self.pb_add_row = QPushButton('Add Row')
        self.pb_remove_row = QPushButton('Remove Selected Row')
        self.pb_save = QPushButton('Save')
        self.pb_restore = QPushButton('Restore')
        self.pb_sendto = QPushButton('Send To Spice-E-Bot')
        
        self.tbl = QTableWidget(0, 5, self)
        
        # config up the table        
        header = self.tbl.horizontalHeader()
        input_header = ['Recipe', 'qty:Salt(tsp)', 'qty:Pepper(tsp)', 'qty:Paprika(tsp)']
        self.tbl.setHorizontalHeaderLabels(input_header)
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        # add widgets to UI
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tbl)
        self.vbox.addWidget(self.pb_add_row)
        self.vbox.addWidget(self.pb_remove_row)
        self.vbox.addWidget(self.pb_save)
        self.vbox.addWidget(self.pb_restore)
        self.vbox.addWidget(self.pb_sendto)
        wid.setLayout(self.vbox)
            
    # pb signals
    def initSignals(self):#
        self.pb_add_row.clicked.connect(self.pb_add_row_clicked)
        self.pb_remove_row.clicked.connect(self.pb_remove_row_clicked)
        self.pb_save.clicked.connect(self.pb_save_clicked)
        self.pb_restore.clicked.connect(self.pb_restore_clicked)
        self.pb_sendto.clicked.connect(self.pb_sendto_clicked)

    # reads in the ini file adn re-generate the table contents
    def restore_settings(self):
        self.setting_value = self.settings.value('table')
        self.setting_row = self.settings.value('rows')
        self.setting_col = self.settings.value('columns')
        print(f'RESTORE: {self.setting_value}')
        
        # change the table row/columns, create a dictionary out of the saved table
        try:
            self.tbl.setRowCount(int(self.setting_row))
            self.tbl.setColumnCount(int(self.setting_col))
            self.my_dict = dict(eval(self.setting_value))
        except TypeError:
            print(f'RESTORE: No ini file, resulting in no rows/columns')
        
        # loop over each table cell and populate with old values
        for row in range(self.tbl.rowCount()):
            for col in range(self.tbl.columnCount()):
                try:
                    if col == 0: self.tbl.setItem(row, col, QTableWidgetItem(self.my_dict['Recipe'][row]))
                    if col == 1: self.tbl.setItem(row, col, QTableWidgetItem(self.my_dict['qty:Salt(tsp)'][row]))
                    if col == 2: self.tbl.setItem(row, col, QTableWidgetItem(self.my_dict['qty:Pepper(tsp)'][row]))
                    if col == 3: self.tbl.setItem(row, col, QTableWidgetItem(self.my_dict['qty:Paprika(tsp)'][row]))                            
                except IndexError:
                    print(f'INDEX ERROR')          
        
    
    
    
    def pb_sendto_clicked(self):
        print("sending")
        filename = "temp.ini"
        host ="192.168.20.39"
        port =5001
        # get the file size
    
        filesize = os.path.getsize(filename)
        # create the client socket
        s = socket.socket()
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")

        # send the filename and filesize
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        # start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))

        # close the socket
        s.close()



    # add a new row to the end 

    
    def pb_add_row_clicked(self):
        current_row_count = self.tbl.rowCount()
        row_count = current_row_count + 1
        self.tbl.setRowCount(row_count)

    # remove selected row
    def pb_remove_row_clicked(self):
        self.tbl.removeRow(self.tbl.currentRow())
    
    # save the table contents and table row/column to the ini file
    def pb_save_clicked(self):
        # create an empty dictionary
        self.tbl_dict = {'Recipe':[], 'qty:Salt(tsp)':[], 'qty:Pepper(tsp)':[], 'qty:Paprika(tsp)':[]}
        
        # loop over the cells and add to the table
        for column in range(self.tbl.columnCount()):
            for row in range(self.tbl.rowCount()):
                itm = self.tbl.item(row, column)
                try:
                    text = itm.text()
                except AttributeError: # happens when the cell is empty
                    text = ''
                if column == 0: self.tbl_dict['Recipe'].append(text)
                if column == 1: self.tbl_dict['qty:Salt(tsp)'].append(text)
                if column == 2: self.tbl_dict['qty:Pepper(tsp)'].append(text)
                if column == 3: self.tbl_dict['qty:Paprika(tsp)'].append(text)

        
        # write values to ini file      
        self.settings.setValue('table', str(self.tbl_dict))
        self.settings.setValue('rows', self.tbl.rowCount())
        self.settings.setValue('columns', self.tbl.columnCount())
        print(f'WRITE: {self.tbl_dict}')
        
    def pb_restore_clicked(self):
        self.restore_settings()

    def closeEvent(self, event):
        self.pb_save_clicked()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()