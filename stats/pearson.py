import numpy

def compute_pearson(self, *datasets):
    dataset_length = None
    for d in datasets:
        if len(d) != dataset_length and not dataset_length:
            raise ValueError("Datasets are of unequal length")

    

    float(sum(l))/len(l) if len(l) > 0 else float('nan')
    return numpy.corrcoef(datasets)
