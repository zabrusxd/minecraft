from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from panda3d.core import loadPrcFileData

from mapmanager import MapManager
from controller import Controller
from editor import Editor

# Настройка конфигурации приложения
# Заголовок окна
loadPrcFileData('', 'window-title My Minecraft')
# Отключение синхронизации
loadPrcFileData('', 'sync-video false')
# Включение отображения FPS
loadPrcFileData('', 'show-frame-rate-meter true')
# скрыть курсор мыши
loadPrcFileData('', 'cursor-hidden true')
# Установка размера окна
#loadPrcFileData('', 'win-size 1000 750')
loadPrcFileData('', 'win-size 1600 900')


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # режим редактирования
        self.edit_mode = True

        # создаём менеджер карты
        self.map_manager = MapManager()

        # создаём контроллер мышки и клавиатуры
        self.controller = Controller()

        # создаём редактор
        self.editor = Editor(self.map_manager)

        # загружаем картинку курсора
        self.pointer = OnscreenImage(image='target.png',
                                     pos=(0, 0, 0), scale=0.08)
        # устанавливаем прозрачность
        self.pointer.setTransparency(TransparencyAttrib.MAlpha)

        # имя файла для сохранения и загрузки карт
        self.file_name = "my_map.dat"

        self.accept("f1", self.basicMap)
        self.accept("f2", self.generateRandomMap)
        self.accept("f3", self.saveMap)
        self.accept("f4", self.loadMap)

        print("'f1' - создать базовую карту")
        print("'f2' - создать случайную карту")
        print("'f3' - сохранить карту")
        print("'f4' - загрузить карту")

        # зарегистрируйте на события нажатия клавиш
        # "0", "1", "2" ... "9" метод установки цвета
        # ...

        base.accept("tab", self.switchEditMode)

        # генерируем случайный уровень
        self.generateRandomMap()

    def basicMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.basicMap()
        print('Basic map generated')

    def generateRandomMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.generateRandomMap()
        print('Random map generated')

    def saveMap(self):
        self.map_manager.saveMap(self.file_name)
        print('Map saved to "'+self.file_name+'"')

    def loadMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.loadMap(self.file_name)
        print('Map loaded from "'+self.file_name+'"')

    # добавьте метод установки цвета
    # ...
        # если установлен режим редактирования
        # ...
            # вызовите метод setColor менеджера карты
            # ...

    def switchEditMode(self):
        self.edit_mode = not self.edit_mode
        self.controller.setEditMode(self.edit_mode)
        self.editor.setEditMode(self.edit_mode)

        if self.edit_mode:
            self.pointer.setImage(image='target.png')
        else:
            self.pointer.setImage(image='target1.png')
        self.pointer.setTransparency(TransparencyAttrib.MAlpha)


app = Game()
app.run()