# -*- coding: utf-8 -*-
"""
skim_pdf.

Embed Skim notes as PDF notes or convert PDF notes to Skim notes.
Date: 2019-01-30
Version: 1.2
Author: Alexander Gogl
"""

import sys
import os
# import system, walk, path, argv


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

        os.system(cmd)
        pass

    def batch_convert_to_pdf_notes(self, folder):
        """Loop through directories in given folder and embed notes."""
        messages = []
        i = 0
        for path, subdirs, files in os.walk(folder):
            for name in files:
                if name.endswith(".pdf"):
                    i += 1
                    # embed notes to pdf
                    pdf_file = "%s/%s" % (path, name)
                    skim.convert_to_pdf_notes(pdf_file)

        return i

    def convert_to_skim_notes(self, in_pdf):
        """Convert PDF notes to Skim notes (unembed)."""
        if self.replace_original is False:
            out_pdf = "%s%s.pdf" % (in_pdf[:-4], self.skim_suffix)
        else:
            out_pdf = in_pdf

        # Convert PDF notes to Skim notes
        cmd = '%s unembed "%s" "%s"' % (self.skimpdf_path, in_pdf, out_pdf)

        os.system(cmd)
        pass

    def batch_convert_to_skim_notes(self, folder):
        """Loop through directories in given folder and embed notes."""
        messages = []
        i = 0
        for path, subdirs, files in os.walk(folder):
            for name in files:
                if name.endswith(".pdf"):
                    i += 1
                    # embed notes to pdf
                    pdf_file = "%s/%s" % (path, name)
                    skim.convert_to_skim_notes(pdf_file)

        return i


skim = SkimPDF()
skim.replace_original = True

paths = sys.argv[1:]

if len(paths) > 1:
	# Multiple elements selected
	i = 0
	for path in paths:
		if os.path.isdir(path):
			i += skim.batch_convert_to_skim_notes(path)
		else:
			skim.convert_to_skim_notes(path)
			i += 1
else:
	# one element selected
	path = paths[0]
	if os.path.isdir(path):
		i = skim.batch_convert_to_skim_notes(path)
	else:
		skim.convert_to_skim_notes(path)
		i = 1

message = 'Converted %s files with pdf notes to skim notes' % i
print(message)
