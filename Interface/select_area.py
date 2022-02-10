from PyQt6.QtTest import QTest


class SelectArea():
    def pullData(self, data):
        self.l.append(data)

    def pullHtml(self, coordinateData):
        self.l = coordinateData
        i = 0
        while 1:
            self.view.page().runJavaScript(f"document.getElementsByClassName('cm-number')[{i}].innerHTML", self.pullData)
            QTest.qWait(100)
            if not self.l[i]:
                self.l.pop()
                break
            i += 1
        
        if i % 2 != 0: self.l.pop(0)
