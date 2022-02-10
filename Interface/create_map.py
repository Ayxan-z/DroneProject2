from PyQt6 import QtWebEngineWidgets
from PyQt6.QtCore import QUrl


class CreateMap:
    def connectPage2(self):
        self.ui.btnConnectPage2.setEnabled(False)
        self.ui.prbConnectPage2.setVisible(1)
        self.map = QtWebEngineWidgets.QWebEngineView()
        self.map.load(QUrl("https://geojson.io/#map=2/20.0/0.0"))
        self.ui.horizontalLayout.addWidget(self.map, stretch=1)
        self.map.loadFinished.connect(self.__onLoadFinished)
        self.map.loadProgress.connect(self.ui.prbConnectPage2.setValue)
    
    def __onLoadFinished(self, ok):
        if ok:
            self.map.page().runJavaScript(
                """
                function remove_by_class_name(_className){
                    var elem = document.getElementsByClassName(_className)[0];
                    elem.parentNode.removeChild(elem);
                }
                remove_by_class_name("file-bar");
                remove_by_class_name("leaflet-draw-draw-polyline");
                remove_by_class_name("leaflet-draw-draw-marker");
                remove_by_class_name("top");
                remove_by_class_name("leaflet-control-attribution");
            """)
            self.ui.stackedWidget.setCurrentIndex(1)