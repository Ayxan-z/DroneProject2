import io
import sys
import folium
from PyQt6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt6.QtCore import QUrl, QEventLoop
from select_area import SelectArea
from QtPyFiles.drone import Ui_MainWindow
from folium import plugins

class Window(QtWidgets.QMainWindow, SelectArea):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # WebEngine
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QUrl("https://geojson.io/#map=2/20.0/0.0"))
        self.ui.horizontalLayout.addWidget(self.view, stretch=1)
        
        # Buttons
        self.ui.btnPullData.clicked.connect(lambda : self.pullHtml(self.coordinateData))

        # Variables
        self.coordinateData = []
        
    
        
        
        # m = folium.Map(
        #     location=[40.422998, 49.900892], zoom_start=13, width="%100", height="%100"
        # )

        # folium.Circle(
        # radius=500,
        # location=[40.422998, 49.900892],
        # color='crimson',
        # fill=False,).add_to(m)

        # minimap = plugins.MiniMap()
        # m.add_child(minimap)
        
        # folium.Marker([40.422998, 49.900892], popup='alma').add_to(m)
        # folium.CircleMarker(location=[40.422998, 49.900892], radius=1, popup="alma").add_to(m)
        
        # data = io.BytesIO()
        # m.save(data, close_file=False)
        # self.view.setHtml(data.getvalue().decode())

app = QtWidgets.QApplication(sys.argv)
wnd = Window()
wnd.show()
sys.exit(app.exec())