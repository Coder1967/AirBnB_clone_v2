#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
import models
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        def cities(self):
            var = models.storage.all()
            new_list = []
            result = []
            for key in var:
                if ('City' in city):
                    new_list.append(var[key])
            for elem in new_list:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)
