#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

douban_movie = scoped_session(sessionmaker())

def config_douban_movie_session(conf, engine=None):
  if engine is None:
    engine = _create_engine(conf['MYSQL_HOSTS'],
                            conf['MYSQL_USER'],
                            conf['MYSQL_PASSWORD'],
                            conf['MYSQL_PORT'],
                            conf['MYSQL_DB'])
    douban_movie.configure(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)

def _create_engine(host, user, password, port, db):
  engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=utf8&use_unicode=1' % (
          user, password,
          host, port,
          db),
          pool_size=10,
          max_overflow=-1,
          pool_recycle=7200
      )
  return engine