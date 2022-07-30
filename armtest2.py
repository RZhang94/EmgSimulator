class Win_setup(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('设置画图参数')
        self.canvasConfig = 0
        self.createWidget()

    def createWidget(self):
        lineWidthFrame = Frame(self)
        lineWidthFrame.pack()
        label_lineWidth = Label(lineWidthFrame, text='线条粗细')
        label_lineWidth.pack(side='left')
        self.lineWidth = IntVar()
        self.lineWidth.set(1)
        self.line_spinBox = Spinbox(lineWidthFrame, from_=1, to=10, textvariable=self.lineWidth)
        self.line_spinBox.pack(side='left')

        self.btnok = Button(self, text='确定', command=self.returnSetup)
        self.btnok.pack()

        btnCancel = Button(self, text='取消', command=self.cancelSetup)
        btnCancel.pack()

    def returnSetup(self):
        self.canvasConfig = self.lineWidth.get()
        self.destroy()

    def cancelSetup(self):
        self.destroy()

