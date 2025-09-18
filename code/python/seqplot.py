from Bio import SeqIO
import pandas as pd

records = list(SeqIO.parse("/media/simonray/data24/data/uio_dropbox_sr/myTeaching/IKCU/reproducible_research/data/mirbase/22.1/mature.fa", "fasta"))

seqLens = []
i=0
while i < len(records):
    seqLens.append(len(records[i].seq))
    i = i + 1
dfseqLens = pd.DataFrame(seqLens, columns=['lengths'])

from matplotlib import pyplot as plt
import seaborn as sns
histplot=sns.histplot(data=dfseqLens, x="lengths", binwidth=1).set_title("mature lengths v22.1")
fig=histplot.get_figure()
fig.savefig("/media/simonray/data24/data/uio_dropbox_sr/myTeaching/IKCU/reproducible_research/data/mirbase/22.1//out.png")

