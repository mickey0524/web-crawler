#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Movie(Base):

  # 表的名字:
  __tablename__ = 'movie'

  # 表的结构:
  movie_title = Column(String(20), primary_key=True)
  movie_pic = Column(String(100))
  movie_info = Column(String(60))
  movie_score = Column(String(10))
