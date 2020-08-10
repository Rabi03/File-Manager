from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os, subprocess
from Style import style
import shutil

from PyQt5.uic import loadUiType
ui, _ = loadUiType("file.ui")

class FileManager(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.HandleUiChange()
        self.Handle_Buttons()
        self.tabWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabWidget.customContextMenuRequested.connect(self.contextMenu)
        
        self.s = []
        self.list = ["Open",
        'Cut',
        'Copy',
        'Delete',]
        self.dict={"New": ["Folder", "Text Document"]}
        self.tabWidget.currentChanged.connect(self.ChangeStyle)
        self.isCutEnable=False
        self.s.append('Quick Acess')
        self.style1='''
        text-align:left;
        color:white;
        background-color:rgb(118, 118, 118);
        border:0px;
        border-radius:10px
        '''
        self.style2='''
        text-align:left;
        color:white;
        border:0px;
        border-radius:10px
        '''
    
    def HandleUiChange(self):
        self.HideThemes()
        self.close_btn.setGeometry(1180,0,51,41)
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.tabWidget.tabsClosable()
        self.buttons = [self.home_btn,self.quick_btn,self.net_btn,self.settings_btn,self.recycle_btn,self.theme_btn]
        
    
    def ChangeStyle(self,index):
        t = self.tabWidget.tabText(index)
        for i in self.buttons:
            if t in i.text():
                i.setStyleSheet(self.style1)
                self.head_btn.setText(i.text())
                self.head_btn.setIcon(i.icon())
            else:i.setStyleSheet(self.style2)
        

    
    def CreateTabs(self):
        # self.ChangeStyle(self.sender())
        obj = self.sender().objectName()
        tab = QWidget()
        text = self.sender().text()
        icon = self.sender().icon()
        if not text:
            if "desktop" in obj: text = "Desktop"
            elif "obj" in obj: text = "3D Objects"
            elif "documents" in obj: text = "Documents"
            elif "downloads" in obj: text = "Downloads"
            elif "music" in obj: text = "Music"
            elif "video" in obj: text = "Video"
            elif "picture" in obj:text="Picture"


        
        if text in self.s:
            self.tabWidget.setCurrentIndex(self.s.index(text))
        else:
            self.s.append(text)
            self.head_btn.setText(text)
            self.head_btn.setIcon(icon)
            self.newTab = self.tabWidget.addTab(tab, text)
            self.tabWidget.setTabIcon(self.newTab, icon)
            self.tabWidget.tabCloseRequested.connect(self.CloseTabs)
            # self.tabWidget.currentChanged.connect(self.CurrentTab)
            self.tabWidget.setCurrentIndex(self.newTab)
            self.GenerateFiles(self.newTab, text)
    
    def openCurrentDirectory(self, path):
        layout = self.Opendirectory(path)
        self.tabWidget.widget(self.tabWidget.currentIndex()).setLayout(layout)
    
    def CreateList_Model(self, text, path):
        if text == "Home":
            self.home_list = QTableView()
            self.home_model = QFileSystemModel()
            self.home_model.setRootPath(path)
            return [self.home_list,self.home_model]
        elif text == "Recycle Bin":
            self.recycle_list=QTableView()
            self.recycle_model = QFileSystemModel()
            self.recycle_model.setRootPath(path)
            return [self.recycle_list,self.recycle_model]
        elif text == "Network":
            self.net_list=QTableView()
            self.net_model = QFileSystemModel()
            self.net_model.setRootPath(path)
            return [self.net_list,self.net_model]
        elif text == "3D Objects":
            self.obj_list=QTableView()
            self.obj_model = QFileSystemModel()
            self.obj_model.setRootPath(path)
            return [self.obj_list,self.obj_model]
        elif text == "Desktop":
            self.desktop_list=QTableView()
            self.desktop_model = QFileSystemModel()
            self.desktop_model.setRootPath(path)
            return [self.desktop_list,self.desktop_model]
        elif text == "Downloads":
            self.download_list=QTableView()
            self.download_model = QFileSystemModel()
            self.download_model.setRootPath(path)
            return [self.download_list,self.download_model]
        elif text == "Documents":
            self.document_list=QTableView()
            self.document_model = QFileSystemModel()
            self.document_model.setRootPath(path)
            return [self.document_list,self.document_model]
        elif text == "Music":
            self.music_list=QTableView()
            self.music_model = QFileSystemModel()
            self.music_model.setRootPath(path)
            return [self.music_list,self.music_model]
        elif text == "Picture":
            self.picture_list=QTableView()
            self.picture_model = QFileSystemModel()
            self.picture_model.setRootPath(path)
            return [self.picture_list,self.picture_model]
        elif text == "Video":
            self.video_list=QTableView()
            self.video_model = QFileSystemModel()
            self.video_model.setRootPath(path)
            return [self.video_list,self.video_model]
        

    
    def Opendirectory(self, path, text):
        ls, ml = self.CreateList_Model(text, path)
        ls.verticalHeader().setVisible(False)
        ls.setStyleSheet(style)
        ls.horizontalHeader().setStyleSheet('color:#8c8c8c')
        ls.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        ls.setModel(ml)
        ls.setRootIndex(ml.index(path))
        ls.clicked.connect(self.onClicked)
        
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(ls)
        layout.setContentsMargins(30, 30, 100, 60)

        return layout
    

    def GenerateFiles(self,index, text):
        if text == "Home":
            dir_path = "This Pc path"
            self.home=["This Pc path"]
        elif text == "Recycle Bin":
            dir_path = "C:\Windows\Temp"
            self.recycle = ["C:\Windows\Temp"]
        elif text == "Network":
            dir_path = "F:\Robo 3T"
            self.net = [dir_path]
        elif text == "3D Objects":
            dir_path = "C:/Users/Asus/3D Objects"
            self.obj = [dir_path]
        elif text == "Desktop":
            dir_path = "C:/Users/Asus/Desktop"
            self.desktop = [dir_path]
        elif text == "Downloads":
            dir_path = "C:/Users/Asus/Downloads"
            self.downloads = [dir_path]
        elif text == "Picture":
            dir_path = "C:/Users/Asus/Pictures"
            self.picture = [dir_path]
        elif text == "Music":
            dir_path = "C:/Users/Asus/Music"
            self.music = [dir_path]
        elif text == "Video":
            dir_path = "C:/Users/Asus/Videos"
            self.video = [dir_path]
        elif text == "Documents":
            dir_path = "C:/Users/Asus/Documents"
            self.document = [dir_path]



        layout = self.Opendirectory(dir_path,text)

        self.tabWidget.widget(self.newTab).setLayout(layout)
        
    
    def onClicked(self, index):
        path = self.sender().model().filePath(index)
        if os.path.isdir(path):
            path = os.path.realpath(path)
            self.curr_Text = self.tabWidget.tabText(self.tabWidget.currentIndex())
            tabindex=self.tabWidget.currentIndex()
            if self.curr_Text == "Home":
                self.home.append(path)
                self.home_model.setRootPath(path)
                self.home_list.setRootIndex(self.home_model.index(path))
            elif self.curr_Text == "Network":
                self.net.append(path)
                self.net_model.setRootPath(path)
                self.net_list.setRootIndex(self.net_model.index(path))
            elif self.curr_Text == "Recycle Bin":
                self.recycle.append(path)
                self.recycle_model.setRootPath(path)
                self.recycle_list.setRootIndex(self.recycle_model.index(path))
            elif self.curr_Text == "3D Objects":
                self.obj.append(path)
                self.obj_model.setRootPath(path)
                self.obj_list.setRootIndex(self.obj_model.index(path))
            elif self.curr_Text == "Desktop":
                self.desktop.append(path)
                self.desktop_model.setRootPath(path)
                self.desktop_list.setRootIndex(self.desktop_model.index(path))
            elif self.curr_Text == "Downloads":
                self.curr_model = self.download_model
                self.curr_list=self.download_list
                self.download.append(path)
                self.download_model.setRootPath(path)
                self.download_list.setRootIndex(self.download_model.index(path))
            elif self.curr_Text == "Documents":
                self.document.append(path)
                self.document_model.setRootPath(path)
                self.document_list.setRootIndex(self.document_model.index(path))
            elif self.curr_Text == "Music":
                self.music.append(path)
                self.music_model.setRootPath(path)
                self.music_list.setRootIndex(self.music_model.index(path))
            elif self.curr_Text == "Picture":
                self.picture.append(path)
                self.picture_model.setRootPath(path)
                self.picture_list.setRootIndex(self.picture_model.index(path))
            elif self.curr_Text == "Video":
                self.video.append(path)
                self.video_model.setRootPath(path)
                self.video_list.setRootIndex(self.video_model.index(path))
        else:
            os.startfile(path)
    

    def contextMenu(self):
        self.menu = QMenu()
        self.menu.setStyleSheet(style)
        self.cursor = QCursor()
        self.list.append(self.dict)
        self.newMenu(self.list,self.menu)
        self.menu.exec_(self.cursor.pos())
    
    def newMenu(self, data, menu):
        if isinstance(data, dict):
            for k, v in data.items():
                subMenu = QMenu(k, menu)
                menu.addMenu(subMenu)
                self.newMenu(v, subMenu)
        elif isinstance(data, list):
            for element in data:
                self.newMenu(element, menu)
        else:
            if data == "Folder": 
                action = menu.addAction(QIcon("./Icons/folder.png"),data)
                action.triggered.connect(self.openFile)
            elif (data=="Text Document"):
                action = menu.addAction(QIcon("./Icons/text.png"), data)
                action.triggered.connect(self.openFile)
            else:
                action = menu.addAction(data)
                action.triggered.connect(self.openFile)

            
    
    def CopyFile(self,file):
        self.filecopy = file
        _, self.filename = os.path.split(file)
        self.list = [sub.replace("Copy", "Paste") for sub in self.list if isinstance(sub,str)]
        
        

    def CutFile(self,path):
        self.CopyFile(path)
        self.isCutEnable = True
    

    def Paste(self, path):
        new=os.path.join(path[-1],"file.txt")
        shutil.copyfile(self.filecopy, new)
        real=os.path.join(path[-1],self.filename)
        os.rename(new, real)
            
        if self.isCutEnable: os.remove(self.filecopy); self.isCutEnable = False
        self.list = [sub.replace("Paste", "Copy") for sub in self.list if isinstance(sub,str)]
        
        
    
    def openFile(self):
        text = self.tabWidget.tabText(self.tabWidget.currentIndex())
        curr_list,lists,model=None,None,None
        if "Home" in text:
            curr_list=self.home
            lists = self.home_list
            model = self.home_model
        if "Recycle" in text:
            curr_list=self.recycle
            lists = self.recycle_list
            model = self.recycle_model
        if "Network" in text:
            curr_list=self.net
            lists = self.net_list
            model = self.net_model
        if "3D" in text:
            curr_list=self.obj
            lists = self.obj_list
            model = self.obj_model
        if "Desktop" in text:
            curr_list=self.desktop
            lists = self.desktop_list
            model = self.desktop_model
        if "Documents" in text:
            curr_list=self.document
            lists = self.document_list
            model = self.document_model
        if "Download" in text:
            curr_list=self.download
            lists = self.download_list
            model = self.download_model
        if "Music" in text:
            curr_list=self.music
            lists = self.music_list
            model = self.music_model
        if "Picture" in text:
            curr_list=self.picture
            lists = self.picture_list
            model = self.picture_model
        if "Video" in text:
            curr_list=self.video
            lists = self.video_list
            model = self.video_model
        index=lists.currentIndex()
        filepath = model.filePath(index)
        text = self.sender().text()
        if(text=="Open"):
            if os.path.isfile(filepath):
                os.startfile(filepath)
        elif text == "Folder":
            folderName,done1=QInputDialog.getText(self,"New Folder in "+filepath,"Enter Folder Name")
            newPath=os.path.join(filepath,folderName)
            if done1 and not os.path.exists(newPath):
                os.makedirs(newPath)
            else:
                QMessageBox.critical(self, "Error", "Folder is exists.Please Give another name")
        elif text == "Text Document":
            fileName, done = QInputDialog.getText(self, "New File", "Enter File Name")
            if done:
                with open(os.path.join(filepath, fileName), 'w') as fp:
                    pass
        elif text == "Delete":
            if os.path.isdir(filepath):
                os.rmdir(filepath)
            elif os.path.isfile(filepath): os.remove(filepath)
        elif text == "Copy":
            self.CopyFile(filepath)
        elif text == "Paste":
            self.Paste(curr_list)
        elif text == "Cut":
            self.CutFile(filepath)
        
    
    def CloseTabs(self,index):
        tab = self.tabWidget.widget(index)
        t = self.tabWidget.tabText(index)
        tab.deleteLater()
        img = self.tabWidget.tabIcon(index-1)
        if t in self.s: self.s.remove(t)
        if index==self.tabWidget.currentIndex():
            self.head_btn.setText(self.s[-1])
            self.head_btn.setIcon(img)
    

    def Handle_Buttons(self):
        self.theme_btn.clicked.connect(self.ShowThemes)
        self.hide_btn.clicked.connect(self.HideThemes)
        self.quick_btn.clicked.connect(self.CreateTabs)
        self.home_btn.clicked.connect(self.CreateTabs)
        self.net_btn.clicked.connect(self.CreateTabs)
        self.recycle_btn.clicked.connect(self.CreateTabs)
        self.settings_btn.clicked.connect(self.OpenSettings)
        self.obj_btn.clicked.connect(self.CreateTabs)
        self.desktop_btn.clicked.connect(self.CreateTabs)
        self.documents_btn.clicked.connect(self.CreateTabs)
        self.downloads_btn.clicked.connect(self.CreateTabs)
        self.music_btn.clicked.connect(self.CreateTabs)
        self.picture_btn.clicked.connect(self.CreateTabs)
        self.video_btn.clicked.connect(self.CreateTabs)
        self.left_btn.clicked.connect(self.GotoBack)
        self.right_btn.clicked.connect(self.GotoFront)
        self.close_btn.clicked.connect(self.CloseWindow)
        self.th_1.clicked.connect(self.DarkOrengeTheme)
        self.th_2.clicked.connect(self.DarkBlueTheme)
        self.th_3.clicked.connect(self.QDark)
        self.th_4.clicked.connect(self.ManjaroMix)
        self.th_5.clicked.connect(self.DefaultTheme)
        self.minimize_btn.clicked.connect(self.minimize)
        self.large_btn.clicked.connect(self.large)
    
    def large(self):
        if self.isMaximized():
            self.showNormal()
            self.large_btn.setIcon(QIcon('Icons/large.png'))
            self.close_btn.move(1180,0)
            self.minimize_btn.move(1060,0)
            self.large_btn.move(1120,0)
            self.groupBox.move(840,0)
            self.tabWidget.resize(1031,761)
            self.picture_btn.move(70, 240)
            self.video_btn.move(222,240)
        else:
            self.showMaximized()
            self.close_btn.move(1850,0)
            self.minimize_btn.move(1710,0)
            self.large_btn.move(1780,0)
            self.groupBox.move(1500,0)
            self.tabWidget.resize(1701, 1011)
            self.picture_btn.move(830, 50)
            self.video_btn.move(990,50)
            self.large_btn.setIcon(QIcon('Icons/mini.png'))

    def minimize(self):
        self.showMinimized()

    def ShowThemes(self,event):
        self.groupBox.show()

    def HideThemes(self):
        self.groupBox.hide()
    
    def CloseWindow(self):
        app.quit()
    
    def OpenSettings(self):
        subprocess.Popen([r"C:\Windows\System32\DpiScaling.exe"])
    
    def GotoBack(self):
        Text = self.tabWidget.tabText(self.tabWidget.currentIndex())
        
        if Text == "Home" and len(self.home)>1:
            self.setNewRoot(self.home,self.home_list,self.home_model)
        elif Text == "Network" and len(self.net)>1:
            self.setNewRoot(self.net,self.net_list,self.net_model)
        elif Text == "Recycle Bin" and len(self.recycle)>1:
            self.setNewRoot(self.recycle, self.recycle_list, self.recycle_model)
        elif Text == "3D Objects" and len(self.obj) > 1:
            self.setNewRoot(self.obj, self.obj_list, self.obj_model)
        elif Text == "Desktop" and len(self.desktop)>1:
            self.setNewRoot(self.desktop, self.desktop_list, self.desktop_model)
        elif Text == "Downloads" and len(self.download)>1:
            self.setNewRoot(self.download, self.download_list, self.download_model)
        elif Text == "Music" and len(self.music)>1:
            self.setNewRoot(self.music, self.music_list, self.music_model)
        elif Text == "Picture" and len(self.picture)>1:
            self.setNewRoot(self.picture, self.picture_list, self.picture_model)
        elif Text == "Video" and len(self.video)>1:
            self.setNewRoot(self.video, self.video_list, self.video_model)
        elif Text == "Documents" and len(self.document)>1:
            self.setNewRoot(self.document,self.document_list,self.document_model)
    
    def setNewRoot(self,stack, ls, model):
        self.old=stack.pop()
        model.setRootPath(stack[-1])
        ls.setRootIndex(model.index(stack[-1]))
    
    def GoPrevRoot(self, stack, ls, model):
        model.setRootPath(stack[-1])
        ls.setRootIndex(model.index(stack[-1]))
    
    def GotoFront(self):
        Text=self.tabWidget.tabText(self.tabWidget.currentIndex())
        if Text == "Home":
            self.home.append(self.old)
            self.GoPrevRoot(self.home,self.home_list,self.home_model)
        elif Text == 'Network':
            self.net.append(self.old)
            self.GoPrevRoot(self.net, self.net_list, self.net_model)
        elif Text == "Recycle Bin" and len(self.recycle) > 1:
            self.recycle.append(self.old)
            self.GoPrevRoot(self.recycle, self.recycle_list, self.recycle_model)
        elif Text == "3D Objects" and len(self.obj) > 1:
            self.obj.append(self.old)
            self.GoPrevRoot(self.obj, self.obj_list, self.obj_model)
        elif Text == "Desktop" and len(self.desktop) > 1:
            self.desktop.append(self.old)
            self.GoPrevRoot(self.desktop, self.desktop_list, self.desktop_model)
        elif Text == "Downloads" and len(self.download) > 1:
            self.download.append(self.old)
            self.GoPrevRoot(self.download, self.download_list, self.download_model)
        elif Text == "Music" and len(self.music) > 1:
            self.music.append(self.old)
            self.GoPrevRoot(self.music, self.music_list, self.music_model)
        elif Text == "Picture" and len(self.picture) > 1:
            self.picture.append(self.old)
            self.GoPrevRoot(self.picture, self.picture_list, self.picture_model)
        elif Text == "Video" and len(self.video) > 1:
            self.video.append(self.old)
            self.GoPrevRoot(self.video, self.video_list, self.video_model)
        elif Text == "Documents" and len(self.document) > 1:
            self.document.append(self.old)
            self.GoPrevRoot(self.document, self.document_list, self.document_model)

    def DarkBlueTheme(self):
        style = open("themes/darkblue.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    def DarkOrengeTheme(self):
        style = open("themes/darkorenge.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    def QDark(self):
        style = open("themes/qdark.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    def ManjaroMix(self):
        style = open("themes/ManjaroMix.css", 'r')
        style = style.read()
        self.setStyleSheet(style)
    def DefaultTheme(self):
        self.setStyleSheet(style)
        
        







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.setStyleSheet(style)
    window.show()
    app.exec_()
    
