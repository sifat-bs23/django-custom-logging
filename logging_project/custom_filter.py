import logging
from logging import Filter, LogRecord
from .global_request_middlewear import get_request
from .utils import getattrd

local_thread = get_request()
logger = logging.getLogger(__name__)


class CustomFilter(Filter):
    def __init__(self, capture_list=None, *args, **kwargs):
        super().__init__()
        if not isinstance(capture_list, (list, tuple)):
            pass
        self.capture_list = capture_list

    def filter(self, record: LogRecord) -> bool:
        for capture_in, capture_out in self.capture_list:
            setattr(
                record, capture_out, getattrd(local_thread, capture_in, None) or "-"
            )

        return True