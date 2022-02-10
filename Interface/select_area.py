from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QMessageBox


class SelectArea:
    def __pullData(self, data):
        self.l.append(data)

    def pullHtml(self, coordinateData):
        coordinateData.clear()
        self.l = coordinateData
        
        i = 0
        while 1:
            self.map.page().runJavaScript(f"document.getElementsByClassName('cm-number')[{i}].innerHTML", self.__pullData)

            QTest.qWait(150)            
            try:
                if not self.l[-1]:
                    self.l.pop()
                    break
            
            except IndexError:
                QMessageBox.warning(self, 'Xəta', f'<font size = 4>Xəta yarandı, yenidən başladın!</font>')
            
            i += 1
        
        if i % 2 != 0: self.l.pop(0)
        
        try:
            if self.coordinateData[0] != self.coordinateData[-2]:
                QMessageBox.warning(self, 'Xəta', f'<font size = 4>Məlumat alınanmadı!</font>')
        
        except IndexError:
            QMessageBox.warning(self, 'Xəta', f'<font size = 4>Sahə seçilməyib!</font>')
        
        print(self.coordinateData)
