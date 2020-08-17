# SkimPDF

[Skim](https://skim-app.sourceforge.io/) is a PDF viewer with great search and annotation tools for OSX. It stores annotations in a non-standard format, thus the annotation can not viewed or edited in other PDF viewer like Adobe Acrobat Reader. However, Skim can convert Skim notes to standard PDF notes (embed) or make PDF notes editable in Skim (unembed).

![](img/example-skim.png)
PDF viewed in Skim with Skim annotations.

![](img/example-acrobat.png)
The same PDF with embedded annotations viewed in Adobe Acrobat Reader DC.

## How it works

The Python class `SkimPDF` builds on `skimpdf` to automate the conversion step:

1. Embed notes
2. Unembed notes
3. Batch embed and unembed notes (works with nested folders)

I have used the script to embed Skim notes of 568 pdfs scattered in a folder with various subfolders. It took about 5 minutes. Be aware, that the script won't process files with a `"` in its filepath and that the files are overwritten, so make a copy before running on large sets of files.

## How to install and use it

There are three options how to use SkimPDF:

1. as an OSX automator workflow
2. as an Alfred Workflow, or
3. as a Python module

### OSX-Automator

For ease of use, I have wrapped the python script in the OSX Automator workflows `Convert to pdf notes.workflow` and `Convert to skim notes.workflow` to process one or more selected PDFs. The script detects if one PDF or multiple PDFs or folders have been selected and automatically batch processes it.

The workflows process a selected PDF file, or multiple PDFs, folders, and nested folders (batch processing). Non-PDF files are ignored. **WARNING:** The workflows replaces the selected files.

Install the workflow as an OSX service by:

1. download the SkimPDF Automator Workflows [here](https://github.com/alexandergogl/SkimPDF/releases/latest)
2. double-clicking on the donwloaded files `Convert to pdf notes.workflow` and `Convert to skim notes.workflow` and select "Install as service."

Start the workflow by

1. selecting PDF files or folders,
2. click right,
3. navigate to `services` (German: Dienste) > `PDF - Skim => PDF notes` or `PDF - PDF => Skim notes`

### Alfred Workflows

For ease of use, I have wrapped the python script in the [Alfred Workflows](https://www.alfredapp.com/) `PDF to Skim notes.alfredworkflow` and `Skim to PDF notes.alfredworkflow` to process one or more selected PDFs.

The workflows process a selected PDF file, or multiple PDFs, folders, and nested folders (batch processing). Non-PDF files are ignored. **WARNING:** The workflows overwrite the selected files.

Install the workflow as an Alfred workflow by:

1. download the Alfred Workflows [here](https://github.com/alexandergogl/SkimPDF/releases/latest)
2. double-clicking on the donwloaded files `PDF to Skim notes.alfredworkflow` and `Skim to PDF notes.alfredworkflow`. Be aware, that you need an active Alfred power user licence to enable custom workflows.

### Python module

If you need to have more control on the script like making a copy of the converted pdf instead of overwriting it, then you can access the Python class options by loading class as a module in a python script or via CLI.

Download the module from `src/skim_pdf.py` or [here](https://github.com/alexandergogl/SkimPDF/releases/latest) (Source code)

#### Available options

```
skim = SkimPDF()

# Path to skimpdf
skim.skimpdf_path = '/Applications/Skim.app/Contents/SharedSupport/skimpdf'

# Replace pdf or place a copy in place
skim.replace_original = True

# If skim.replace_original is set to False,
# then you can set the embed or unembed suffix
skim.embed_suffix = '_embedded'
skim.unembed_suffix = '_skim_notes'
```

#### Available methods

```
# Convert Skim notes to PDF notes (embed)
skim.convert_to_pdf_notes('../path/to/pdf file.pdf')

# Convert PDF notes to Skim notes (unembed)
skim.convert_to_skim_notes('../path/to/pdf file.pdf')

# Batch convert notes in a folder
skim.batch_convert_to_pdf_notes('../path/to/Literature folder')
skim.batch_convert_to_skim_notes('../path/to/Literature folder')
```
