import {IOptimizer} from '../../interfaces';
import {OptimizerState} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';

export const mutations = {
    setOptimizers(state: OptimizerState, payload: IOptimizer[]) {
        state.optimizers = payload;
    },
};

const {commit} = getStoreAccessors<OptimizerState, State>('');

export const commitSetOptimizers = commit(mutations.setOptimizers);

