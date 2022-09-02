from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime

Base = declarative_base()


class IPs(Base):
    __tablename__ = "ips"
    id = Column(Integer, primary_key=True, autoincrement=True)
    resource = Column(String(20), nullable=False)
    ip = Column(String(50), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.now())
