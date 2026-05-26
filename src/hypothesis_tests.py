from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency


def perform_ttest(group_a, group_b):
    """
    Performs independent t-test.
    """

    stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False,
        nan_policy='omit'
    )

    return stat, p_value

def perform_chi2_test(contingency_table):
    """
    Performs chi-squared test.
    """

    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return chi2, p_value