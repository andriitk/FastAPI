from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool
from models import Base, IPs

engine = create_engine("sqlite:///ips.db", poolclass=SingletonThreadPool)

Base.metadata.bind = engine
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_data(url: str, ip_add: str):
    ip = IPs(
        ip=ip_add,
        resource=url
    )
    session.add(ip)

    session.commit()
