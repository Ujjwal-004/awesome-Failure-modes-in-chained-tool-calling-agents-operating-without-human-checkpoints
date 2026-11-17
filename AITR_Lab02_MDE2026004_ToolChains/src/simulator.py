"""Deterministic synthetic chained-tool execution benchmark; no LLM API calls."""
from dataclasses import dataclass
from random import Random

@dataclass(frozen=True)
class Scenario:
    trial_id: int
    length: int
    fault_draws: tuple
    detect_draws: tuple
    risks: tuple
    risk_noise: tuple


def scenario(seed, trial_id, length):
    rng=Random(seed*1000003+trial_id*1009+length)
    return Scenario(trial_id,length,tuple(rng.random() for _ in range(length)),
                    tuple(rng.random() for _ in range(length)),
                    tuple(rng.random()<0.30 for _ in range(length)),
                    tuple(rng.random() for _ in range(length)))


def execute(sc, policy, error_low=0.035, error_high=0.17, detection=0.92,
            fixed_interval=4, risk_recall=1.0):
    corrupted=False
    reviews=0; recovered=0; initial_errors=0; unsafe=0; first_error=-1
    for i in range(sc.length):
        high=sc.risks[i]
        # Risk-adaptive safeguard checks the inherited state BEFORE risky execution.
        if policy=='adaptive' and high and sc.risk_noise[i]<risk_recall:
            reviews+=1
            if corrupted and sc.detect_draws[i]<detection:
                corrupted=False
                recovered+=1
        p=error_high if high else error_low
        new_fault=sc.fault_draws[i]<p
        if new_fault:
            initial_errors+=1
            if first_error==-1: first_error=i+1
            corrupted=True
        if high and corrupted:
            unsafe+=1
        # Fixed periodic review occurs AFTER tool execution.
        if policy=='fixed' and (i+1)%fixed_interval==0:
            reviews+=1
            if corrupted and sc.detect_draws[i]<detection:
                corrupted=False
                recovered+=1
    return {'trial_id':sc.trial_id,'length':sc.length,'policy':policy,
            'task_success':int(not corrupted and unsafe==0), 'end_state_clean':int(not corrupted),
            'unsafe_actions':unsafe,'any_unsafe':int(unsafe>0),'reviews':reviews,
            'recoveries':recovered,'initial_faults':initial_errors,'first_error_step':first_error,
            'risk_recall':risk_recall}
