#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models import place_amenity

class Amenity(BaseModel, Base):
    """
    the amenities available
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", back_populates='amenities',
                                   secondary=place_amenity)
