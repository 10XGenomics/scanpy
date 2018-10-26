import scanpy.api as sc


def test_read_10x_mtx():
    sc.read_10x_mtx('./_data/10x_data/1.2.0/filtered_gene_bc_matrices/hg19_chr21/',
                    var_names='gene_symbols', cache=True)
    sc.read_10x_mtx('./_data/10x_data/3.0.0/filtered_feature_bc_matrix/',
                    var_names='gene_symbols', cache=True)


def test_read_10x_h5():
    sc.read_10x_h5('_data/10x_data/1.2.0/filtered_gene_bc_matrices_h5.h5', genome='hg19_chr21')
    sc.read_10x_h5('_data/10x_data/3.0.0/filtered_feature_bc_matrix.h5', genome='GRCh38_chr21')
