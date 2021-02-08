import pandas as pd


def to_lower_arr(arr: list) -> list:
    """Функция переводит все к общему регистру"""
    return_arr = []
    for i in arr:
        return_arr.append(i.lower())
    return return_arr


def get_value(dict_data: dict, a: list, b: list, c: list, d: list, e: list, f: list, g: list):
    def result(letters, key_value, item_value):
        for i in letters:
            if i.split(' (')[0] == key_value.lower():
                return item_value
        return 0

    a_result, b_result, c_result, d_result, e_result, f_result, g_result = 0, 0, 0, 0, 0, 0, 0
    for key, item in dict_data.items():
        a_result += result(a, key, item)
        b_result += result(b, key, item)
        c_result += result(c, key, item)
        d_result += result(d, key, item)
        e_result += result(e, key, item)
        f_result += result(f, key, item)
        g_result += result(g, key, item)
    return {"p1": a_result, "p2": b_result, "p3": c_result, "p4": d_result, "p5": e_result, "p6": f_result,
            "p7": g_result}


def main():
    df_scopus_oecd = pd.read_excel('scopus_oecd.xlsx')
    df_scopus_date = pd.read_excel('2016.xlsx')

    df_result = pd.merge(left=df_scopus_date, right=df_scopus_oecd, left_on='Направление', right_on='направление')
    df_result.to_excel("result.xlsx")

    a_priority = to_lower_arr(pd.read_excel('a.xlsx')['a'].values)
    b_priority = to_lower_arr(pd.read_excel('b.xlsx')['b'].values)
    c_priority = to_lower_arr(pd.read_excel('c.xlsx')['c'].values)
    d_priority = to_lower_arr(pd.read_excel('d.xlsx')['d'].values)
    e_priority = to_lower_arr(pd.read_excel('e.xlsx')['e'].values)
    f_priority = to_lower_arr(pd.read_excel('f.xlsx')['f'].values)
    g_priority = to_lower_arr(pd.read_excel('g.xlsx')['g'].values)

    df_scopus_date_name = df_scopus_date['Направление']
    df_scopus_date_value = df_scopus_date['количество']

    df_scopus_date_dict = dict(zip(df_scopus_date_name, df_scopus_date_value))
    result = get_value(df_scopus_date_dict, a_priority, b_priority, c_priority, d_priority, e_priority, f_priority,
                       g_priority)

    result_df = pd.DataFrame(result, index=['']).T
    result_df.to_excel("result_ntr_year.xlsx")
    # print(a_priority)
