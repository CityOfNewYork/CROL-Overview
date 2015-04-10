import pandas as pd


# Todo: refactor; parametrize
def pivot_df(df,
             groupby=['AgencyName', 'TypeOfNoticeDescription'],
             colnames=['RequestID', 'StartDate', 'EndDate',
                       'AgencyCode', 'AgencyName', 'AgencyDivision',
                       'TypeOfNoticeCode', 'TypeOfNoticeDescription',
                       'ShortTitle', 'SectionID', 'SectionName', 'DueDate',
                       'ConfirmationNumber', 'AdditionalDescription']
             ):

    grouped = df[colnames].groupby(groupby)
    return pd.DataFrame(grouped.count('RequestID')['RequestID']) \
             .rename(columns={'RequestID': 'MessageCount'}) \
             .sort(['MessageCount'], ascending=[0])
