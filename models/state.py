#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            """Gets a list of City instances with state_id equal to the current State.id."""
            cities = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
