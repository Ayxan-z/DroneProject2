import io
import sys
import folium
from PyQt6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt6.QtCore import QUrl, QEventLoop
from select_area import SelectArea
from QtPyFiles.drone import Ui_MainWindow
from folium import plugins
from PyQt6.QtTest import QTest
from create_map import CreateMap

class Window(QtWidgets.QMainWindow, CreateMap, SelectArea):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons
        self.ui.btnStart.clicked.connect(lambda : self.pullHtml(self.coordinateData))
        self.ui.btnConnectPage2.clicked.connect(self.connectPage2)

        # Variables
        self.coordinateData = []

        # Functions
        self.ui.prbConnectPage2.setVisible(0)

        
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