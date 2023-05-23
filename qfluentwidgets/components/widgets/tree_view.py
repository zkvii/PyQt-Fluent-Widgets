# coding:utf-8

from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import QTreeWidget, QStyledItemDelegate, QStyle, QTreeView

from ...common.style_sheet import FluentStyleSheet, themeColor, isDarkTheme
from ...common.font import getFont
from .scroll_area import SmoothScrollDelegate


class TreeItemDelegate(QStyledItemDelegate):
    """ Tree item delegate """

    def __init__(self, parent: QTreeView):
        super().__init__(parent)

    def paint(self, painter, option, index):
        painter.setRenderHints(
            QPainter.Antialiasing | QPainter.TextAntialiasing)
        super().paint(painter, option, index)

        if not (option.state & (QStyle.State_Selected | QStyle.State_MouseOver)):
            return

        painter.save()
        painter.setPen(Qt.NoPen)

        # draw background
        h = option.rect.height() - 4
        c = 255 if isDarkTheme() else 0
        painter.setBrush(QColor(c, c, c, 9))
        painter.drawRoundedRect(
            4, option.rect.y() + 2, self.parent().width() - 8, h, 4, 4)

        # draw indicator
        if option.state & QStyle.State_Selected and self.parent().horizontalScrollBar().value() == 0:
            painter.setBrush(themeColor())
            painter.drawRoundedRect(4, 9+option.rect.y(), 3, h - 13, 1.5, 1.5)

        painter.restore()

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.font = getFont(13)
        if isDarkTheme():
            option.palette.setColor(QPalette.Text, Qt.white)
            option.palette.setColor(QPalette.HighlightedText, Qt.white)
        else:
            option.palette.setColor(QPalette.Text, Qt.black)
            option.palette.setColor(QPalette.HighlightedText, Qt.black)


class TreeViewBase:
    """ Tree view base class """

    def _initView(self):
        self.scrollDelagate = SmoothScrollDelegate(self)

        self.setItemDelegate(TreeItemDelegate(self))
        self.setIconSize(QSize(16, 16))

        FluentStyleSheet.TREE_VIEW.apply(self)

    def drawBranches(self, painter, rect, index):
        rect.moveLeft(15)
        return QTreeView.drawBranches(self, painter, rect, index)


class TreeWidget(TreeViewBase, QTreeWidget):
    """ Tree widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._initView()


class TreeView(TreeViewBase, QTreeView):
    """ Tree view """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._initView()
