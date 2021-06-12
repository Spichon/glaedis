import {IRun} from '../../interfaces';
import {RunState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const mutations = {
    setRuns(state: RunState, payload: IRun[]) {
        state.runs = payload;
    },
};

const {commit} = getStoreAccessors<RunState, State>('');

export const commitSetRuns = commit(mutations.setRuns);

