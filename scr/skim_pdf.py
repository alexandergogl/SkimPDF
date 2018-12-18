# -*- coding: utf-8 -*-
"""
skim_pdf.

Embed Skim notes as PDF notes or convert PDF notes to Skim notes.
Date: 2018-12-18
Version: 1.1
Author: Alexander Gogl
"""

from os import system, walk, path


class SkimPDF(object):
    """docstring for SkimPDF."""
    def __init__(self):
        self.skimpdf_path = '/Applications/Skim.app/Contents/SharedSupport/skimpdf'
        self.embed_suffix = '_embedded'
        self.unembed_suffix = '_skim_notes'
        self.replace_original = True
        pass

    def convert_to_pdf_notes(self, in_pdf):
        """Embed skim notes to PDF notes."""
        if self.replace_original is False:
            out_pdf = "%s%s.pdf" % (in_pdf[:-4], self.embed_suffix)
        else:
            out_pdf = in_pdf

        # Embed notes
        cmd = '%s embed "%s" "%s"' % (self.skimpdf_path, in_pdf, out_pdf)

        result = system(cmd)

        # Compose message
        if result == 0:
            message = "Embeded notes to '%s'" % out_pdf
        else:
            message = result

        return message

    def batch_convert_to_pdf_notes(self, folder):
        """Loop through directories in given folder and embed notes."""
        messages = []
        i = 0
        for path, subdirs, files in walk(folder):
            for name in files:
                if name.endswith(".pdf"):
                    i += 1
                    # embed notes to pdf
                    pdf_file = "%s/%s" % (path, name)
                    result = skim.convert_to_pdf_notes(pdf_file)
                    # add result message to report
                    messages.append(result)
                    # report current state
                    print(i)

        self.report(messages)
        pass

    def convert_to_skim_notes(self, in_pdf):
        """Convert PDF notes to Skim notes (unembed)."""
        if self.replace_original is False:
            out_pdf = "%s%s.pdf" % (in_pdf[:-4], self.skim_suffix)
        else:
            out_pdf = in_pdf

        # Convert PDF notes to Skim notes
        cmd = '%s unembed "%s" "%s"' % (self.skimpdf_path, in_pdf, out_pdf)

        result = system(cmd)

        # Compose message
        if result == 0:
            message = "Converted PDF notes to Skim notes in '%s'" % out_pdf
        else:
            message = result

        return message

    def batch_convert_to_skim_notes(self, folder):
        """Loop through directories in given folder and embed notes."""
        messages = []
        i = 0
        for path, subdirs, files in walk(folder):
            for name in files:
                if name.endswith(".pdf"):
                    i += 1
                    # embed notes to pdf
                    pdf_file = "%s/%s" % (path, name)
                    result = skim.convert_to_skim_notes(pdf_file)
                    # add result message to report
                    messages.append(result)
                    # report current state
                    print(i)

        self.report(messages)
        pass

    def report(self, messages):
        """Print list of processed pdfs."""
        print("\n\nProcessing PDFs done:")

        for i in range(len(messages)):
            message = "%s: %s" % (i + 1, messages[i])
            print(message)
        pass


skim = SkimPDF()
skim.replace_original = False

skim.embed_notes('../test/test.pdf')
# skim.convert_to_skim_notes('../test/test.pdf')

# batch embeding process with path to folder with literature
# skim.batch_convert_to_pdf_notes('../test')
