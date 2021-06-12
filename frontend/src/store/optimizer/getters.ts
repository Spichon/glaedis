import { OptimizerState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    optimizers: (state: OptimizerState) => state.optimizers,
    oneOptimizer: (state: OptimizerState) => (optimizerId: number) => {
        const filteredOptimizers = state.optimizers.filter((optimizer) => optimizer.id === optimizerId);
        if (filteredOptimizers.length > 0) {
            return { ...filteredOptimizers[0] };
        }
    },
};

const { read } = getStoreAccessors<OptimizerState, State>('');

export const readOneOptimizer = read(getters.oneOptimizer);
export const readOptimizers = read(getters.optimizers);
