def write_df_to_csv(info_file, index=False):
    """Write a data frame to a csv file"""
    df, file_name = info_file
    df.to_csv(file_name, index=index)
    return file_name
