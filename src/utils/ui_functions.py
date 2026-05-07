from PySide6.QtCore import QEvent, Qt, QTimer


class UIFunctions:
    GLOBAL_STATE = False

    @staticmethod
    def uiDefinitions(self):
        # 1. 关闭按钮
        self.close_button.clicked.connect(lambda: self.close())

        # 2. 最小化按钮
        self.min_sf.clicked.connect(lambda: self.showMinimized())

        # 3. 最大化按钮
        self.max_sf.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # 4. 窗口拖动逻辑 (使用 Event Filter 确保捕获所有子控件的点击)

        def moveWindow(event):
            if UIFunctions.GLOBAL_STATE:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                if hasattr(self, "dragPos"):
                    self.move(
                        self.pos() + event.globalPosition().toPoint() - self.dragPos
                    )
                    self.dragPos = event.globalPosition().toPoint()
                event.accept()

        if hasattr(self, "dragPos"):

            def topMousePress(event):
                self.dragPos = event.globalPosition().toPoint()

            def dobleClickMaximizeRestore(event):
                if event.type() == QEvent.MouseButtonDblClick:
                    QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

            self.top.mousePressEvent = topMousePress
            self.mouseMoveEvent = moveWindow
            self.top.mouseDoubleClickEvent = dobleClickMaximizeRestore

    @staticmethod
    def maximize_restore(self):
        status = UIFunctions.GLOBAL_STATE
        if not status:
            UIFunctions.GLOBAL_STATE = True
            self.showMaximized()
        else:
            UIFunctions.GLOBAL_STATE = False
            self.showNormal()
