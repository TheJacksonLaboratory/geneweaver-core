"""Mapping definitions."""

from geneweaver.core.enum import GeneIdentifier, Species

AON_ID_TYPE_FOR_SPECIES = {
    Species.MUS_MUSCULUS: GeneIdentifier.MGI,
    Species.HOMO_SAPIENS: GeneIdentifier.HGNC,
    Species.RATTUS_NORVEGICUS: GeneIdentifier.RGD,
    Species.DANIO_RERIO: GeneIdentifier.ZFIN,
    Species.DROSOPHILA_MELANOGASTER: GeneIdentifier.FLYBASE,
    Species.MACACA_MULATTA: GeneIdentifier.ENTREZ,
    Species.CAENORHABDITIS_ELEGANS: GeneIdentifier.WORMBASE,
    Species.SACCHAROMYCES_CEREVISIAE: GeneIdentifier.SGD,
    Species.GALLUS_GALLUS: GeneIdentifier.CGNC,
    Species.CANIS_FAMILIARIS: GeneIdentifier.ENTREZ,
}
