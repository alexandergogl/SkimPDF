# SkimPDF

Python script to batch embed Skim notes to PDFs. I used it to embed 568 pdfs scattered in a folder with various subfolders. It took 300 seconds. Be aware, that the script won't process files with a `"` in its filepath.



### Available options

* Replace pdf or place a copy in place: `skim.replace = True`

* Set the embed suffix (if `skim.replace` is `False`): `skim.embed_suffix = '_embeded'`

### Functions

* Embed notes of a simgle pdf: `skim.embed_notes('../path/to/pdf file.pdf')`

* Batch embed notes to pdfs in folder: `skim.embed_notes_batch('../path/to/Literature folder')`
