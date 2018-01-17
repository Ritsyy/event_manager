#!/usr/bin/env python

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(200))
    organizer = Column(String(40))
    venue = Column(String(200))
    registeration_fees = Column(Integer())
    start_date_time = Column(DateTime)
    end_date_time = Column(DateTime)
    # event_type_id = Column(Integer, ForeignKey('event_type.id'))


class EventType(Base):
    __tablename__ = 'event_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    # event = relationship("Event")



if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
