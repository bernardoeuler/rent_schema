from core.services.sample_service import SampleService

class MainController:
  def __init__(self):
    self.service = SampleService()

  def test_connection(self):
    return self.service.check_database()