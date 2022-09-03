from scidownl import scihub_download

paper = "https://doi.org/10.1017/jfm.2017.541"
paper_type = "doi"
# out = "./paper/one_paper.pdf"

out = "./paper/"
scihub_download(paper, paper_type=paper_type, out=out)

