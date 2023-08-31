##############################
Becky Lee's QC plot notebook
https://ghe-rss.roche.com/leeb38/Polarix/blob/master/FailedQC_analysis.ipynb
##############################

### Set up display
plt.rcParams['figure.dpi'] = 300

sns.set(style="whitegrid")


### Usage of lambda
df['col'].apply(lambda x: fill_in[x])
pd.concat([Table1, Table2], ignore_index=True).loc[:, ['col1', 'col2', 'col3']]
pd.read_csv().rename(columns={:,:,:})
failed = clia_sampleData.loc[clia_sampleData["SamplePassFail"]=="Fail"].reset_index(drop=True)

for row in range(failed_sample_count):
    sample_id, subject_id, sample_input = failed.at[row, "sampleID"], failed.at[row, "subjectID"], failed.at[row, "Input Mass (ng)"]
	df.at[4, 'B']
	
###	Boxplot + stripplot
fig, axes = plt.subplots(ncols=5, figsize=(25,5), tight_layout=True)

metrics = ["Plasma Volume (mL)", "Input Mass (ng)", "Extracted Mass (ng)", "Yield (ng/mL)", "Unique Depth Median"]
count = 0
for ax in fig.axes:
    sns.boxplot(ax=ax, data=polarix_filtered_qc, x="timepoint", y=metrics[count], whis=np.inf)
    sns.stripplot(ax=ax, data=polarix_filtered_qc, x="timepoint", y=metrics[count], color="black", size=3)
    ax.set_title(metrics[count])
    count+=1

axes[2].set_ylim(bottom=-5, top=200)
axes[3].set_ylim(bottom=-5, top=200)

plt.show()

### Horizontal bar plot to show percent of distribution
data = (polarix_filtered_qc.groupby(by=["timepoint"]).sum().loc[:,["Pass Input QC", "Pass Sequencing QC"]] *100/180).round(1).reindex(index = ["TCV ETTV", "C2D1", "C1D1"])
fig, ax = plt.subplots()
rects = ax.barh(width=data["Pass Input QC"], y=data.index, color="#55a868")
ax.bar_label(rects, label_type="center", color="white")
rects = ax.barh(width=100-data["Pass Input QC"], y=data.index, left=data["Pass Input QC"], color="#c44e52")
ax.bar_label(rects, label_type="center", color="white")
ax.legend(title="Input QC", labels=["Pass", "Fail"], loc="upper left", bbox_to_anchor=(1,1))
ax.set_title("Percent samples pass/fail Input QC")

plt.show()


### How to add legend in seaborn/matplotlib
ax.legend(title="Input QC", labels=["Pass", "Fail"], loc="upper left", bbox_to_anchor=(1,1))


### How to make heatmap in seaborn
sns.heatmap(ax=axes[0], data=matrix, annot=True, cmap="Blues", fmt='.0f', cbar=False, square=True, linecolor="black", linewidth=0.1, center=90)
sns.heatmap(ax=axes[1], data=matrix_norm, annot=True, cmap="Blues", fmt='.1f', cbar=False, square=True, linecolor="black", linewidth=0.1, center=50)
    
         
##############
https://ghe-rss.roche.com/leeb38/Share/blob/master/horizonal_bar_plots.ipynb
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
sns.set(style="whitegrid")


### How to make subplots 
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,8), sharey=True, constrained_layout=True)
data_cum = data.cumsum(axis=1)

### How to obtain color palette through matplotlib
https://matplotlib.org/stable/tutorials/colors/colormaps.html
category_colors = plt.get_cmap('RdYlGn')(
	np.linspace(0.15, 0.85, data.shape[1]))

### Operate on "ax"
fig, ax = plt.subplots(figsize=(9.2, 5))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())
axs[0].set_xlim(left=0.75, right=4.25) #add bumper space on both ends of x-axis
axs[0].set_xticks([1,2,3,4])
axs[0].set_ylabel("Subject IDs")
axs[0].set_xlabel("Scenarios")
axs[0].set_title("Scenario from C2D1 to TVC ETTV")

### Custom legend
##### https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html
axs[0].legend(handles = [Line2D([], [], marker="o", color="black", fillstyle="left", markeredgecolor="black", linestyle="None", markersize=10),
                         Line2D([], [], marker="s", color="black", fillstyle="left", markeredgecolor="black", linestyle="None", markersize=10),
                         Line2D([], [], marker="s", color='#4c72b0', fillstyle="left", markeredgecolor='#4c72b0', linestyle="None", markersize=10),
                         Line2D([], [], marker="s", color='#dd8452', fillstyle="left", markeredgecolor='#dd8452', linestyle="None", markersize=10),
                         Line2D([], [], marker="s", color='#55a868', fillstyle="left", markeredgecolor='#55a868', linestyle="None", markersize=10),
                         Line2D([], [], marker="s", color='#8172b3', fillstyle="left", markeredgecolor='#8172b3', linestyle="None", markersize=10)],
              labels = ["No Scenario Change",
                        "TVC ETTV Scenario",
                        "TVC ETTV Scenario 1",
                        "TVC ETTV Scenario 2",
                        "TVC ETTV Scenario 3",
                        "TVC ETTV Scenario 4"],
              ncol = 2,
              loc = "center",
              bbox_to_anchor = (0.5,-0.15))



### Shapes on top of plots
#Dots for ctDNA-
axs[0].plot(plot_df_no_width.query("mono_fill_color=='white'").bar_start_pos,
            plot_df_no_width.query("mono_fill_color=='white'").subjectID,
            color="white",
            marker="o",
            linestyle="",
            markeredgecolor="black")

#Squares for ctDNA+
axs[0].plot(plot_df_bars_only.query("mono_fill_color=='black'").end_scenario,
            plot_df_bars_only.query("mono_fill_color=='black'").subjectID,
            color="black",
            marker="s",
            linestyle="",
            markeredgecolor="black")

#Squares for ctDNA-
axs[0].plot(plot_df_bars_only.query("mono_fill_color=='white'").end_scenario,
            plot_df_bars_only.query("mono_fill_color=='white'").subjectID,
            color="white",
            marker="s",
            linestyle="",
            markeredgecolor="black")
            
            
            
# How to set log scale
ax.set_[xy]scale(scale, ...), linear, log, symlog, logit
ticket.LogLocator(base=10, numticks=15)

# Log Locator
ax = plt.subplot(n, 1, 8)
setup(ax)
ax.set_xlim(10**3, 10**10)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
ax.text(0.0, 0.1, "LogLocator(base=10, numticks=15)",
        fontsize=15, transform=ax.transAxes)

# Scatterplot transparency
ax.scatter(X,Y, 40, "C1", lw=0, alpha=0.1)
sns_plt.get_xaxis().set_major_formatter(
    mtick.FuncFormatter(lambda x, _: "{:.0f}".format(10 ** x))
)

# How to customize the ticker
import matplotlib.ticker as mtick



# How to annotate
sns_plt.axvline(np.log10(5), ls='-', color='black')
sns_plt.text(np.log10(5), 10, "5ng (89% of samples)", horizontalalignment='right', size='medium', color='black', rotation="vertical") 
