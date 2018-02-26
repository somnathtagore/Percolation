
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from(
	[('CTBP1','CDC23'),('CDC23','CTBP2'),('CDC23','BCAS3'),('BCAS3','CTBP2'),('KAT2B','CDC23'),('KAT2B','CTBP2'),('KAT2B','BCAS3')])
#,('POLR2A','EPAS1'),('POLR2A','EP300'),('POLR2A','PARP1'),('ESR1','CREBBP'),('ESR1','EPAS1'),('ESR1','EP300'),('ESR1','PARP1'),('ESR1','POLR2A'),('AR','ESR1'),('TP53','ESR1'),('AR','TP53'),('ESR1','RPA2'),('AR','RPA2'),('RPA2','TP53'),('RAD23A','ESR1'),('RAD23A','AR'),('RAD23A','TP53'),('RAD23A','RPA2'),('PRKDC','ESR1'),('PRKDC', 'AR'),('PRKDC', 'TP53'), ('PRKDC', 'RPA2'), ('PRKDC','RAD23A')])
#, ('CTBP2','CDC23'), ('CTBP2', 'KAT2B'), ('CTBP2','BCAS3'),('CDC23','KAT2B'), ('CDC23','BCAS3'),('KAT2B','BCAS3')])
#('EPAS1','AR'),('EPAS1','POLR2A'),('EPAS1','RPA2'),('EPAS1','EP300'),('EPAS1','CREBBP'),('RAD23A','ESR1'), ('RAD23A', 'PARP1'), ('RAD23A','PRKDC'),('RAD23A','AR'),('RAD23A','POLR2A'),('RAD23A','RPA2'),('RAD23A','EP300'),('RAD23A','CREBBP'),('ESR1','PARP1'), ('ESR1','PRKDC'),('ESR1','AR'),('ESR1','POLR2A'),('ESR1','RPA2'),('ESR1','EP300'),('ESR1','CREBBP'),('PARP1','PRKDC'),('PARP1','AR'),('PARP1','POLR2A'),('PARP1','RPA2'),('PARP1','EP300'),('PARP1','CREBBP'),('PRKDC','AR'),('PRKDC','POLR2A'),('PRKDC','RPA2'),('PRKDC','EP300'),('PRKDC','CREBBP'),('AR','POLR2A'),('AR','RPA2'),('AR','EP300'),('AR','CREBBP'),('POLR2A','RPA2'),('POLR2A','EP300'),('POLR2A','CREBBP'),('RPA2','EP300'),('RPA2','CREBBP'),('EP300','CREBBP')])
#[('HDAC1','BRCA1'),('HDAC1','KMT2A'), ('HDAC1', 'SMARCC1'), ('HDAC1','HDAC2'),('HDAC1','CREBBP'),('HDAC1','CTBP1'),('HDAC1','EP300'),('HDAC1','SMARCA4'),('HDAC1','NCOR2'),('HDAC1','NCOR1'),('BRCA1','KMT2A'), ('BRCA1', 'SMARCC1'), ('BRCA1','HDAC2'),('BRCA1','CREBBP'),('BRCA1','CTBP1'),('BRCA1','EP300'),('BRCA1','SMARCA4'),('BRCA1','NCOR2'),('BRCA1','NCOR1'),('KMT2A','SMARCC1'), ('KMT2A','HDAC2'),('KMT2A','CREBBP'),('KMT2A','CTBP1'),('KMT2A','EP300'),('KMT2A','SMARCA4'),('KMT2A','NCOR2'),('KMT2A','NCOR1'),('SMARCC1','HDAC2'),('SMARCC1','CREBBP'),('SMARCC1','CTBP1'),('SMARCC1','EP300'),('SMARCC1','SMARCA4'),('SMARCC1','NCOR2'),('SMARCC1','NCOR1'),('HDAC2','CREBBP'),('HDAC2','CTBP1'),('HDAC2','EP300'),('HDAC2','SMARCA4'),('HDAC2','NCOR2'),('HDAC2','NCOR1'),('CREBBP','CTBP1'),('CREBBP','EP300'),('CREBBP','SMARCA4'),('CREBBP','NCOR2'),('CREBBP','NCOR1'),('CTBP1','EP300'),('CTBP1','SMARCA4'),('CTBP1','NCOR2'),('CTBP1','NCOR1'),('EP300','SMARCA4'),('EP300','NCOR2'),('EP300','NCOR1'),('SMARCA4','NCOR2'),('SMARCA4','NCOR1'),('NCOR2','NCOR1')])
#[('KMT2A','SMARCC1'),('KMT2A','SMARCA4'),('KMT2A','CREBBP'),('SMARCC1','SMARCA4'),('SMARCC1','CREBBP'),('SMARCA4','CREBBP')])
#    [('TP53', 'ESR1'), ('TP53', 'PARP1'), ('TP53', 'EP300'), ('TP53','CREBBP'),('TP53','XRCC1'),('ESR1','PARP1'), ('ESR1', 'EP300'), ('ESR1','CREBBP'),('ESR1','XRCC1'),('PARP1','EP300'), ('PARP1','CREBBP'),('PARP1','XRCC1'),('EP300','CREBBP'),('EP300','XRCC1'),('CREBBP','XRCC1')])
#,('CREBBP1','EP300'),('HDAC1','SMARCA4'),('HDAC1','NCOR2'),('HDAC1','NCOR1'),('BRCA1','KMT2A'), ('BRCA1', 'SMARCC1'), ('BRCA1','HDAC2'),('BRCA1','CREBBP'),('BRCA1','CTBP1'),('BRCA1','EP300'),('BRCA1','SMARCA4'),('BRCA1','NCOR2'),('BRCA1','NCOR1'),('KMT2A','SMARCC1'), ('KMT2A','HDAC2'),('KMT2A','CREBBP'),('KMT2A','CTBP1'),('KMT2A','EP300'),('KMT2A','SMARCA4'),('KMT2A','NCOR2'),('KMT2A','NCOR1'),('SMARCC1','HDAC2'),('SMARCC1','CREBBP'),('SMARCC1','CTBP1'),('SMARCC1','EP300'),('SMARCC1','SMARCA4'),('SMARCC1','NCOR2'),('SMARCC1','NCOR1'),('HDAC2','CREBBP'),('HDAC2','CTBP1'),('HDAC2','EP300'),('HDAC2','SMARCA4'),('HDAC2','NCOR2'),('HDAC2','NCOR1'),('CREBBP','CTBP1'),('CREBBP','EP300'),('CREBBP','SMARCA4'),('CREBBP','NCOR2'),('CREBBP','NCOR1'),('CTBP1','EP300'),('CTBP1','SMARCA4'),('CTBP1','NCOR2'),('CTBP1','NCOR1'),('EP300','SMARCA4'),('EP300','NCOR2'),('EP300','NCOR1'),('SMARCA4','NCOR2'),('SMARCA4','NCOR1'),('NCOR2','NCOR1')])

#val_map = {'A': 1.0,
 #          'D': 0.5714285714285714,
 #          'H': 0.0}

#values = [val_map.get(node, 0.25) for node in G.nodes()]
#labels=nx.draw_networkx_labels(G,pos=nx.spring_layout(G))
#labels=nx.draw_networkx_labels(G)
#nx.draw(G, cmap = plt.get_cmap('jet'), node_color = values)
nx.draw(G, with_labels=True,node_size=4000,node_color='y')
plt.show()
