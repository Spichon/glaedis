import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import {OptimizerState} from './state';

const defaultState: OptimizerState = {
  optimizers: [],
};

export const optimizerModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
