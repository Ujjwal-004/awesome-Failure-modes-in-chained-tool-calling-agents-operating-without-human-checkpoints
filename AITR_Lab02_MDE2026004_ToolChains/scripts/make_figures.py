import csv,pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=pathlib.Path(__file__).resolve().parents[1]
R=ROOT/'results';F=R/'figures'
with (R/'results.csv').open() as f:rows=list(csv.DictReader(f))
with (R/'sensitivity.csv').open() as f:sens=list(csv.DictReader(f))
for metric,ylabel,name in [('success_rate','Strict task success rate','success_by_length'),('unsafe_run_rate','Fraction of runs with unsafe action','unsafe_by_length'),('mean_reviews','Human reviews per chain','review_cost')]:
    fig,ax=plt.subplots(figsize=(7,4.4))
    for p in ['none','fixed','adaptive']:
        ss=[x for x in rows if x['policy']==p]
        ax.plot([int(x['length']) for x in ss],[float(x[metric]) for x in ss],marker='o',label=p)
    ax.set(xlabel='Chain length (tool calls)',ylabel=ylabel);ax.legend();ax.grid(alpha=.25);fig.tight_layout()
    fig.savefig(F/(name+'.png'),dpi=170);fig.savefig(F/(name+'.pdf'));plt.close(fig)
fig,ax=plt.subplots(figsize=(7,4.4))
for length in [6,12,24]:
    ss=[x for x in sens if int(x['length'])==length]
    ax.plot([float(x['risk_recall']) for x in ss],[float(x['success_rate']) for x in ss],marker='o',label=f'length {length}')
ax.set(xlabel='Risk detector recall (simulated)',ylabel='Strict task success rate');ax.legend();ax.grid(alpha=.25);fig.tight_layout()
fig.savefig(F/'risk_sensitivity.png',dpi=170);fig.savefig(F/'risk_sensitivity.pdf');plt.close(fig)
