# best pdf2txt in python
#
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io


def pdf2txt(filename):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(filename, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

        # close open handles
        converter.close()
        fake_file_handle.close()
        return text


filename='rsd8-pdf/Jun Canham Organisation Failure in UK healthcare.pdf'
text=pdf2txt(filename)
print(text)
