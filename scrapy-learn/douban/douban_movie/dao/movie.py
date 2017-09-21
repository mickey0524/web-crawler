#!/usr/bin/env python
# -*- coding: utf-8 -*-

from douban_movie.dao import session
from douban_movie.dao.config import MYSQL_CONF
from douban_movie.models.movie import Movie

session.config_game_write_session(MYSQL_CONF)

def insert_movie(movie):
  """
  type movie dict 存数据库movie的信息
  """
  new_movie = Movie(
    movie_title = movie['movie_title'],
    movie_pic = movie['movie_pic'],
    movie_info = movie['movie_info'],
    movie_score = movie['movie_score']
  )
  session.douban_movie.add(new_movie)
  session.douban_movie.commit()

