import { RunState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    runs: (state: RunState) => state.runs,
    oneRun: (state: RunState) => (runId: number) => {
        const filteredRuns = state.runs.filter((run) => run.id === runId);
        if (filteredRuns.length > 0) {
            return { ...filteredRuns[0] };
        }
    },
};

const { read } = getStoreAccessors<RunState, State>('');

export const readOneRun = read(getters.oneRun);
export const readRuns = read(getters.runs);
