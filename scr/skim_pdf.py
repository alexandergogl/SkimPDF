# -*- coding: utf-8 -*-

from os import system, walk, path


class SkimPDF(object):
    """docstring for SkimPDF."""
    def __init__(self):
        self.skimpdf_path = '/Applications/Skim.app/Contents/SharedSupport/skimpdf'
        self.embed_suffix = '_embeded'
        self.replace = False
        pass

    def embed_notes(self, in_pdf):
        """Embed skim notes to PDF."""
        if self.replace is False:
            out_pdf = "%s%s.pdf" % (in_pdf[:-4], self.embed_suffix)
        else:
            out_pdf = in_pdf

        # Embed notes
        cmd = '%s embed "%s" "%s"' % (self.skimpdf_path, in_pdf, out_pdf)

        result = system(cmd)

        # Compose message
        if result == 0:
            message = "Embeded notes to '%s'" % in_pdf
        else:
            message = result

        return message

    def embed_notes_batch(self, folder):
        """Loop through directories in given folder and embed notes."""
        messages = []
        i = 0
        for path, subdirs, files in walk(folder):
            for name in files:
                if name.endswith(".pdf"):
                    i += 1
                    # embed notes to pdf
                    pdf_file = "%s/%s" % (path, name)
                    result = skim.embed_notes(pdf_file)
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
skim.replace = True

# batch embeding process with path to folder with literature
skim.embed_notes_batch('../Literature')
