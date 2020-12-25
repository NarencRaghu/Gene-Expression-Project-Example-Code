import csv
with open('C:/Users/Naren/.spyder-py3/results.csv') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    listofgenes = []
    i=0
    for row in csvreader:
        if i<10:
            if row[2] == 'gene_symbol':
                continue
            else:
                listofgenes.append(row[2])
                i+=1
from brainrender import Scene
from brainrender import settings
from brainrender.atlas_specific import GeneExpressionAPI


for genes in listofgenes:
    settings.SHOW_AXES = False
    scene = Scene(inset=False)
    gene = genes
    geapi = GeneExpressionAPI()
    expids = geapi.get_gene_experiments(gene)
    if len(expids) > 1:
        data = geapi.get_gene_data(gene, expids[1])
    else:
        data = geapi.get_gene_data(gene, expids[0])
    gene_actor = geapi.griddata_to_volume(data, min_quantile=99, cmap="inferno")
    act = scene.add(gene_actor)
    scene.add_silhouette(act)
    
    scene.render(zoom=1.6)