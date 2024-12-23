from marshmallow import EXCLUDE

from automateda11y.pw.a11y.engine import Engine
from automateda11y.pw.modal.axe.issues import Issues
from automateda11y.pw.modal.params import Params
from automateda11y.pw.util.a11y import A11y


class AxeRunner:

    def __init__(self, page, params=None):
        self.a11y = A11y(page)
        self.params = Params()

    def set_page_title(self, page_title):
        self.params.set_page_title(page_title)
        return self

    def set_ignore_codes(self, ignore_codes):
        self.params.set_ignore_codes(ignore_codes)
        return self

    def execute(self):
        data = self.a11y.execute(Engine.AXE, self.params)
        return Issues.Schema().load(data, unknown=EXCLUDE)
