__authors__ = 'Zia-Ur-Rehman, Kishwar, Azmat Ali, and Adnan Niazi'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from my_gui import Ui_MainWindow

class MyMainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)

        # define a scene
        self.scene = QGraphicsScene()

        # signals and slots
        self.pic_index = 0
        self.actionLoad.triggered.connect(self.load_pictures)
        self.toolButton_next.clicked.connect(self.show_next_picture)
        self.toolButton_previous.clicked.connect(self.show_previous_picture)
        self.toolButton_rotateCW.clicked.connect(self.rotate_CW)
        self.toolButton_rotateCCW.clicked.connect(self.rotate_CCW)
        self.horizontalSlider_zoom.sliderMoved.connect(self.zoom_in_or_out)
        self.toolButton_zoom_in.clicked.connect(self.zoom_in)
        self.toolButton_zoom_out.clicked.connect(self.zoom_out)
        self.toolButton_fit_in_view.clicked.connect(self.fit_in_view)
        self.listWidget.itemClicked.connect(self.display_picture_clicked_in_list)

        self.actionExit.triggered.connect(self.exit)
        self.actionFile_explorer.triggered.connect(self.toggle_file_explorer)
        self.actionFile_explorer.setText('Hide file explorer')
        self.dockWidget.visibilityChanged.connect(self.dockWidget_closed)

        # initialize the zoom slider
        self.min_value = 100
        self.max_value = 2100
        self.center_value = (self.min_value + self.max_value)/2
        self.horizontalSlider_zoom.setMinimum(self.min_value)
        self.horizontalSlider_zoom.setMaximum(self.max_value)
        self.horizontalSlider_zoom.setValue(self.center_value)
        self.horizontalSlider_zoom.setEnabled(False) # disable slide unless a picture has been uploaded

    def load_pictures(self):
        """Presents a dialog box to select pictures and then displays the first picture."""

        self.file_names = QFileDialog.getOpenFileNames(self, None, '',
                                                       "Image files (*.png *.bmp *.jpeg *.tiff *.jpg *.gif *.svg);;"
                                                       "All files(*)")
        if self.file_names == []:
            # if user hasn't chosen a picture, then don't do anything
            return

        self.populate_pictures_list()
        self.display_picture(index=0)
        self.listWidget.setCurrentRow(0)
        self.horizontalSlider_zoom.setEnabled(True)

    def populate_pictures_list(self):
        """Populates the names of selected pictures in the list widget in file explorer."""

        for i in range(0,len(self.file_names)):
            file_name_object = QFileInfo(self.file_names[i])    # make a file object
            file_name = file_name_object.fileName()             # extract file name
            self.listWidget.addItem(file_name)

    def display_picture(self, index=0):
        """Displays a picture inside the QGraphics scence."""

        self.scene.clear()                                       # clear graphics scene

        self.pix_map = QPixmap(self.file_names[index])           # make pixel map of the picture

        # important for centering the picture within the scene
        self.scene.setSceneRect(0, 0, self.pix_map.width(), self.pix_map.height())

        self.scene.addPixmap(self.pix_map)                       # assign picture to the scene
        self.graphicsView.setScene(self.scene)                   # assign scene to a view
        self.graphicsView.show()                                 # show the scene

        # fits the picture within the scene
        self.rect = self.graphicsView.sceneRect()
        self.graphicsView.fitInView(self.rect, Qt.KeepAspectRatio)

        # bring the zoom slider in the middle
        self.horizontalSlider_zoom.setValue(self.center_value)

    def show_next_picture(self):
        """Displays the next picture in queue when the user presses the
        next button."""

        if self.pic_index < len(self.file_names)-1:
            self.pic_index += 1
            self.listWidget.setCurrentRow(self.pic_index)

        self.display_picture(index=self.pic_index)

    def show_previous_picture(self):
        """Displays the previous picture in queue when the user presses the
        next button."""

        if self.pic_index > 0:
            self.pic_index -= 1
            self.listWidget.setCurrentRow(self.pic_index)

        self.display_picture(index=self.pic_index)

    def rotate_CW(self):
        """Rotate the picture Clockwise by 90 degrees."""

        self.graphicsView.rotate(90)

    def rotate_CCW(self):
        """Rotate the picture Counter-Clockwise by 90 degrees."""

        self.graphicsView.rotate(-90)

    def zoom_in_or_out(self):
        """Scales the picture by a scaling factor."""

        scale_factor = self.horizontalSlider_zoom.value()/self.center_value
        newWidth = self.pix_map.width() * scale_factor
        newHeight = self.pix_map.height() * scale_factor
        scaledPixmap = self.pix_map.scaled(newWidth, newHeight)
        self.scene.clear()
        self.scene.setSceneRect(0, 0, newWidth, newHeight)
        self.scene.addPixmap(scaledPixmap)
        self.graphicsView.setScene(self.scene)                   # assign scene to a view
        self.graphicsView.show()

    def zoom_in(self):
        """Zooms in by a fixed factor when the user presses the zoom-in button. In total,
         20 button presses can be done after which no more zooming-in is possible."""

        current_slider_value = self.horizontalSlider_zoom.value()
        new_slider_value = current_slider_value + (self.max_value - self.center_value)/20
        self.horizontalSlider_zoom.setValue(new_slider_value)
        self.zoom_in_or_out()

    def zoom_out(self):
        """Zooms out by a fixed factor when the user presses the zoom-out button. In total,
         20 button presses can be done after which no more zooming-out is possible."""

        current_slider_value = self.horizontalSlider_zoom.value()
        new_slider_value = current_slider_value - (self.max_value - self.center_value)/20
        self.horizontalSlider_zoom.setValue(new_slider_value)
        self.zoom_in_or_out()

    def fit_in_view(self):
        """When the user press Fit in View button, this code
        stretches the picture in the available scene rectangle. We
        already have a function available that do this so we
        just call it"""

        self.display_picture_clicked_in_list()


    def display_picture_clicked_in_list(self):
        """Displays the picture that the user had clicked in the
        pictures list in file explorer."""

        current_pic_index = self.listWidget.currentRow()
        self.display_picture(index=current_pic_index)
        self.pic_index = current_pic_index

    def toggle_file_explorer(self):
        """Controls the visibility of dock widget. Also adds Show/Hide
        to 'File explorer' text in the menu depending on whether it is
        currently visible or invisible."""

        if self.dockWidget.isVisible() == True:
            self.dockWidget.setVisible(False)
            self.actionFile_explorer.setText('Show file explorer')
        else:
            self.dockWidget.setVisible(True)
            self.actionFile_explorer.setText('Hide file explorer')

    def dockWidget_closed(self):
        """Responds to the close event on dockWidget and updates the
        File explorer text in the menu. It is just a hack
        because the dockWidget.destroyed signal wasn't working."""

        if self.dockWidget.isVisible() == True:
            self.actionFile_explorer.setText('Hide file explorer')
        else:
            self.actionFile_explorer.setText('Show file explorer')

    def exit(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())