import pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.simulator import scenario,execute,Scenario
s=scenario(11,1,12)
a=execute(s,'fixed');b=execute(s,'fixed')
assert a==b, 'same seed must reproduce identical result'
assert execute(s,'none')['reviews']==0
assert execute(s,'fixed')['reviews']==3
assert execute(s,'adaptive')['reviews']==sum(s.risks)
# With perfect detectors, no faults, each policy succeeds.
clean=Scenario(1,6,(0.99,)*6,(0.0,)*6,(False,)*6,(0.0,)*6)
assert all(execute(clean,p)['task_success']==1 for p in ['none','fixed','adaptive'])
# A fault at an irreversible action is unsafe even if a post-action check removes corrupted state.
bad=Scenario(1,1,(0.0,),(0.0,),(True,),(0.0,))
assert execute(bad,'adaptive')['any_unsafe']==1
assert execute(bad,'adaptive')['task_success']==0
print('PASS: deterministic replay, policy review counts, clean workflow, irreversible-action safety')
