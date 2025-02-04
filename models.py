from database import Base

class CleanedData(Base):
    __tablename__ = "cleaned_data"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    cleaned_date = Column(DateTime)
