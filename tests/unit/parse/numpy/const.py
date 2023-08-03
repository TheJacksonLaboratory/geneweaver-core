import numpy as np

valid_geneset_array = np.array([("GeneA", 1.2), ("GeneB", 2.5)])

valid_labeled_geneset_array = np.array(
    [("GeneA", 1.2), ("GeneB", 2.5)], dtype=[("Symbol", "U10"), ("Value", "f8")]
)
valid_labeled_geneset_array_2 = np.array(
    [("GeneC", 3.6), ("GeneD", 4.7)], dtype=[("Symbol", "U10"), ("Score", "f8")]
)
valid_labeled_geneset_array_3 = np.array(
    [("GeneE", 5.8), ("GeneF", 6.9)], dtype=[("GeneID", "U10"), ("PValue", "f8")]
)
valid_labeled_geneset_array_4 = np.array(
    [("GeneG", 7.1), ("GeneH", 8.2)], dtype=[("Gene_ID", "U10"), ("QValue", "f8")]
)
valid_labeled_geneset_array_5 = np.array(
    [("GeneI", 9.3), ("GeneJ", 10.4)], dtype=[("Gene ID", "U10"), ("Effect", "f8")]
)
valid_labeled_geneset_array_6 = np.array(
    [("GeneK", 11.5), ("GeneL", 12.6)], dtype=[("GeneID", "U10"), ("Correlation", "f8")]
)

valid_gt_2_labeled_geneset_array = np.array(
    [("GeneA", 1.2, 3.6), ("GeneB", 2.5, 4.7)],
    dtype=[("Symbol", "U10"), ("Value", "f8"), ("Score", "f8")],
)
valid_gt_2_labeled_geneset_array_2 = np.array(
    [("GeneC", 3.6, 5.8), ("GeneD", 4.7, 6.9)],
    dtype=[("Symbol", "U10"), ("Score", "f8"), ("PValue", "f8")],
)

empty_array = np.array([], dtype=[("Symbol", "U10"), ("Value", "f8")])

missing_symbol_array = np.array([(1.2,), (2.5,)], dtype=[("Value", "f8")])
missing_value_array = np.array([("GeneA",), ("GeneB",)], dtype=[("Symbol", "U10")])
missing_symbol_array_2 = np.array([(13.7,), (14.8,)], dtype=[("Score", "f8")])
missing_symbol_array_3 = np.array([(15.9,), (16.0,)], dtype=[("PValue", "f8")])
missing_value_array_2 = np.array([("GeneM",), ("GeneN",)], dtype=[("Gene_ID", "U10")])
missing_value_array_3 = np.array([("GeneO",), ("GeneP",)], dtype=[("Gene ID", "U10")])
