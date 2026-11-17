import json, csv, pathlib, sys, platform
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.simulator import scenario, execute


def dump(path, rows):
    with open(path,'w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader();writer.writerows(rows)


def main():
    cfg=json.loads((ROOT/'configs/protocol.json').read_text())
    rows=[]
    for seed in cfg['seeds']:
        for length in cfg['scenario_lengths']:
            for j in range(cfg['trials_per_seed_length']):
                trial_id=seed*10000+j
                sc=scenario(seed,trial_id,length)
                for pol in ['none','fixed','adaptive']:
                    r=execute(sc,pol,cfg['low_risk_fault_probability'],cfg['high_risk_fault_probability'],
                              cfg['checkpoint_detection_probability'],cfg['fixed_checkpoint_interval'])
                    r['seed']=seed
                    rows.append(r)
    out=ROOT/'results';dump(out/'trial_results.csv',rows)
    agg=[]
    for (length,pol),part in sorted(group(rows,lambda r:(r['length'],r['policy'])).items()):
        agg.append(dict(length=length,policy=pol,n=len(part),
                        success_rate=mean(part,'task_success'),unsafe_run_rate=mean(part,'any_unsafe'),
                        mean_unsafe_actions=mean(part,'unsafe_actions'),mean_reviews=mean(part,'reviews'),
                        mean_recoveries=mean(part,'recoveries'),end_state_clean_rate=mean(part,'end_state_clean')))
    dump(out/'results.csv',agg)
    # Sensitivity: only the risk recognition recall changes. Identical scenario streams.
    sens=[]
    for recall in [0.5,0.75,1.0]:
        for length in cfg['scenario_lengths']:
            part=[]
            for seed in cfg['seeds']:
                for j in range(cfg['trials_per_seed_length']):
                    sc=scenario(seed,seed*10000+j,length)
                    part.append(execute(sc,'adaptive',risk_recall=recall))
            sens.append(dict(length=length,risk_recall=recall,n=len(part),
                             success_rate=mean(part,'task_success'),unsafe_run_rate=mean(part,'any_unsafe'),
                             mean_reviews=mean(part,'reviews')))
    dump(out/'sensitivity.csv',sens)
    log={'python':platform.python_version(),'platform':platform.platform(),'config':cfg,
         'total_primary_runs':len(rows),'sensitivity_runs':len(cfg['seeds'])*cfg['trials_per_seed_length']*len(cfg['scenario_lengths'])*3,
         'execution':'completed; all results produced by scripts/run_experiments.py'}
    (out/'execution_log.json').write_text(json.dumps(log,indent=2))
    print('PRIMARY COMPARISONS')
    for r in agg:print(r)
    print('SENSITIVITY')
    for r in sens:print(r)

def mean(rs,key):return round(sum(x[key] for x in rs)/len(rs),5)
def group(rows,keyfn):
    o=defaultdict(list)
    for r in rows:o[keyfn(r)].append(r)
    return o
if __name__=='__main__':main()
