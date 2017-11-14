# This script contains everything the whole sequence of things to do
# to get our results.

import networkx as nx

from read_graph import read_graph
from common.pipeline import Pipeline
from common.feature_generators import *

# Loading PPI graph
Graph, node_names = read_graph(directed=False)
print("Loaded graph:\n\t{} nodes\n\t{} edges".format(
    Graph.number_of_nodes(),
    Graph.number_of_edges()
    ))

#########################
# Computing node features
#########################

# The pipeline object takes as an argument the sequence of features we want
pipeline = Pipeline(Degree(), ExpectedDegree())
features = pipeline.apply(Graph, verbose=True)


#########################
# Learning
#########################

gene_list, gene_rank = [], []

#########################
# Validation
#########################

#Perform gene set enrichment analysis (GSEA) on a variety of gene sets directories
gene_sets_directories = [u'Cancer_Cell_Line_Encyclopedia', u'ChEA_2016', u'DrugMatrix', u'GeneSigDB', u'KEGG_2016', u'LINCS_L1000_Chem_Pert_down', u'LINCS_L1000_Chem_Pert_up', u'MSigDB_Computational', u'MSigDB_Oncogenic_Signatures', u'OMIM_Disease', u'OMIM_Expanded', u'PPI_Hub_Proteins', u'Panther_2016', u'Reactome_2016']
enrichr = enrichr_validation(gene_list, gene_rank=None, outdir="validation_results", gene_sets='KEGG_2016')
prerank = prerank_validation(gene_list, gene_rank, outdir="validation_results", gene_sets='KEGG_2016')

#Extract relevant gene lists
cancer = get_cancer()
mendelian = get_mendelian()
drugbank_target_all = get_drugbank(molecule_type="target", subset="all")
drugbank_target_approved = get_drugbank(molecule_type="target", subset="approved")
drugbank_enzyme_all = get_drugbank(molecule_type="enzyme", subset="all")
drugbank_enzyme_approved = get_drugbank(molecule_type="enzyme", subset="approved")
drugbank_carrier_all = get_drugbank(molecule_type="carrier", subset="all")
drugbank_carrier_approved = get_drugbank(molecule_type="carrier", subset="approved")
drugbank_transporter_all = get_drugbank(molecule_type="transporter", subset="all")
drugbank_transporter_approved = get_drugbank(molecule_type="transporter", subset="approved")



