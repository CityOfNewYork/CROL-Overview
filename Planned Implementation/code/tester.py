import pandas as pd

def evaluate_parser(filepath, gold_parse_colname,
                    proposed_parser, source_col="AdditionalDescription"):
    """
    Given an input .csv, a proposed parsing function, and a column containing
    correct parses, return a dataframe with proposed parses and a column assessing
    correctness.
    
    Example usage (just for show):
    x = evaluate_parser('procPublicationRequest Oct-Dec 2014 (Updated) - Sheet1-2.csv',
                        'TypeOfNoticeCode',lambda x: 13)
    x.agreement.describe()
    Out[26]: 
        count          478
        mean     0.4539749
        std      0.4983988
        min          False
        25%              0
        50%              0
        75%              1
        max           True

    To see correct parses:
    x.AdditionalDescription[x.agreement]
    
    And wrong parses:
    x.AdditionalDescription[-x.agreement]

    """
    our_df = pd.read_csv(filepath)
    our_df['proposed_parse'] = our_df[source_col].apply(proposed_parser)
    our_df['agreement'] = (our_df['proposed_parse'] == our_df[gold_parse_colname])
    return our_df