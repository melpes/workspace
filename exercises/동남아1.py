import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

mousepos = QPoint(0, 0)

class MyWidget(QWidget): # 그림판 인터페이스 구축

    def __init__(self):
        global mousepos

        super().__init__()
        self.color = QColor(255, 0, 0)

        # 그림 창과 하단 영역 분리
        basicbox = QVBoxLayout()
        self.setLayout(basicbox)

        up = QHBoxLayout()
        down = QHBoxLayout()

    # 하단 안내 문구, 색상 버튼, 위치 엔트리, 타원그리기 버튼 배치
        down.addStretch(1)

        # 안내 문구 설정
        self.infor = QLabel("색상을 선택하세요")
        self.infor.setStyleSheet(f"background-color : {self.color}")

        down.addWidget(self.infor)
        self.colorbt = QPushButton("색상")
        self.colorbt.clicked.connect(self.showColorDlg)
        down.addWidget(self.colorbt)

        xpos = str(mousepos.x())
        ypos = str(mousepos.y())
        xypos = QLabel(f"x : {xpos}, y : {ypos}")
        xypos.setStyleSheet("border-style :solid;" "border-width : 2px;" "background-color : #FFFFFF")
        down.addWidget(xypos)

        self.ellipsebt = QRadioButton("타원그리기", self)
        self.ellipsebt.clicked.connect(self.ellipsebtClicked)
        down.addWidget(self.ellipsebt)

        down.addStretch(1)
        
        # 레이아웃 배치
        self.drawing = MyDrawing(self) # 그림 그리는 영역
        up.addWidget(self.drawing)

        basicbox.addLayout(up)
        basicbox.addLayout(down)

        self.setGeometry(100, 100, 800, 500)


        
        self.pencolor = QColor(0,0,0)
        self.drawType = 0
        self.brushcolor = QColor(255, 255, 255)


    def showColorDlg(self):       
         
        # 색상 대화상자 생성      
        color = QColorDialog.getColor()
 
        # sender = self.sender()
 
        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if color.isValid():           
            self.pencolor = color
            self.infor.setStyleSheet('background-color: {}'.format( color.name()))
        else:
            self.brushcolor = color
            self.brushbtn.setStyleSheet('background-color: {}'.format( color.name()))

    def ellipsebtClicked(self):
        if self.ellipsebt.isChecked():
            self.drawType = 1
        else:
            self.drawType = 0

class MyDrawing(QGraphicsView):

    def __init__(self, parent):
        
        super().__init__(parent)       
        self.scene = QGraphicsScene()        
        self.setScene(self.scene)
 
        self.items = []
         
        self.start = QPointF()
        self.end = QPointF()
 
        self.setRenderHint(QPainter.HighQualityAntialiasing)

        global mousepos
        
 
    def moveEvent(self, e):
        rect = QRectF(self.rect())
        rect.adjust(0,0,-2,-2)
 
        self.scene.setSceneRect(rect)
 
    def mousePressEvent(self, e):
 
        if e.button() == Qt.LeftButton:
            # 시작점 저장
            self.start = e.pos()
            self.end = e.pos()        
            mousepos = e.pos()
 
    def mouseMoveEvent(self, e):  
         
        # e.buttons()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴 
        if e.buttons() & Qt.LeftButton:           
 
            self.end = e.pos()
 
            pen = QPen(self.parent().pencolor, 1)
 
            # 곡선 그리기
            if self.parent().drawType == 0:
 
                # Path 이용
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
 
                # Line 이용
                #line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                #self.scene.addLine(line, pen)
                 
                # 시작점을 다시 기존 끝점으로
                self.start = e.pos()

            # 원 그리기
            if self.parent().drawType == 1:
                brush = QBrush(self.parent().brushcolor)
 
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])
 
 
                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addEllipse(rect, pen, brush))

            
            mousepos = e.pos()
 
 
    def mouseReleaseEvent(self, e):        
 
        if e.button() == Qt.LeftButton:
 
        
 
            pen = QPen(self.parent().pencolor, 1)
 
            if self.parent().drawType == 0:
 
                self.items.clear()
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                 
                self.scene.addLine(line, pen)
 
            if self.parent().drawType == 2:
 
                brush = QBrush(self.parent().brushcolor)
 
                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addRect(rect, pen, brush)
 
            if self.parent().drawType == 3:
 
                brush = QBrush(self.parent().brushcolor)
 
                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addEllipse(rect, pen, brush)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())