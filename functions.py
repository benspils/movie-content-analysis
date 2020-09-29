

def bar_plot_success(groupby,label):
    
    %matplotlib inline
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    figure, ax = plt.subplots(2, 2, figsize=(30, 30))
    x=master_table.groupby(groupby).mean().index
    y0_gross_rev= master_table.groupby(groupby).mean().worldwide_gross
    y1_net_prof= master_table.groupby(groupby).mean().worldwide_gross-master_table.groupby(groupby).mean().production_budget
    y2_roi_percent= master_table.groupby(groupby).mean().worldwide_gross/master_table.groupby(groupby).mean().production_budget
    y3_comp= master_table.groupby(groupby).mean().success_score 

    ax[0][0].set_title('Gross Revenue vs {}'.format(label))
    ax[0][0].set_xlabel('{}'.format(label))
    ax[0][0].set_ylabel('Gross Revenue ($)')
    ax[0][1].set_title('Net Profit vs {}'.format(label))
    ax[0][1].set_xlabel('{}'.format(label))
    ax[0][1].set_ylabel('Net Profit ($)')
    ax[1][0].set_title('Percent Return on Investment vs {}'.format(label))
    ax[1][0].set_xlabel('{}'.format(label))
    ax[1][0].set_ylabel('ROI (%)')
    ax[1][1].set_title('Composite Success Score vs {}'.format(label))
    ax[1][1].set_xlabel('{}'.format(label))
    ax[1][1].set_ylabel('Success Score')

    ax[0][0].set_xticklabels(x,rotation=45)
    ax[0][1].set_xticklabels(x,rotation=45)
    ax[1][0].set_xticklabels(x,rotation=45)
    ax[1][1].set_xticklabels(x,rotation=45)

    ax[0][0].spines['top'].set_visible(False)
    ax[0][0].spines['right'].set_visible(False)
    ax[0][0].spines['left'].set_visible(False)
    ax[0][0].spines['bottom'].set_color('#DDDDDD')

    ax[0][1].spines['top'].set_visible(False)
    ax[0][1].spines['right'].set_visible(False)
    ax[0][1].spines['left'].set_visible(False)
    ax[0][1].spines['bottom'].set_color('#DDDDDD')

    ax[1][0].spines['top'].set_visible(False)
    ax[1][0].spines['right'].set_visible(False)
    ax[1][0].spines['left'].set_visible(False)
    ax[1][0].spines['bottom'].set_color('#DDDDDD')

    ax[1][1].spines['top'].set_visible(False)
    ax[1][1].spines['right'].set_visible(False)
    ax[1][1].spines['left'].set_visible(False)
    ax[1][1].spines['bottom'].set_color('#DDDDDD')

    sns.set_style("whitegrid")
    sns.barplot(x, y0_gross_rev, ax=ax[0][0], color='green')
    sns.barplot(x, y1_net_prof, ax=ax[0][1], color='yellow')
    sns.barplot(x, y2_roi_percent, ax=ax[1][0], color='blue')
    sns.barplot(x, y3_comp, ax=ax[1][1], palette='YlGn')
    
    return figure