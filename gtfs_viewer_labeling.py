from qgis.PyQt.QtGui import QColor, QFont
from qgis.core import *

from .gtfs_viewer_settings import (
    STOPS_LABEL_FONT,
    STOPS_LABEL_SIZE,
    STOPS_LABEL_BUFFER_SIZE,
    STOPS_LABEL_BUFFER_COLOR,
    STOPS_LABEL_DIST,
    STOPS_LABEL_MINUMUM_VISIBLE_SCALE
)


def get_labeling_for_stops(target_field_name="stop_name"):
    text_format = QgsTextFormat()
    text_format.setFont(QFont(STOPS_LABEL_FONT, STOPS_LABEL_SIZE))
    text_format.setSize(STOPS_LABEL_SIZE)

    if STOPS_LABEL_BUFFER_SIZE > 0:
        buffer_settings = QgsTextBufferSettings()
        buffer_settings.setEnabled(True)
        buffer_settings.setSize(STOPS_LABEL_BUFFER_SIZE)
        buffer_settings.setColor(QColor(STOPS_LABEL_BUFFER_COLOR))
        text_format.setBuffer(buffer_settings)

    pal_layer = QgsPalLayerSettings()
    pal_layer.setFormat(text_format)
    pal_layer.fieldName = target_field_name
    pal_layer.placement = QgsPalLayerSettings.Placement.OrderedPositionsAroundPoint
    pal_layer.dist = STOPS_LABEL_DIST
    pal_layer.scaleVisibility = True
    pal_layer.minimumScale = STOPS_LABEL_MINUMUM_VISIBLE_SCALE
    pal_layer.enabled = True
    labeling = QgsVectorLayerSimpleLabeling(pal_layer)
    return labeling
