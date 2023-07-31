from . import db
from sqlalchemy.sql import func

class ControlPointsData(db.Model):
    __tablename__ = 'control_points_data'

    sno = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    point_id = db.Column(db.String(10))
    arch1960_eastings = db.Column(db.Float)
    arch1960_northings = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    heights = db.Column(db.Float)
    monument_status = db.Column(db.String(20))
    usage = db.Column(db.String(20))
    image_description = db.Column(db.String(255))
    satellite_image = db.Column(db.String(255))
    wgs84_eastings = db.Column(db.Float)
    wgs84_northings = db.Column(db.Float)


    def __init__(self, point_id, arch1960_eastings, arch1960_northings, latitude, longitude, heights, monument_status, usage, image_description, satellite_image, wgs84_eastings, wgs84_northings):
        self.point_id = point_id
        self.arch1960_eastings = arch1960_eastings
        self.arch1960_northings = arch1960_northings
        self.latitude = latitude
        self.longitude = longitude
        self.heights = heights
        self.monument_status = monument_status
        self.usage = usage
        self.image_description = image_description
        self.satellite_image = satellite_image
        self.wgs84_eastings = wgs84_eastings
        self.wgs84_northings = wgs84_northings