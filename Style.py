
style = ('''
QTableView::item{
    border:0px;
}

QPushButton#home_btn::hover,
#recycle_btn::hover,
#net_btn::hover{
    background-color: rgb(160, 160, 160);;
    border:0px
}
QPushButton#settings_btn::hover,
#theme_btn::hover,
#quick_btn::hover{
    background-color: rgb(160, 160, 160);;
    border:0px
}
QPushButton#close_btn::hover{
    background-color : red;
    border:1px;
}
QPushButton#large_btn::hover{
    background-color : yellow;
    border:0px;
}
QPushButton#minimize_btn::hover{
    background-color : green;
    border:0px;
}
QMenu{
    background-color:black;
    color:white;
}
QMenu::item {
    font-size:25px;
    padding: 2px 130px 10px 10px ;
}
QMenu::item:selected{
    color:black;
    background-color:white;
}




QMainWindow{
    background-color: rgb(111, 149, 182);
}

''')